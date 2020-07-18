/*
 * SPDX-License-Identifier: Apache-2.0
 */

// This file is use to query a certain prefix from the blockchain using prefix
// an argument of prefix needed when calling this function
// ex: node queryPref.js 2.2.2.2/24
 'use strict';

const { Gateway, Wallets } = require('fabric-network');
const path = require('path');
const fs = require('fs');
var prefkey = process.argv.slice(2);

async function main() {
    try {
        console.log(`your pref key is : ${prefkey}`)
        // load the network configuration
        //connection using organization 1 credential
        const ccpPath = path.resolve(__dirname, '..', '..', 'test-network', 'organizations', 'peerOrganizations', 'org1.example.com', 'connection-org1.json');
        const ccp = JSON.parse(fs.readFileSync(ccpPath, 'utf8'));

        // Create a new file system based wallet for managing identities.
        const walletPath = path.join(process.cwd(), 'wallet');
        const wallet = await Wallets.newFileSystemWallet(walletPath);
        console.log(`Wallet path: ${walletPath}`);

        // Check to see if we've already enrolled the router1.
        const identity = await wallet.get('router1');
        if (!identity) {
            console.log('An identity for the "router1" does not exist in the wallet');
            console.log('Run the registerRouter.js application before retrying');
            return;
        }

        // Create a new gateway for connecting to our peer node.
        const gateway = new Gateway();
        await gateway.connect(ccp, { wallet, identity: 'router1', discovery: { enabled: true, asLocalhost: true } });

        // Get the network (channel) our contract is deployed to.
        const network = await gateway.getNetwork('mychannel');

        // Get the contract from the network.
        const contract = network.getContract('bsbri');

        // Evaluate the specified transaction.
        // sending parameter to get a prefix
        const result = await contract.evaluateTransaction('querybyKey',prefkey);
        console.log(`Transaction has been evaluated, result is: ${result.toString()}`);

    } catch (error) {
        console.error(`Failed to evaluate transaction: ${error}`);
        process.exit(1);
    }
}

main();
