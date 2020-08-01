import requests
import json
import timeit
import os

# def check_config():
#     try:
#         with open(dirname + "/config.json","r") as json_conf:
#             jc = json.load(json_conf)
#             url = jc["url"]
#             asn = jc["asn"]
#             router_id = jc["router_id"]
#     except Exception as error:
#         print(error)

def verify_prefix(pref,path):
    print(str(pref) + ' is verified with '+ str(path))
    return True


    # url = 'http://localhost:8091/api/querypref'
    # headers = {'content-type': 'application/json',
    #     'accept-encoding': 'application/json',
    #     'charsets': 'utf-8'}
    # payload = {'ip_prefix':pref,'ASN':asn,'exp_stat':stat}
    # response = requests.post(url=url_set,headers=headers,data=json.dumps(payload))
    # print(response)

def file_compare():
    try:      
        print(dirname+'/buffer_rov.txt')
        buffer_file = dirname+'/buffer_rov.txt'
        local_file = dirname+'/local_rov.txt'      

        # find difference buffer - local
        hijacker=[]
        with open (buffer_file,"r") as buff:
            with open (local_file,"r") as loc:
                diff = list(set(buff).difference(loc))           
        for line in diff:
            prefix,path = map(str.strip,line.split(';'))
            pref_status = verify_prefix(prefix,path) # verify prefix send to blockchain
            if pref_status is False:
                hijacker.append(prefix+';'+path) # catch the hijacker
        check_filter(hijacker) #check filter availibility
        
        temp_loc = open(local_file,"w")      
        with open(buffer_file,"r") as buff : #write to local table
            for line in buff : 
                if line.rstrip("\n") not in hijacker:
                    temp_loc.write(line)
    except Exception as error:
        print(error)

def check_filter(hijacker):
    # sending filte if hijacker found
    print('this is hijacker :'+str(hijacker))
    filter_list = dirname+'/filter_list.txt'
    filter_data=[]
    # got the content of filter list
    with open(filter_list,"r") as myfile:
        for line in myfile:
            filter_data.append(line.rstrip("\n"))
    print('this is filter list '+str(filter_data))
    dif = list(set(hijacker).difference(filter_data)) #find a new hijacker
    for line in dif:
        send_filter(line)
    dif = list(set(filter_data).difference(hijacker)) # remove old hijacker
    for line in dif:
        remove_filter(line)

    temp_filter = open(filter_list,"w")      
    for line in hijacker:
        temp_filter.write(line+"\n")


def send_filter(dif):
    print('send filter for '+str(dif))

def remove_filter(dif):
    print('remove filter for '+str(dif))


global url,asn,router_id
  
url = ''
asn = ''
dirname = os.getcwd()
file_compare()