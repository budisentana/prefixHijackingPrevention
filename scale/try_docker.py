import os
import subprocess
import time
import timeit
from pathlib import Path


start = time.time()
# start = timeit.default_timer()
# for item in range (0,10):
#     print('process')
time.sleep(5)
end = time.time()
# end = timeit.default_timer()
result = end - start
print(start)
print(result)

two_up = Path().absolute().parent.parent.parent
print(two_up/'time_note.txt')


# print('Creating Docker container Network ')
# docker_net = 'docker network create --subnet=99.0.0.0/8 blockjack-bgp-net'
# print(str(docker_net))
# os.system(docker_net)

# router_name = 'router1'
# host_ip = '99.3.4.5'
# host_name = 'host1'
# as_name = 'AS10'

# docker_run = 'docker run --name '+ router_name+' --net blockjack-bgp-net --ip '+ host_ip+' --hostname='+host_name+' -d -v `pwd`/'+as_name+':/etc/quagga:rw pierky/quagga'
# print(docker_run)
# os.system(docker_run)


# argument = router_name+' '+host_ip+ ' '+host_name+' '+as_name
# subprocess.Popen(["bash","run_docker.sh",router_name,host_ip,host_name,as_name])

# docker_run = 'docker run --name '+ router_name+' --net blockjack-bgp-net --ip '+ host_ip+' --hostname='+host_name+' -d -v `pwd`/'+as_name+':/etc/quagga:rw pierky/quagga'
# print(str(docker_run))
# # os.system(docker_run)

# root = os.path.dirname(os.getcwd())
# server_path = root+'/server/'

# print('Deploying Blockchain module')
# os.chdir(server_path)
# os.system('./startbsbri.sh')

# Installing node js module (npm install)
# print('Installing node js to server')
# os.chdir(server_path+'/server1/')
# os.system('npm install')


# # Create admin and router credential
# print ('Create admin and router credential')
# os.system('node enrollAdmin.js')
# os.system('node registerRouter.js')
# print('Activating REST API server')
# # os.system('node apiServer.js')
# server = os.getcwd()+'/apiServer.js'
# print(server)
# subprocess.Popen(["node",server])

# print('Sleep 5 second before Sending prefix to the Blockchain')
# time.sleep(5)