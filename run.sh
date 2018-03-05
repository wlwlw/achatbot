#!/bin/bash

#docker rm achatbot
#echo 0 > /proc/sys/kernel/nmi_watchdog
pmu-tools/toplev.py -I200 -x, -o test.csv -l3 sleep 20
pmu-tools/interval-plot.py test.csv
#docker run --name achatbot achatbots