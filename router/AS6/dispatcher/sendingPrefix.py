import requests
import json
import timeit
import os

def check_config():
    try:
        global url,asn
        with open(dirname + "/config.json","r") as json_conf:
            jc = json.load(json_conf)
            url = jc["server"]
            asn = jc["asn"]
    except Exception as error:
        print(error)

def sendPrefixRequest(pref,stat):
    if stat in ['1']:
        print('advertising Prefix '+str(pref))
    else:
        print('withdraw Prefix '+str(pref))

    url_set = url+'/api/addpref'
    headers = {'content-type': 'application/json',
        'accept-encoding': 'application/json',
        'charsets': 'utf-8'}
    payload = {'ip_prefix':pref,'ASN':asn,'exp_stat':stat}

    response = requests.post(url=url_set,headers=headers,data=json.dumps(payload))
    # print(response.status_code)
    # add response status before write to local table

def compare_roa(buffer_roa):
    try:      
        check_config()
        local_file = dirname+'/local_roa.txt'      
        buff=[]
        loc =[]
        for x in buffer_roa:
            buff.append(x.rstrip("\n"))
        # print('this is buff'+str(buff))

        with open (local_file,"r") as local:
            for y in local:
                loc.append(y.rstrip("\n"))

        diff = set(buff).difference(loc)           
        # print('this is second different buffer'+str(diff))
        for line in diff:
            prefix = line.rstrip("\n")
            sendPrefixRequest(prefix,'1')

        diff = set(loc).difference(buff)           
        # print('this is different local'+str(diff))
        for line in diff:
            prefix = line.rstrip("\n")
            sendPrefixRequest(prefix,'0')

        # update the local tabless
        temp_loc = open(local_file,"w")
        for line in buffer_roa:
            temp_loc.write(line+"\n")

    except Exception as error:
        print(error)
    

url = ''
asn = ''
dirname = os.getcwd()

        
