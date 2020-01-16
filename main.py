import time
import math  
from threading import Thread 
from multiprocessing import Process

from data_plot import DataPlot
from data_join import DataJoin
       
def plot(part, count, save=False, show=False):

    plot = DataPlot(part, count)
    plot.create()

    if save:
        plot.save()
    
    if show:
        plot.show()

def runShow(part=0, count=-1):
    plot(part, count, show=True)

def runJoin():
    join = DataJoin()

def runSave(start, end, count):

    all_processes = []

    for i in range(start, end):
        p = Process(target=plot, args=(i, count, True))
        p.start()
        all_processes.append(p)
        time.sleep(1)

    for p in all_processes:
        p.join()

if __name__ == '__main__':
    
    size = DataPlot(0, -1).size

    count = 10000
    parts = int(size/count)
    part = 0
    step = 20
    
    while part < parts:
        runSave(part, min(parts + 1, part + step), count)
        part += step

    runJoin()
