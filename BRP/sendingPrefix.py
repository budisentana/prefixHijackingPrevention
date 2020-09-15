import requests
import json
import timeit
import os

def check_config():
    try:
        with open(dirname + "/config.json","r") as json_conf:
            jc = json.load(json_conf)
            url = jc["url"]
            asn = jc["asn"]
            router_id = jc["router_id"]
    except Exception as error:
        print(error)

def sendPrefixRequest(pref,stat):
    print(pref)
    if stat in ['1']:
        print('advert')
    else:
        print('withdraw')
    # url_set = url+'/api/addpref'
    # headers = {'content-type': 'application/json',
    #     'accept-encoding': 'application/json',
    #     'charsets': 'utf-8'}
    # payload = {'ip_prefix':pref,'ASN':asn,'exp_stat':stat}
    # response = requests.post(url=url_set,headers=headers,data=json.dumps(payload))
    # print(response)

def compare_roa(buffer_roa):
    try:      
        local_file = dirname+'/local_roa.txt'      
        buff=[]
        loc =[]
        for x in buffer_roa:
            buff.append(x.rstrip("\n"))
        # print('this is buff'+str(buff))

        with open (local_file,"r") as local:
            for y in local:
                loc.append(y.rstrip("\n"))

        diff = set(loc).difference(buff)           
        # print('this is different'+str(diff))
        for line in diff:
            prefix = line.rstrip("\n")
            sendPrefixRequest(prefix,'0')

        diff = set(buff).difference(loc)           
        # print('this is second different'+str(diff))
        for line in diff:
            prefix = line.rstrip("\n")
            sendPrefixRequest(prefix,'1')

        # update the local table
        temp_loc = open(local_file,"w")
        for line in buffer_roa:
            temp_loc.write(line+"\n")

    except Exception as error:
        print(error)
    
global url,asn,router_id

url = ''
asn = ''
dirname = os.getcwd()
# file_compare()

        
