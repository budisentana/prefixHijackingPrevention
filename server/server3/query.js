/*
 * SPDX-License-Identifier: Apache-2.0
 */

// This file is used to query all prefix in the blockchain
// this query using credential of user in organization 1
 'use strict';

const { Gateway, Wallets } = require('fabric-network');
const path = require('path');
const fs = require('fs');


async function main() {
    try {
        // load the network configuration
        // using credential of organization 1
        const ccpPath = path.resolve(__dirname, '..', '..', 'test-network', 'organizations', 'peerOrganizations', 'org2.example.com', 'connection-org2.json');
        const ccp = JSON.parse(fs.readFileSync(ccpPath, 'utf8'));

        // Create a new file system based wallet for managing identities.
        const walletPath = path.join(process.cwd(), 'wallet');
        const wallet = await Wallets.newFileSystemWallet(walletPath);
        console.log(`Wallet path: ${walletPath}`);

        // Check to see if we've already enrolled the router credential.
        const identity = await wallet.get('router3');
        if (!identity) {
            console.log('An identity for the  "router3" does not exist in the wallet');
            console.log('Run the registerRouter.js application before retrying');
            return;
        }

        // Create a new gateway for connecting to our peer node.
        const gateway = new Gateway();
        await gateway.connect(ccp, { wallet, identity: 'router3', discovery: { enabled: true, asLocalhost: true } });

        // Get the network (channel) our contract is deployed to.
        const network = await gateway.getNetwork('mychannel');

        // Get the contract from the network.
        const contract = network.getContract('bsbri');

        // Evaluate the specified transaction.
        // query all prefix transaction - required argument, startkey and endkey
        // ex: ('queryAllbsbri', '0.0.0.0/0'.'999.999.999.999/32')
        const result = await contract.evaluateTransaction('queryAllbsbri','0.0.0.0/0','999.999.999.999/32');
        console.log(`Transaction has been evaluated, result is: ${result.toString()}`);
    
    } catch (error) {
        console.error(`Failed to evaluate transaction: ${error}`);
        process.exit(1);
    }
}

main();
