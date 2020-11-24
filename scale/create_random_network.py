import plotly.graph_objects as go
import networkx as nx
import random
import os

n = 10
print('Creating '+str(n)+' random geometric node graph ')
G = nx.random_geometric_graph(n, 0.125)

ip_list =[]
print('Creating '+str(n)+' random IP address for the node')
while len(ip_list) < n:
    x1 = 99
    x2 = random.randint(0,255)
    x3 = random.randint(0,255)        
    x4 = random.randint(0,255)
    result = ".".join(map(str,([x1,x2,x3,x4])))
    if result not in ip_list:    
        ip_list.append(result)

# for i,item in enumerate (ip_list):
#     print('ini adalah '+str(i+1)+ ' : ' +str(item))

print('Creating Docker container Network ')
docker_net = 'docker network create --subnet=99.0.0.0/8 blockjack-bgp-net'
print(str(docker_net))
os.system(docker_net)

node_att =[]
for i,node in enumerate(G.nodes()):
    host_name = 'host'+str(node+1)
    host_ip = ip_list[i]
    as_name = 'AS'+str(node+1)
    router_name = 'router'+str(node+1)
    node_att.append(host_name+';'+host_ip+';'+router_name+';'+as_name)

    print('Creating Directory of '+as_name )
    mk_dir = 'mkdir '+as_name
    os.system(mk_dir)
    print('Copying quagga configuration file to '+router_name)
    cp_conf = 'sudo cp quagga.conf `pwd`/'+as_name+'/quagga.conf'
    os.system(cp_conf)

    print('Run '+router_name+ ' on Docker Container in Detach mode')
    print('Assigning IP Address ' +host_ip + ' to the Router')
    print('Attaching router to the network')
    docker_run = 'docker run --name '+ router_name+' --net blockjack-bgp-net --ip '+ host_ip+' --hostname='+host_name+' -d -v `pwd`/'+as_name+':/etc/quagga:rw pierky/quagga'
    print(docker_run)
    os.system(docker_run)

print('Writing the node configuration to the file ')
with open('node_setup.txt','w') as node_seed:
    for row in node_att :
        node_seed.write(row+'\n')

