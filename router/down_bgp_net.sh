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
docker network rm blockjack-bgp-net
echo "Network Down"
echo "clean up done"
