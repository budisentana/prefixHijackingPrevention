import requests
import json
import timeit
import os
from pathlib import Path

def check_config():
    try:
        global url,asn,router_ip,bgp_port,password      
        with open(dirname + "/config.json","r") as json_conf:
            jc = json.load(json_conf)
            url = jc["server"]
            asn = jc["asn"]
            router_ip = jc["router_ip"]
            password = jc["password"]
            bgp_port = jc["bgp_port"]

    except Exception as error:
        print(error)

def verify_prefix(pref,path):
    print(str(pref) + ' is verified to '+ str(path))

    url_set = url+'/api/querypref'
    headers = {'content-type': 'application/json',
        'accept-encoding': 'application/json',
        'charsets': 'utf-8'}
    payload = {'ip_prefix':pref,'ASN':path}
    response = requests.post(url=url_set,headers=headers,data=json.dumps(payload))
    print(response.status_code)
    if response.status_code in [205]:
        return False
    else:
        return True

def compare_rov(buffer_rov):
    try:      
        check_config()
        local_file = dirname+'/local_rov.txt'      
        buff=[]
        loc =[]
        hijacker=[]
        for x in buffer_rov:
            buff.append(x.rstrip("\n"))
        # print('this is buff'+str(buff))

        with open (local_file,"r") as local:
            for y in local:
                loc.append(y.rstrip("\n"))

        diff = set(buff).difference(loc)           
        # print('this is second different'+str(diff))
        for line in diff:
            global hop
            prefix,hop,path = map(str.strip,line.split(';'))
            t_appear = timeit.default_timer()
            pref_status = verify_prefix(prefix,path) # verify prefix send to blockchain
            print(str(pref_status))
            if pref_status is False:
                t_identified = timeit.default_timer()
                send_filter(prefix,hop,path)
                t_neutralized = timeit.default_timer()
                # write_to_time(t_appear,t_identified,t_neutralized)
                write_record(prefix,path,t_appear,t_identified)
                hijacker.append(prefix+';'+hop +';'+path) # catch the hijacker

        # check_filter(hijacker) #check filter availibility
       
        temp_loc = open(local_file,"w")      
        for line in buff : 
            if line.rstrip("\n") not in hijacker:
                temp_loc.write(line+"\n")

    except Exception as error:
        print(error)

def write_record(prefix,path,prepend,identified):
    two_up = Path().absolute().parent.parent.parent
    keeper = two_up /'multiple/time_note.txt'
    with open(keeper,'a') as note_time:
        note_time.write(str(path)+';'+prefix+';P;'+str(prepend)+'\n')
        note_time.write(str(path)+';'+prefix+';N;'+str(identified)+'\n')


def send_filter(prefix,hop,path):
    print('Prefix '+prefix+' Hijacked by '+str(path))
    print('Sending Filter for ' +str(path))
    filter_command = dirname+'/filter.sh'
    print (router_ip+bgp_port+password+hop+path+asn)
    os.system (filter_command + router_ip + bgp_port + password + hop +' '+ path + asn)
    print('Neutralize Hijacking '+str(path))

# def remove_filter(dif):
#     print('remove filter for '+str(dif))

 
url = ''
asn = ''
bgp_port = ''
password = ''
router_ip = ''
hop = ''
dirname = os.getcwd()

# def write_to_time(t_appear, t_identified, t_neutralized):

#     two_up = Path().absolute().parent.parent.parent
#     keeper = two_up /'BRP/time_keeper.txt'
#     global last_line
#     last_line = ''
#     t_prepend = ''
#     with open (keeper,'r') as keeper_file:
#         for num,last_line in enumerate(keeper_file):
#             pass           
#         line_p = [num-9]
#         line_a = [num-7]
#         line_n = [num-3]

#     if '>>' in last_line:
#         print('test')
#         t_prepend = float(last_line.lstrip(">>").rstrip("\n"))
#     else:
#         with open(keeper) as keeper_file :
#             for nums, line in enumerate(keeper_file):
#                 if nums in line_p :
#                     prepend_time = line
#                     old_prepend = float(prepend_time.lstrip(">>").rstrip("\n"))
#                 if nums in line_n :
#                     neutral_time = line
#                     old_neutral = float(neutral_time.lstrip("**>").rstrip("\n"))
#                 if nums in line_a :
#                     appear_time = line
#                     old_appear = float(appear_time.lstrip(">").rstrip("\n"))
#             t_prepend = old_prepend + old_neutral+old_appear
#         with open(keeper,'a') as keeper_file :
#             keeper_file.write('This is next attack from '+str(hop)+'\n'+str(t_prepend)+'\n')

    
#     print(t_prepend)
#     prepend_to_appear = t_appear - t_prepend
#     identification_time = t_identified - t_appear
#     neutralized_from_identified = t_neutralized - t_identified
#     neutralized_from_appear = t_neutralized - t_appear

#     with open(keeper,'a') as keeper_file:
#         keeper_file.write('This is : [prepend --> appear ] time  from '+str(hop)+'\n'+ '>'+ str(prepend_to_appear)+'\n')
#         keeper_file.write('This is : [appear --> identified]  as hijacker from '+str(hop)+'\n'+ '*>'+ str(identification_time)+'\n')
#         keeper_file.write('This is : [appear --> neutralized] time  from '+str(hop)+'\n'+ '**>'+ str(neutralized_from_appear)+'\n')
#         keeper_file.write('This is : [identified --> neutralized] time  from '+str(hop)+'\n'+ '***>'+ str(neutralized_from_identified)+'\n')
#         keeper_file.write('-----------------------------------------------------------\n')



# def check_filter(hijacker):
#     # sending filte if hijacker found
#     # print('this is hijacker :'+str(hijacker))
#     filter_list = dirname+'/filter_list.txt'
#     filter_data=[]
#     # got the content of filter list
#     with open(filter_list,"r") as myfile:
#         for line in myfile:
#             filter_data.append(line.rstrip("\n"))
#     # print('this is filter list '+str(filter_data))
#     dif = list(set(hijacker).difference(filter_data)) #find a new hijacker
#     for line in dif:
#         send_filter(line)
#     # dif = list(set(filter_data).difference(hijacker)) # remove old hijacker
#     # for line in dif:
#     #     remove_filter(line)

#     temp_filter = open(filter_list,"w")      
#     for line in hijacker:
#         temp_filter.write(line+"\n")



