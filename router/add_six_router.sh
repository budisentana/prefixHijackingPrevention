#!/bin/bash
# This script is use to create a BGP network as a playground for Blockjack testing scenario
docker run --name router5 --net blockjack-bgp-net --ip 192.9.5.5 --hostname=routera5 -d -v `pwd`/AS5:/etc/quagga:rw pierky/quagga
echo "router5 for AS5 created"
docker run --name router6 --net blockjack-bgp-net --ip 192.9.6.6 --hostname=routera6 -d -v `pwd`/AS6:/etc/quagga:rw pierky/quagga
echo "router6 for AS6 created"
docker run --name router7 --net blockjack-bgp-net --ip 192.9.7.7 --hostname=routera7 -d -v `pwd`/AS7:/etc/quagga:rw pierky/quagga
echo "router7 for AS7 created"
docker run --name router8 --net blockjack-bgp-net --ip 192.9.8.8 --hostname=routera8 -d -v `pwd`/AS8:/etc/quagga:rw pierky/quagga
echo "router8 for AS8 created"
docker run --name router9 --net blockjack-bgp-net --ip 192.9.9.9 --hostname=routera9 -d -v `pwd`/AS9:/etc/quagga:rw pierky/quagga
echo "router9 for AS9 created"
docker run --name router10 --net blockjack-bgp-net --ip 192.9.10.10 --hostname=routera10 -d -v `pwd`/AS10:/etc/quagga:rw pierky/quagga
echo "router10 for AS10 created"
echo "configuration done"
