import requests
import json
import timeit

def sendPrefixRequest(pref,asN):
    url = 'http://localhost:8080/api/querypref'
    headers = {'content-type': 'application/json',
        'accept-encoding': 'application/json',
        'charsets': 'utf-8'}
    payload = {'ip_prefix':pref,'ASN':asN,'exp_stat':'0'}
    response = requests.post(url=url,headers=headers,data=json.dumps(payload))
    print(response)

# Searching for ASN number from shell schript

# sourceAS = open("/etc/quagga/ASN.txt", "r")
# asNumber = sourceAS.read().replace("\n","")

startTime = timeit.default_timer()
with open ("verif.txt") as myfile:
    for line in myfile:
        prefix,path = map(str.strip,line.split(';'))
        if path != "i":
            word = path.split(" ")
            asNumber = word[0]
            print(asNumber)
            sendPrefixRequest(prefix,asNumber)
            stopTime = timeit.default_timer()
            exeTime = str(stopTime-startTime)
            with open ("verifTime.txt","a") as sendingTime:
                sendingTime.write(exeTime + '\n')        
        
