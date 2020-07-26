/*
 * SPDX-License-Identifier: Apache-2.0
 */

'use strict';

const { Contract } = require('fabric-contract-api');

class bsbri extends Contract {

    async initLedger(ctx) {
        console.info('============= START : Initialize Ledger ===========');
        const prefixs = [
            {
                prefix: 'xxx.xxx.xxx.xxx/xx',
                ASN: 'xx',
                act_stat: '0',
            },
        ];

        for (let i = 0; i < prefixs.length; i++) {
            var prefKey = prefixs[i].prefix;
            prefixs[i].docType = 'prefix';
            await ctx.stub.putState(prefKey, Buffer.from(JSON.stringify(prefixs[i])));
            console.info('Added <--> ', prefixs[i]);
        }
        console.info('============= END : Initialize Ledger ===========');
        
    }

    async createbsbri(ctx, prefKey, newPrefix, newASN,new_act_stat) {
        console.info('============= START : Create IP Prefix ===========');
        // check if the prefix exist in the ledger
        const checkData= await ctx.stub.getState(prefKey);
        if(!checkData || checkData.length===0){
            const pref = {
                docType: 'prefix',
                prefix: newPrefix,
                ASN: newASN,
                act_stat: new_act_stat,
            };
            await ctx.stub.putState(prefKey, Buffer.from(JSON.stringify(pref)));
            console.info('============= END : Create IP Prefix ===========');
            return('valid');
            
        }
        else{            
            const changePrefix = JSON.parse(checkData.toString())
            // if the the prefix belong the same ASN than update active status only
            // can be hapen during prefix withdrawal
            if (changePrefix.ASN === newASN && changePrefix.act_stat !== new_act_stat){
                changePrefix.act_stat = new_act_stat;
                await ctx.stub.putState(prefKey, Buffer.from(JSON.stringify(changePrefix)));
                console.info('=====New Active Status has been updated');
                return ('updated');
            }
            else{
                throw new Error(`${newPrefix} belong to other ASN or no update on active status`);
                return ('ilegal');    
            }       
        }    
    }

    async querybyKey(ctx, prefKey) {
        const prefAsBytes = await ctx.stub.getState(prefKey); // get the ip prefix from chaincode state
        if (!prefAsBytes || prefAsBytes.length === 0) {
            throw new Error(`${prefKey} does not exist`);
        }
        console.log(prefAsBytes.toString());
        return prefAsBytes.toString();
    }

    async queryAllbsbri(ctx,startkey,endkey) {
        const startKey = startkey;
        const endKey = endkey;
        const allResults = [];
        for await (const {key, value} of ctx.stub.getStateByRange(startKey, endKey)) {
            const strValue = Buffer.from(value).toString('utf8');
            let record;
            try {
                record = JSON.parse(strValue);
            } catch (err) {
                console.log(err);
                record = strValue;
            }
            allResults.push({ Key: key, Record: record });
        }
        console.info(allResults);
        return JSON.stringify(allResults);
    }
}

module.exports = bsbri;
