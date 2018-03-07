import matplotlib.pyplot as plt
import numpy as np

p = argparse.ArgumentParser(
        usage='plot statistic CSV output from perf stat -r in bar chart',
        description='''
perf stat -I1000 -x, -o file ...
toplev -I1000 -x, -o file ... 
bar-plot.py file (or stdin)
delimeter must be ,
this is for data that is not normalized.''')
p.add_argument('file', help='CSV file to plot (or stdin)', nargs='?')
p.add_argument('--output', '-o', help='Output to file. Otherwise show.', 
               nargs='?')
args = p.parse_args()

label = ['Adventure', 'Action', 'Drama', 'Comedy', 'Thriller/Suspense', 'Horror', 'Romantic Comedy', 'Musical',
         'Documentary', 'Black Comedy', 'Western', 'Concert/Performance', 'Multiple Genres', 'Reality']
         
no_movies = [
    941,
    854,
    4595,
    2125,
    942,
    509,
    548,
    149,
    1952,
    161,
    64,
    61,
    35,
    5
]

def plot_bar_x():
    # this is for plotting purpose
    index = np.arange(len(label))
    plt.bar(index, no_movies)
    plt.xlabel('Genre', fontsize=5)
    plt.ylabel('No of Movies', fontsize=5)
    plt.xticks(index, label, fontsize=5, rotation=30)
    plt.title('Market Share for Each Genre 1995-2017')
    plt.show()

plot_bar_x()