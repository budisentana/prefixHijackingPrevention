/*
 * SPDX-License-Identifier: Apache-2.0
 */

// this file is use to manually invoke a prefix to the blockchain
// credential used are organization 1

 'use strict';

const { Gateway, Wallets } = require('fabric-network');
const fs = require('fs');
const path = require('path');

async function main() {
    try {
        // load the network configuration
        const ccpPath = path.resolve(__dirname, '..', '..', 'test-network', 'organizations', 'peerOrganizations', 'org1.example.com', 'connection-org1.json');
        let ccp = JSON.parse(fs.readFileSync(ccpPath, 'utf8'));

        // Create a new file system based wallet for managing identities.
        const walletPath = path.join(process.cwd(), 'wallet');
        const wallet = await Wallets.newFileSystemWallet(walletPath);
        console.log(`Wallet path: ${walletPath}`);

        // Check to see if we've already enrolled the router.
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

        // Submit the specified transaction.
        // createCar transaction - requires 4 argument -->function_name, prefix,ASN, active status, 
        // ex: ('createbsbri', '23.23.23.0/24', '123', '1')
        await contract.submitTransaction('createbsbri', '23.23.23.0/24','23.23.23.0/24', '123', '1');
        console.log('Transaction has been submitted');

        // Disconnect from the gateway.
        await gateway.disconnect();

    } catch (error) {
        console.error(`Failed to submit transaction: ${error}`);
        process.exit(1);
    }
}

main();
