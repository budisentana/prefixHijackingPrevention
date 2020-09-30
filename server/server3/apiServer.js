
// This file is use to received http request from router dispatcher
// if there is new prefix announcement or withdrawal

var express = require('express');
var bodyParser = require('body-parser');

var app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Setting for Hyperledger Fabric
// using organization 1 credential
const { Gateway, Wallets } = require('fabric-network');
const path = require('path');
const fs = require('fs');
const { json } = require('body-parser');
const ccpPath = path.resolve(__dirname, '..', '..', 'test-network', 'organizations', 'peerOrganizations', 'org2.example.com', 'connection-org2.json');
const accRouter = 'router3'; //router id
const smartCon = 'bsbri'; //smart contract to use
const opChanel = 'mychannel'; //channel to use

app.post('/api/queryAllPref', async function (req, res) {
    try {
        const ccp = JSON.parse(fs.readFileSync(ccpPath, 'utf8'));

        // Create a new file system based wallet for managing identities.
        const walletPath = path.join(process.cwd(), 'wallet');
        const wallet = await Wallets.newFileSystemWallet(walletPath);
        console.log(`Wallet path: ${walletPath}`);

        // Check to see if we've already enrolled the router.
        const identity = await wallet.get(accRouter);
        if (!identity) {
            console.log('An identity for the  "accRouter" does not exist in the wallet');
            console.log('Run the registerRouter.js application before retrying');
            return;
        }

        // Create a new gateway for connecting to our peer node.
        const gateway = new Gateway();
        await gateway.connect(ccp, { wallet, identity: accRouter, discovery: { enabled: true, asLocalhost: true } });

        // Get the network (channel) our contract is deployed to.
        const network = await gateway.getNetwork(opChanel);

        // Get the contract from the network.
        const contract = network.getContract(smartCon);

        // Evaluate the specified transaction.
        // queryAllPrefix transaction - requires arguments start key and end key
        var startKey = req.body.startKey;
        var endKey = req.body.endKey;
        const result = await contract.evaluateTransaction('queryAllbsbri',startKey,endKey);
        console.log(`Transaction has been evaluated, result is: ${result.toString()}`);
        res.status(200).json({response: result.toString()});

    } catch (error) {
        console.error(`Failed to evaluate transaction: ${error}`);
        res.status(500).json({error: error});
    }
});

//use to handle single prefix request
app.post('/api/querypref/', async function (req, res) {
    try {
        const ccp = JSON.parse(fs.readFileSync(ccpPath, 'utf8'));      
        // Create a new file system based wallet for managing identities.
        const walletPath = path.join(process.cwd(), 'wallet');
        const wallet = await Wallets.newFileSystemWallet(walletPath);
        console.log(`Wallet path: ${walletPath}`);

        // Check to see if we've already enrolled the user.
        const identity = await wallet.get(accRouter);
        if (!identity) {
            console.log('An identity for the user "accRouter" does not exist in the wallet');
            console.log('Run the registerRouter.js application before retrying');
            return;
        }

        // Create a new gateway for connecting to our peer node.
        const gateway = new Gateway();
        await gateway.connect(ccp, { wallet, identity: accRouter, discovery: { enabled: true, asLocalhost: true } });

        // Get the network (channel) our contract is deployed to.
        const network = await gateway.getNetwork(opChanel);

        // Get the contract from the network.
        const contract = network.getContract(smartCon);

        // Evaluate the specified transaction.
        // query transaction - requires 1 argument, ex: ('querybKey', '192.168.3.6/24')
        var prefKey = req.body.ip_prefix;
        console.log(req.body);
        const result = await contract.evaluateTransaction('querybyKey',prefKey);
        new_res = JSON.parse(result)
        console.log(new_res.ASN)
        if(req.body.ASN===new_res.ASN){
            res.status(200).json({result});
            console.info('valid prefix');
        }
        else{
            res.status(205).json({result});
            console.info('invalid prefix');
        }
    } catch (error) {
        console.error(`Failed to evaluate transaction`);
        res.status(500).json({error: error});
    }
});

app.post('/api/addpref/', async function (req, res) {
    try {
        let ccp = JSON.parse(fs.readFileSync(ccpPath, 'utf8'));
        // Create a new file system based wallet for managing identities.
        const walletPath = path.join(process.cwd(), 'wallet');
        const wallet = await Wallets.newFileSystemWallet(walletPath);
        console.log(`Wallet path: ${walletPath}`);

        // Check to see if we've already enrolled the user.
        const identity = await wallet.get(accRouter);
        if (!identity) {
            console.log('An identity for the router does not exist in the wallet');
            console.log('Run the registerRouter.js application before retrying');
            return;
        }

        // Create a new gateway for connecting to our peer node.
        const gateway = new Gateway();
        await gateway.connect(ccp, { wallet, identity: accRouter, discovery: { enabled: true, asLocalhost: true } });

        // Get the network (channel) our contract is deployed to.
        const network = await gateway.getNetwork(opChanel);

        // Get the contract from the network.
        const contract = network.getContract(smartCon);

        // Submit the specified transaction.
        // createPref transaction - requires 4 argument,
        //await contract.submitTransaction('createPref', req.body.prefNumber, req.body.ip_prefix, req.body.prefix_length, req.body.company, req.body.ASN);
        const resStatus = await contract.submitTransaction('createbsbri', req.body.ip_prefix, req.body.ip_prefix, req.body.ASN, req.body.exp_stat);
        console.log(resStatus.toString());
        res.status(200).json({resStatus});

        // Disconnect from the gateway.
        await gateway.disconnect();

    } catch (error) {
        console.error(`Failed to submit transaction`);
        res.status(500).json({error});
    }
});

app.listen(8093);
