#!/usr/bin/env python
# author: lwang107@ucsc.edu
import argparse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import sys
import math

p = argparse.ArgumentParser(
        usage='plot statistic CSV output from perf stat -r in bar chart',
        description='''
perf stat -e cpu-clock -x, -o file ...
bar-plot.py -n 100 file (or stdin)
delimeter must be ,
this is for data that is not normalized.''')
p.add_argument('file', help='CSV file to plot (or stdin)', nargs='?')
p.add_argument('--num', '-n', help='Number of output columns. 20 by default', 
               nargs='?')
p.add_argument('--output', '-o', help='Output to file. Otherwise show.', 
               nargs='?')
args = p.parse_args()

if args.file:
    inf = open(args.file, "r")
else:
    inf = sys.stdin

ts = []
for line in inf:
    t = line.split(',')[0]
    try:
        ts.append(float(t))
    except ValueError:
        pass
ts.sort()
num = int(args.num) if args.num else 20
delta = math.ceil((ts[-1]-ts[0])/num)
step = 0
stat = [0]
start = math.floor(ts[0])
for t in ts:
    if(t<start+step*delta):
        raise ValueError(ts)
    while(t>=start+(step+1)*delta):
        step+=1
        stat.append(0)
    stat[step]=stat[step]+1
        
label = [str((start+(s+0.5)*delta)) for s in range(step+1)]

def plot_bar_x():
    # this is for plotting purpose
    index = np.arange(len(label))
    plt.bar(index, stat)
    plt.xlabel('cpu-clock(ms)', fontsize=10)
    plt.ylabel('count', fontsize=10)
    plt.xticks(index, label, fontsize=7, rotation=0)
    plt.title('Response time distribution of chatterbot')
    if args.output:
        plt.savefig(args.output)
    else:
        plt.show()

plot_bar_x()