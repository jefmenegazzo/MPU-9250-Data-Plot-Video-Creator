import os
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from data_source import DataSource
from settings import videos_folder
from util import parseTimestampToDate

class DataPlot:

    axesAll = []
    linesAll = []
    sourcesAll = []
    axesLegend = None

    data_source = None
    x_points = None
    window = 1000
    count = None
    part = None
    start = None
    end = None

    fig = None
    gs = None
    
    # Getters para Data Source

    @property
    def data(self):
        return self.data_source.data

    @property
    def interval(self):
        return self.data_source.interval

    @property
    def fps(self):
        return self.data_source.fps

    @property
    def size(self):
        return self.data_source.size

    def __init__(self, part, count):
 
        self.data_source = DataSource()
        self.x_points = np.arange(self.size)

        self.part = part
        self.count = self.size if count == -1 else count

        self.start = self.part * self.count
        self.end = min(((self.part + 1) * self.count), self.size) - 1
        self.count = self.end - self.start + 1

    def createLine(self, axes, ydata, color, label):

        line, = axes.plot(self.x_points, ydata, color=color, label=label) 

        axes.ticklabel_format(useOffset=False, style="plain")
        self.axesAll.append(axes)
        self.linesAll.append(line)
        self.sourcesAll.append(ydata)

    def createSubPlotLegend(self):

        self.axesLegend = self.fig.add_subplot(self.gs[0, 2])
        self.axesLegend.set_axis_off()
        legend = self.axesLegend.legend(handles=self.linesAll[0:4], loc='center')

    def createSubPlotSpeed(self):
    
        speed_color = 'k'
        speed_label = 'Speed'
        ydata = self.data['speed'] * 3.6

        axes = self.fig.add_subplot(self.gs[0, 0:2])
        axes.set_title('', fontdict = {'fontsize' : 10})
        axes.set_xlabel('Sample Number')
        axes.set_ylabel('Speed (km/h)')

        self.createLine(axes=axes, ydata=ydata, color=speed_color, label=speed_label)
    
    def createSubPlot(self, loc, title='', ylabel='', xlabel='', field=''):
    
        axes = self.fig.add_subplot(self.gs[loc[0], loc[1]])
        axes.set_title(title, fontdict = {'fontsize' : 10})
        axes.set_xlabel(xlabel)
        axes.set_ylabel(ylabel)

        if not(field.startswith('mag')):
            bellow_suspension_color = 'g'
            bellow_suspension_label = 'Below Suspension'
            ydata = self.data[field + '_below_suspension']
            self.createLine(axes=axes, ydata=ydata, color=bellow_suspension_color, label=bellow_suspension_label)

        above_suspension_color = 'b'
        above_suspension_label = 'Above Suspension'
        ydata = self.data[field + '_above_suspension']
        self.createLine(axes=axes, ydata=ydata, color=above_suspension_color, label=above_suspension_label)
        
        dashboard_color = 'r'
        dashboard_label = 'Dashboard'
        ydata = self.data[field + '_dashboard']
        self.createLine(axes=axes, ydata=ydata, color=dashboard_color, label=dashboard_label)

    def create(self):
                
        self.fig = plt.figure(self.part, figsize=(16, 9))
        self.gs = self.fig.add_gridspec(nrows=4, ncols=3, wspace=0.25, hspace=0.5)
        
        self.createSubPlotSpeed()

        self.createSubPlot(loc=[1,0], field='gyro_x', title='X-Axis', ylabel='Rotation Rate (°/s)')
        self.createSubPlot(loc=[1,1], field='gyro_y', title='Y-Axis')
        self.createSubPlot(loc=[1,2], field='gyro_z', title='Z-Axis')

        self.createSubPlot(loc=[2,0], field='acc_x', ylabel='Acceleration (m/s²)')
        self.createSubPlot(loc=[2,1], field='acc_y')
        self.createSubPlot(loc=[2,2], field='acc_z')

        self.createSubPlot(loc=[3,0], xlabel='Sample Number', field='mag_x', ylabel='Magnetic Field (μT)')
        self.createSubPlot(loc=[3,1], xlabel='Sample Number', field='mag_y')
        self.createSubPlot(loc=[3,2], xlabel='Sample Number', field='mag_z')

        self.createSubPlotLegend()

    # Plot no Notebook
    def show(self):
        self.plot(show=True)
        
    # Plot para video
    def save(self):
        self.plot(save=True)

    # Limpa todas as linhas
    def clear(self):

        for line in self.linesAll:
            line.set_data([], [])

    # Desenha dados do ponto i
    def point(self, i):

        position = self.start + i - 1
        startWindow = max(0, position - self.window)
        endWindow = min(max(1, position), self.end)

        xdata = self.x_points[startWindow : endWindow + 1]

        for j in range(0, len(self.linesAll)):
            ydata = self.sourcesAll[j][startWindow: endWindow + 1]
            self.linesAll[j].set_data(xdata, ydata)

        for j in range(0, len(self.axesAll)):
            self.axesAll[j].set_xlim(left=startWindow, right=endWindow)
            # self.axesAll[j].relim() 
            # self.axesAll[j].autoscale_view()
        
        self.axesLegend.set_title("Time: " + parseTimestampToDate(self.data['timestamp'].iloc[position]), fontdict = {'fontsize' : 10})
        
    def plot(self, save=False, show=False):

        linesTuple = tuple(self.linesAll)
        load_bar = tqdm(total=self.count, position=self.part, desc='Part ' + str(self.part), ascii=True, ncols=200)

        def init():
            self.clear()
            return linesTuple

        def animate(i):
            self.point(i)
            # fig.canvas.draw()
            return linesTuple
        
        def progress(current_frame: int, total_frames: int):
            load_bar.update(1)

        anim = FuncAnimation(self.fig, animate, init_func=init, frames= self.count, repeat=False, interval=self.interval)

        if save:
            anim.save(os.path.join(videos_folder, "part_" + str(self.part) + ".mp4"), fps=self.fps, extra_args=['-vcodec', 'libx264'], progress_callback=progress)

        if show:
            plt.show()
