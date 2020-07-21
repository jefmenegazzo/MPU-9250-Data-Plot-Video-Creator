import time
import math
from threading import Thread
from multiprocessing import Process

from data_plot import DataPlot
from data_join import DataJoin
from data_source import DataSource
"""
Save the plotted data in MP4 file.
"""

def plot(part, count):
    plot = DataPlot(part, count)
    plot.create()
    plot.save()

def runJoin():
    join = DataJoin()
    join.run()

def runSave(start, end, count):

    all_processes = []

    for i in range(start, end):
        p = Process(target=plot, args=(i, count))
        p.start()
        all_processes.append(p)
        time.sleep(1)

    for p in all_processes:
        p.join()

if __name__ == '__main__':

    source = DataSource()
    source.load()
    size = source.size

    # How much samples to plot in each part
    count = 10000
    # How much parts
    parts = int(size / count)
    # First part
    part = 0
    # Amount of parts to be generate in parallel
    step = 20

    while part < parts:
        runSave(part, min(parts + 1, part + step), count)
        part += step

    runJoin()
