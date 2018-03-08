#!/bin/bash
# Start benchmark container and run throughput/latency test
# Run throughput with 1 2 4 8 thread of size 8 16 32 64 test set(both needs to be integer)
# return IPC, Brach MPKI, cache MPKI statistic.
# Run latency test 200 times, return distribution chart of response time.
# Retreve result back as .csv and .png in result folder.

docker rm achatbot
docker run -td --privileged --name achatbot achatbot

# first run throughput test
for thread in 1 2 4 8
do
	for size in 8 16 32 64
	do
		docker exec achatbot /app/throughput.sh $size $thread
		docker cp achatbot:/app/result-$size-$thread-IPC.png ./result/
		docker cp achatbot:/app/result-$size-$thread-MPKI.png ./result/
		docker cp achatbot:/app/result-$size-$thread.csv ./result/
	done
done
rm db.sqlite3

# then run latency test
LA_SIZE="200"
NUM="20"
docker exec achatbot /app/latency.sh $LA_SIZE $NUM
docker cp achatbot:/app/result-$LA_SIZE-latency.png ./result/
docker cp achatbot:/app/result-$LA_SIZE-latency.csv ./result/

docker stop achatbot