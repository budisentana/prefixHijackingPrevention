#!/bin/bash
# This script is use to clean up a BGP network as a playground for Blockjack testing scenario
echo "This is the bash file to clean up of  four router using quagga in docker container"
docker rm -f router1
echo "router1 Down"
docker rm -f router2
echo "router2 Down"
docker rm -f router3
echo "router3 Down"
docker rm -f router4
echo "router4 Down"
docker rm -f router5
echo "router5 Down"
docker rm -f router6
echo "router6 Down"
docker rm -f router7
echo "router7 Down"
docker rm -f router8
echo "router8 Down"
docker rm -f router9
echo "router9 Down"
docker rm -f router10
echo "router10 Down"
docker network rm blockjack-bgp-net
echo "Network Down"
echo "clean up done"
