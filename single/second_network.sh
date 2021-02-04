#!/bin/bash
# This script is use to create a BGP network as a playground for Blockjack testing scenario

docker network create --subnet=192.8.0.0/16 blockjack2
docker run --name block1 --net blockjack2 --ip 192.8.1.1 --hostname=blocka1 -d -v `pwd`/block1:/etc/quagga:rw pierky/quagga
docker run --name block2 --net blockjack2 --ip 192.8.2.2 --hostname=blocka2 -d -v `pwd`/block2:/etc/quagga:rw pierky/quagga
docker run --name block3 --net blockjack2 --ip 192.8.3.3 --hostname=blocka3 -d -v `pwd`/block3:/etc/quagga:rw pierky/quagga
docker run --name block4 --net blockjack2 --ip 192.8.4.4 --hostname=blocka4 -d -v `pwd`/block4:/etc/quagga:rw pierky/quagga
docker run --name block5 --net blockjack2 --ip 192.8.5.5 --hostname=blocka5 -d -v `pwd`/block5:/etc/quagga:rw pierky/quagga
docker run --name block6 --net blockjack2 --ip 192.8.6.6 --hostname=blocka6 -d -v `pwd`/block6:/etc/quagga:rw pierky/quagga
docker run --name block7 --net blockjack2 --ip 192.8.7.7 --hostname=blocka7 -d -v `pwd`/block7:/etc/quagga:rw pierky/quagga
docker run --name block8 --net blockjack2 --ip 192.8.8.8 --hostname=blocka8 -d -v `pwd`/block8:/etc/quagga:rw pierky/quagga
docker run --name block9 --net blockjack2 --ip 192.8.9.9 --hostname=blocka9 -d -v `pwd`/block9:/etc/quagga:rw pierky/quagga
docker run --name block10 --net blockjack2 --ip 192.8.10.10 --hostname=blocka10 -d -v `pwd`/block10:/etc/quagga:rw pierky/quagga
