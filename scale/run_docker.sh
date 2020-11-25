#!/bin/bash
# This script is use to create a BGP network as a playground for Blockjack testing scenario

# router_name='router1'
# host_ip='192.9.3.4'
# host_name='host1'
# as_name='AS10'
router_name=$1
host_ip=$2
host_name=$3
as_name=$4


# echo "This is the bash file for the configuration of  four router using quagga in docker container"
# docker network create --subnet=192.9.0.0/16 blockjack-bgp-net
# echo "Network created"
# docker run --name $router_name --net blockjack-bgp-net --ip $host_ip --hostname=$host_name -d -v `pwd`/$as_name:/etc/quagga:rw pierky/quagga
# docker run --name router1 --net blockjack-bgp-net --ip 192.9.1.1 --hostname=routera1 -d -v `pwd`/AS10:/etc/quagga:rw pierky/quagga
docker run --name $router_name --net blockjack-bgp-net --ip $host_ip --hostname=$host_name -d -v `pwd`/$as_name:/etc/quagga:rw pierky/quagga
