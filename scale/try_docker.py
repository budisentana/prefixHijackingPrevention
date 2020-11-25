import os
import subprocess


print('Creating Docker container Network ')
docker_net = 'docker network create --subnet=99.0.0.0/8 blockjack-bgp-net'
print(str(docker_net))
os.system(docker_net)

router_name = 'router1'
host_ip = '99.3.4.5'
host_name = 'host1'
as_name = 'AS10'

docker_run = 'docker run --name '+ router_name+' --net blockjack-bgp-net --ip '+ host_ip+' --hostname='+host_name+' -d -v `pwd`/'+as_name+':/etc/quagga:rw pierky/quagga'
print(docker_run)
os.system(docker_run)


# argument = router_name+' '+host_ip+ ' '+host_name+' '+as_name
# subprocess.Popen(["bash","run_docker.sh",router_name,host_ip,host_name,as_name])

# docker_run = 'docker run --name '+ router_name+' --net blockjack-bgp-net --ip '+ host_ip+' --hostname='+host_name+' -d -v `pwd`/'+as_name+':/etc/quagga:rw pierky/quagga'
# print(str(docker_run))
# os.system(docker_run)
