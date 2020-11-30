#!/bin/bash


con_num=$(docker ps -a | grep quagga | wc -l)

docker rm -f $(docker ps -a -q)
docker network rm blockjack-bgp-net

echo "$(($con_num))"
for ((i=1; i<=$(($con_num)); i++))
do 
	rm -r AS$i
	echo "Drop AS$i"
done
