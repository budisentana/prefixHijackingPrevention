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

def file_compare():
    try:      
        print(dirname+'/buffer_roa.txt')
        buffer_file = dirname+'/buffer_roa.txt'
        local_file = dirname+'/local_roa.txt'      

        with open (buffer_file,"r") as buff:
            with open (local_file,"r") as loc:
                diff = list(set(loc).difference(buff))           
        for line in diff:
            prefix = line.rstrip("\n")
            sendPrefixRequest(prefix,'0')

        with open (buffer_file,"r") as buff:
            with open (local_file,"r") as loc:
                diff = list(set(buff).difference(loc))           
        for line in diff:
            prefix = line.rstrip("\n")
            sendPrefixRequest(prefix,'1')


        # getting the line size        
        # bf = open(buffer_file,"r")
        # lc = open(local_file,"r")
        # size_buf = sum([1 for i in bf.readlines() if i.strip()])
        # size_loc = sum([1 for i in lc.readlines() if i.strip()])

        # compare and find the index file
        # if size_buf <= size_loc:
        #     # if buffer size smaller than local size then withdraw prefix
        #     with open (buffer_file,"r") as buff:
        #         with open (local_file,"r") as loc:
        #             diff = list(set(loc).difference(buff))           
        #     for line in diff:
        #         prefix = line.rstrip("\n")
        #         sendPrefixRequest(prefix,'0')
        # else:
        #     # if buffer size bigger than local size than advert prefix
        #     with open (buffer_file,"r") as buff:
        #         with open (local_file,"r") as loc:
        #             diff = list(set(buff).difference(loc))           
        #     for line in diff:
        #         prefix = line.rstrip("\n")
        #         sendPrefixRequest(prefix,'1')
        
        # update the local table
        temp_loc = open(local_file,"w")
        with open(buffer_file,"r") as buff :
            for line in buff:
                temp_loc.write(line)

    except Exception as error:
        print(error)
    
global url,asn,router_id

url = ''
asn = ''
dirname = os.getcwd()
file_compare()

        
