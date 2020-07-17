
var express = require('express');
var bodyParser = require('body-parser');

var app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Setting for Hyperledger Fabric
const { Gateway, Wallets } = require('fabric-network');
const path = require('path');
const fs = require('fs');
const ccpPath = path.resolve(__dirname, '..', '..', 'test-network', 'organizations', 'peerOrganizations', 'org2.example.com', 'connection-org2.json');


app.post('/api/queryAllPref', async function (req, res) {
    try {
        const ccp = JSON.parse(fs.readFileSync(ccpPath, 'utf8'));

        // Create a new file system based wallet for managing identities.
        const walletPath = path.join(process.cwd(), 'wallet');
        const wallet = await Wallets.newFileSystemWallet(walletPath);
        console.log(`Wallet path: ${walletPath}`);

        // Check to see if we've already enrolled the user.
        const identity = await wallet.get('appUser');
        if (!identity) {
            console.log('An identity for the user "appUser" does not exist in the wallet');
            console.log('Run the registerUser.js application before retrying');
            return;
        }

        // Create a new gateway for connecting to our peer node.
        const gateway = new Gateway();
        await gateway.connect(ccp, { wallet, identity: 'appUser', discovery: { enabled: true, asLocalhost: true } });

        // Get the network (channel) our contract is deployed to.
        const network = await gateway.getNetwork('mychannel');

        // Get the contract from the network.
        const contract = network.getContract('bsbri');

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
        process.exit(1);
    }
});


app.post('/api/querypref/', async function (req, res) {
    try {

        const ccp = JSON.parse(fs.readFileSync(ccpPath, 'utf8'));
        
        // Create a new file system based wallet for managing identities.
        const walletPath = path.join(process.cwd(), 'wallet');
        const wallet = await Wallets.newFileSystemWallet(walletPath);
        console.log(`Wallet path: ${walletPath}`);

        // Check to see if we've already enrolled the user.
        const identity = await wallet.get('appUser');
        if (!identity) {
            console.log('An identity for the user "appUser" does not exist in the wallet');
            console.log('Run the registerUser.js application before retrying');
            return;
        }

        // Create a new gateway for connecting to our peer node.
        const gateway = new Gateway();
        await gateway.connect(ccp, { wallet, identity: 'appUser', discovery: { enabled: true, asLocalhost: true } });

        // Get the network (channel) our contract is deployed to.
        const network = await gateway.getNetwork('mychannel');

        // Get the contract from the network.
        const contract = network.getContract('bsbri');

        // Evaluate the specified transaction.
        // query transaction - requires 1 argument, ex: ('querybKey', '192.168.3.6/24')
        var prefKey = req.body.ip_prefix;
        var ASN = req.body.ASN;
        console.log(req.body);
        console.log(prefKey);
        var resStatus = "invalid";
        const result = await contract.evaluateTransaction('querybyKey',prefKey);

        var prefixJson={};      
        prefixJson = JSON.parse(result.toString());
        if (prefixJson.ip_prefix==prefKey && prefixJson.ASN==ASN && prefixJson.exp_stat=='0'){
            resStatus = "valid"; 
                       
        }        
        console.log(result.toString);
        res.status(200).json(resStatus.toString());

    } catch (error) {
        console.error(`Failed to evaluate transaction: ${error}`);
        res.status(500).json({error: error});
        // process.exit(1);
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
        const identity = await wallet.get('appUser');
        if (!identity) {
            console.log('An identity for the user "appUser" does not exist in the wallet');
            console.log('Run the registerUser.js application before retrying');
            return;
        }

        // Create a new gateway for connecting to our peer node.
        const gateway = new Gateway();
        await gateway.connect(ccp, { wallet, identity: 'appUser', discovery: { enabled: true, asLocalhost: true } });

        // Get the network (channel) our contract is deployed to.
        const network = await gateway.getNetwork('mychannel');

        // Get the contract from the network.
        const contract = network.getContract('bsbri');

        // Submit the specified transaction.
        // createPref transaction - requires 4 argument,
        //await contract.submitTransaction('createPref', req.body.prefNumber, req.body.ip_prefix, req.body.prefix_length, req.body.company, req.body.ASN);
        await contract.submitTransaction('createbsbri', req.body.ip_prefix, req.body.ip_prefix, req.body.ASN, req.body.exp_stat);
        // console.log('this is headers :',req.headers);
        console.log(req.body,'Has been added to blockchain');
        resStatus=(req.body,' has been submitted');
        res.status(200).json(resStatus.toString());

        // Disconnect from the gateway.
        await gateway.disconnect();

    } catch (error) {
        console.error(`Failed to submit transaction: ${error}`);
        process.exit(1);
    }
})


app.listen(8080);
