import plotly.graph_objects as go
import networkx as nx
import random
import os
import time

print('Creating Docker container Network ')
docker_net = 'docker network create --subnet=99.0.0.0/8 blockjack-bgp-net'
print(str(docker_net))
os.system(docker_net)

with open('node_setup.txt','r') as node_conf:
    for node in node_conf:
        host_name,host_ip,router_name,as_name = map(str.strip,node.split(';'))

        print(host_name,host_ip,router_name,as_name)
        print('Creating Directory of '+as_name )
        mk_dir = 'mkdir '+as_name
        os.system(mk_dir)
        print('Copying quagga configuration file to '+as_name)
        cp_conf = 'cp quagga.conf `pwd`/'+as_name+'/quagga.conf'
        os.system(cp_conf)

        print('Run '+router_name+ ' on Docker Container in Detach mode')
        print('Assigning IP Address ' +host_ip + ' to the Router')
        print('Attaching router to the network')
        docker_run = 'docker run --name '+ router_name+' --net blockjack-bgp-net --ip '+ host_ip+' --hostname='+host_name+' -d -v `pwd`/'+as_name+':/etc/quagga:rw pierky/quagga'
        print(docker_run)
        os.system(docker_run)

print('Sleep 5 second before configure router')
time.sleep(5)

router_list=[]
with open('node_setup.txt','r') as node_conf:
    for node in node_conf:
        host_name,host_ip,router_name,as_name = map(str.strip,node.split(';'))
        print('Configure routername, BGP ASN, BGP ID for '+str(router_name))
        as_no = as_name.lstrip('AS').rstrip('\n')
        print(as_no)
        shell_path = os.getcwd()+'/conf_node.sh '
        os.system(shell_path + host_ip + ' '+router_name+ ' '+as_no)
        router_list.append(host_ip+';'+as_no)

print('Sleep 5 second before configure BGP Peer')
time.sleep(5)
with open('peer_setup.txt','r') as peer_conf:
    for peer in peer_conf:
        peer_x, ip_x, peer_y, ip_y = map(str.strip,peer.split(';'))

        print('Peering AS '+peer_x+ ' with AS  '+peer_y)
        shell_path = os.getcwd()+'/peer_conf.sh'
        os.system(shell_path + ' '+ ip_x +' '+peer_x + ' '+ip_y+  ' '+peer_y)
        print('Peering AS '+peer_y+ ' with AS  '+peer_x)
        os.system(shell_path + ' '+ ip_y + ' '+peer_y + ' '+ip_x+ ' '+peer_x)

print('Sleep 5 second Creating Random IP Prefix to announce by router')
time.sleep(5)

number_of_prefix = round(len(router_list)/4)
prefix_list =[]
print('Creating random IP Prefix to announce by router')
while len(prefix_list) < number_of_prefix:
    x1 = random.randint(0,255)
    x2 = random.randint(0,255)
    x3 = random.randint(0,255)        
    x4 = 0
    result = ".".join(map(str,([x1,x2,x3,x4])))
    if result not in prefix_list:    
        prefix_list.append(result+'/24')

print('Writing the IP Prefix and owner to the file ')
with open('prefix_list.txt','w') as prefix_seed:      
    for i,line in enumerate(prefix_list):
        router_line = router_list[i]
        prefix_seed.write(router_line.strip('\n')+';'+prefix_list[i]+'\n')

print('Sleep 5 second before announce IP Prefix  by each router')
time.sleep(5)
print(prefix_list)
with open('prefix_list.txt','r') as prefix_list:
    for prefix in prefix_list:
        router_ip, asn, prefix = map(str.strip,prefix.split(';'))

        print('Announcing '+prefix+ ' by router  '+router_ip)
        shell_path = os.getcwd()+'/prefix_announcement.sh'
        os.system(shell_path + ' '+ router_ip +' '+asn + ' '+prefix)

