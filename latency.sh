#!/bin/bash
rm result-$1-latency.csv
touch result-$1-latency.csv
for((n=0;n<$1;n++))
do
	RES="$(perf stat -e cpu-clock -x, --log-fd 3 3>>result-$1-latency.csv python responseTest.py)"
	echo "Response $n: $RES"
done

python pmu-tools/bar-plot.py -n $2 -o result-$1-latency.png result-$1-latency.csv