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
                ip_prefix: '1.1.113.0/24',
                ASN: '24',
                exp_stat: '0',
            },
            {
                ip_prefix: '1.1.116.0/24',
                ASN: '2519',
                exp_stat: '0',
            },
            {
                ip_prefix: '1.1.128.0/16',
                ASN: '23969',
                exp_stat: '0',
            },
            {
                ip_prefix: '1.6.196.0/24',
                ASN: '9583',
                exp_stat: '0',
            },
            {
                ip_prefix: '1.6.226.0/24',
                ASN: '132215',
                exp_stat: '0',
            },
            {
                ip_prefix: '1.22.88.0/24',
                ASN: '45528',
                exp_stat: '0',
            },
            {
                ip_prefix: '189.90.96.0/12',
                ASN: '28634',
                exp_stat: '0',
            },
            {
                ip_prefix: '189.124.88.0/24',
                ASN: '28287',
                exp_stat: '0',
            },
            {
                ip_prefix: '189.125.59.128/24',
                ASN: '3549',
                exp_stat: '0',
            },
            {
                ip_prefix: '189.125.204.0/24',
                ASN: '262357',
                exp_stat: '0',
            },
        ];

        for (let i = 0; i < prefixs.length; i++) {
            var prefKey = prefixs[i].ip_prefix;
            prefixs[i].docType = 'prefix';
            await ctx.stub.putState(prefKey, Buffer.from(JSON.stringify(prefixs[i])));
            console.info('Added <--> ', prefixs[i]);
        }
        console.info('============= END : Initialize Ledger ===========');
    }

    async querybyKey(ctx, prefKey) {
        const prefAsBytes = await ctx.stub.getState(prefKey); // get the ip prefix from chaincode state
        if (!prefAsBytes || prefAsBytes.length === 0) {
            throw new Error(`${prefKey} does not exist`);
        }
        console.log(prefAsBytes.toString());
        return prefAsBytes.toString();
    }
    // async querybyParam(ctx, prefix,ASN,exp_stat) {
    //     const prefAsBytes = await ctx.stub.getState(prefix,ASN,exp_stat); 
    //     if (!prefAsBytes || prefAsBytes.length === 0) {
    //         throw new Error(`${prefix} does not exist`);
    //     }
    //     console.log(prefAsBytes.toString());
    //     return prefAsBytes.toString();
    // }

    async createbsbri(ctx, prefKey, ip_prefix, ASN,exp_stat) {
        console.info('============= START : Create IP Prefix ===========');

        const pref = {
            docType: 'prefix',
            ip_prefix,
            ASN,
            exp_stat,
        };

        await ctx.stub.putState(prefKey, Buffer.from(JSON.stringify(pref)));
        console.info('============= END : Create IP Prefix ===========');
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
