#!/bin/bash
# This script is use to create a BGP network as a playground for Blockjack testing scenario
echo "This is the bash file for the configuration of  four router using quagga in docker container"
docker network create --subnet=192.9.0.0/16 blockjack-bgp-net
echo "Network created"
docker run --name router1 --net blockjack-bgp-net --ip 192.9.1.1 --hostname=routera1 -d -v `pwd`/AS1111:/etc/quagga:rw pierky/quagga
echo "router1 for AS1111 created"
docker run --name router2 --net blockjack-bgp-net --ip 192.9.2.2 --hostname=routera2 -d -v `pwd`/AS2222:/etc/quagga:rw pierky/quagga
echo "router2 for AS2222 created"
docker run --name router3 --net blockjack-bgp-net --ip 192.9.3.3 --hostname=routera3 -d -v `pwd`/AS3333:/etc/quagga:rw pierky/quagga
echo "router3 for AS3333 created"
docker run --name router4 --net blockjack-bgp-net --ip 192.9.4.4 --hostname=routera4 -d -v `pwd`/AS4444:/etc/quagga:rw pierky/quagga
echo "router4 for AS4444 created"
echo "configuration done"
