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
    print(stat)
    # url_set = url+'/api/addpref'
    # headers = {'content-type': 'application/json',
    #     'accept-encoding': 'application/json',
    #     'charsets': 'utf-8'}
    # payload = {'ip_prefix':pref,'ASN':asn,'exp_stat':stat}
    # response = requests.post(url=url_set,headers=headers,data=json.dumps(payload))
    # print(response)

def file_compare():
    try:      
        print(dirname+'/buffer_file.txt')
        buffer_file = dirname+'/buffer_file.txt'
        local_file = dirname+'/local_file.txt'      

        # getting the line size        
        bf = open(buffer_file,"r")
        lc = open(local_file,"r")
        size_buf = sum([1 for i in bf.readlines() if i.strip()])
        size_loc = sum([1 for i in lc.readlines() if i.strip()])

        # compare and find the index file
        if size_buf <= size_loc:
            with open (buffer_file,"r") as buff:
                with open (local_file,"r") as loc:
                    diff = list(set(loc).difference(buff))           
            print('withdraw')
            print(diff)
            for line in diff:
                prefix = line.rstrip("\n")
                sendPrefixRequest(prefix,'0')
        else:
            with open (buffer_file,"r") as buff:
                with open (local_file,"r") as loc:
                    diff = list(set(buff).difference(loc))           
            print('advert')
            print(diff)
            for line in diff:
                prefix = line.rstrip("\n")
                sendPrefixRequest(prefix,'1')
    except Exception as error:
        print(error)
    
global url,asn,router_id

url = ''
asn = ''
dirname = os.getcwd()
file_compare()

        
