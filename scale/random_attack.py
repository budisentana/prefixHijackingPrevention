import os 
import random
import time
import timeit

""" setup number of attack"""
attack_num = 5

print('Find The prefix list')
dirname = os.getcwd()
prefix_list = dirname+'/prefix_list.txt'
print(prefix_list)
prefix_dict=[]
host_asn_dict=[]
# original_list=[]
with open(prefix_list,'r') as prefix_file:
    for line in prefix_file:
        host,asn,prefix = map(str.strip,line.split(';'))
        prefix_dict.append(prefix)
        print(prefix)
#         host_asn_dict.append(host+';'+asn)
#         original_list.append(line.strip('\n'))
# # print(original_list)

"""Find the router list"""
router_list = dirname+'/node_setup.txt'
host_asn_dict = []
with open (router_list,'r') as router_file:
    for line in router_file:
        host_name,host_ip,router,asn = map(str.strip,line.split(';'))
        asn_x = asn.strip('AS')
        host_asn_dict.append(host_ip+';'+asn_x)


"""Create fake list by combinining existing prefix and ASN"""

print('Create random attacker')
fake_list=[]

if len(prefix_dict) < attack_num:
    attack_num = len(prefix_dict)
    print ('Number of attack less than prefix number')

while len(fake_list)<attack_num:
    random_host = random.choice(host_asn_dict)
    random_prefix = random.choice(prefix_dict)
    attacker = random_host+';'+random_prefix
    if attacker not in prefix_list and attacker not in fake_list:
        fake_list.append(attacker)

attacker_list = dirname+'/attacker_list.txt'
with open(attacker_list,'w') as attacker_list:
    for item in fake_list:
        attacker_list.write(item+'\n')
# print(fake_list)

"""Send the false prefix origin to the network""" 
print('Sleep 5 second before announce FALSE IP Prefix  by ATTACKER')
time.sleep(5)
time_list=[]
for item in fake_list:
    host,asn,prefix = map(str.strip,item.split(';'))
    
    print('ATTACK SEND TO PREFIX '+prefix+ ' by ASN  '+asn)
    shell_path = os.getcwd()+'/prefix_announcement.sh'
    os.system(shell_path + ' '+ host +' '+asn + ' '+prefix)
    # start_time = time.time()
    start_time = timeit.default_timer()
    time_list.append(host+';'+asn+';'+prefix+';S;'+str(start_time))


"""Write the time attack record to the file"""
time_note = dirname+'/time_note.txt'
with open(time_note,'w') as time_file:
    for line in time_list:
        time_file.write(line+'\n')
        print(line)
    time_file.write('-----\n')