#!/bin/bash

perf stat -e \
cycles,instructions,branch-misses,cache-misses,\
L1-dcache-load-misses,\
L1-dcache-store-misses \
-I1000 -x, -o result-$1-$2.csv python trainTest.py $1 $2

python pmu-tools/interval-plot-modified.py -m IPC -o result-$1-$2-IPC result-$1-$2.csv
python pmu-tools/interval-plot-modified.py -m MPKI -o result-$1-$2-MPKI result-$1-$2.csv