#!/bin/bash
rm result-latency-$1.csv
touch result-$1-latency.csv
for((n=0;n<$1;n++))
do
	RES="$(perf stat -e cpu-clock -x, --log-fd 3 3>>result-latency-$1.csv python responseTest.py)"
	echo "Response $n: $RES"
done

python pmu-tools/bar-plot.py -n 20 -o result-$1-latency.png result-$1-latency.csv