import time
import math
from threading import Thread
from multiprocessing import Process

from data_plot import DataPlot
from data_join import DataJoin
from data_source import DataSource
"""
Shows the plotted data in live plot.
"""

def runShow(part=0, count=-1):
    plot = DataPlot(part, count)
    plot.create()
    plot.show()

if __name__ == '__main__':

    # To plot a specific interval
    # count = 10000 # How much samples show
    # part = 1 # Part to start plot (each part is dataset size / count)
    # runShow(part, count)

    # To show all data from the begining
    runShow()
