import os
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from data_source import DataSource
from settings import videos_folder
from util import parseTimestampToDate

class DataPlot:

    """ This class creates the video with plotted data. """

    axes_all = []
    """ All the axes """
    lines_all = []
    """ All the lines """
    sources_all = []
    """ Data sources where each value is the data to be plotted in a corresponding line """
    axes_legend = None
    """ Axes for legend """
    data_source = None
    """ Instance of DataSource """
    x_points = None
    """ Points to X axis """
    window = 1000
    """ Window of plot (amount of data by second in a frame)"""
    count = None
    """ Amount of data to be ploted in this video part. Equals to length of interval between start and end indexes. """
    part = None
    """ Video part (sequence) """
    start = None
    """ Index the refer the first sample to be plotted in this video part """
    end = None
    """ Index the refer the last sample to be plotted in this video part """
    fig = None
    """ Matplot Figure, where axes and lines are plotted """
    gs = None
    """ Matplotlib Grid Specification """

    @property
    def data(self):
        """Get data loaded.

        Returns:
            dataframe: the data.
        """
        return self.data_source.data

    @property
    def interval(self):
        """
        Get interval between two samples (in ms).

        Returns:
            int: the interval.
        """
        return self.data_source.interval

    @property
    def fps(self):
        """
        Frames per second to create video.

        Returns:
            int: the fps.
        """
        return self.data_source.fps

    @property
    def size(self):
        """
        The dataset size.

        Returns:
            int: the size.
        """
        return self.data_source.size

    @property
    def sample_start(self):
        """
        Sample where starts de video creation.
        It is used for show sample number in the legend.

        Returns:
            int: the index of start.
        """
        return self.data_source.sample_start

    def __init__(self, part, count):
        """
        Initialize the plot class.
        Instanciate a DataSource and load data.

        Args:
            part (int): index sequence of video parts.
            count (int): amount of data to be ploted in this video part.
        """

        self.data_source = DataSource()
        self.data_source.load()
        self.x_points = np.arange(self.size)

        self.part = part
        self.count = self.size if count == -1 else count

        self.start = self.part * self.count
        self.end = min(((self.part + 1) * self.count), self.size) - 1
        self.count = self.end - self.start + 1

    def createLine(self, axes, ydata, color, label):
        """
        Create a line in a plot area.

        Args:
            axes (axes): axes from the subplot.
            ydata (dataframe): data to plot in Y axis.
            color (str): color of line.
            label (str): line label (to legend).
        """

        line, = axes.plot(self.x_points, ydata, color=color, label=label)

        axes.ticklabel_format(useOffset=False, style="plain")
        self.axes_all.append(axes)
        self.lines_all.append(line)
        self.sources_all.append(ydata)

    def createSubPlotLegend(self):
        """
        Create the subplot where is plotted the legend.
        """

        self.axesLegend = self.fig.add_subplot(self.gs[0, 2])
        self.axesLegend.set_axis_off()
        legend = self.axesLegend.legend(handles=self.lines_all[0:4], loc='center')

    def createSubPlotSpeed(self):
        """
        Create the subplot where is plotted speed data in km/h.
        """

        speed_color = 'k'
        speed_label = 'Speed'
        ydata = self.data['speed'] * 3.6

        axes = self.fig.add_subplot(self.gs[0, 0:2])
        axes.set_title('', fontdict={'fontsize': 10})
        axes.set_xlabel('Sample Number')
        axes.set_ylabel('Speed (km/h)')

        self.createLine(axes=axes, ydata=ydata, color=speed_color, label=speed_label)

    def createSubPlot(self, loc, title='', ylabel='', xlabel='', field=''):
        """
        Create the subplot where is plotted the data from accelerometer, gyroscope and magnetometer.

        Args:
            loc (list): location in grid spec.
            title (str, optional): title of subplot. Defaults to ''.
            ylabel (str, optional): label of subplot Y axis. Defaults to ''.
            xlabel (str, optional): label of subplot X axis. Defaults to ''.
            field (str, optional): preffix corresponding to field data type and axis. Defaults to ''.
        """

        axes = self.fig.add_subplot(self.gs[loc[0], loc[1]])
        axes.set_title(title, fontdict={'fontsize': 10})
        axes.set_xlabel(xlabel)
        axes.set_ylabel(ylabel)

        if not (field.startswith('mag')):
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
        """
        Create the plot area.
        """

        self.fig = plt.figure(self.part, figsize=(16, 9))
        self.gs = self.fig.add_gridspec(nrows=4, ncols=3, wspace=0.25, hspace=0.5)

        self.createSubPlotSpeed()

        self.createSubPlot(loc=[1, 0], field='gyro_x', title='X-Axis', ylabel='Rotation Rate (°/s)')
        self.createSubPlot(loc=[1, 1], field='gyro_y', title='Y-Axis')
        self.createSubPlot(loc=[1, 2], field='gyro_z', title='Z-Axis')

        self.createSubPlot(loc=[2, 0], field='acc_x', ylabel='Acceleration (m/s²)')
        self.createSubPlot(loc=[2, 1], field='acc_y')
        self.createSubPlot(loc=[2, 2], field='acc_z')

        self.createSubPlot(loc=[3, 0], xlabel='Sample Number', field='mag_x', ylabel='Magnetic Field (μT)')
        self.createSubPlot(loc=[3, 1], xlabel='Sample Number', field='mag_y')
        self.createSubPlot(loc=[3, 2], xlabel='Sample Number', field='mag_z')

        self.createSubPlotLegend()

    def show(self):
        """
        Shows a live data plotting.
        """
        self.plot(show=True)

    def save(self):
        """
        Save a video with plotted data.
        """
        self.plot(save=True)

    def clear(self):
        """
        Clear all the lines.
        """

        for line in self.lines_all:
            line.set_data([], [])

    def point(self, i):
        """
        Draw the data of point i in all subplots (lines/axes).

        Args:
            i (int): index point.
        """

        position = self.start + i - 1
        startWindow = max(0, position - self.window)
        endWindow = min(max(1, position), self.end)

        xdata = self.x_points[startWindow:endWindow + 1]

        for j in range(0, len(self.lines_all)):
            ydata = self.sources_all[j][startWindow:endWindow + 1]
            self.lines_all[j].set_data(xdata, ydata)

        for j in range(0, len(self.axes_all)):
            self.axes_all[j].set_xlim(left=startWindow, right=endWindow)
            # self.axes_all[j].relim()
            # self.axes_all[j].autoscale_view()

        self.axesLegend.set_title("Time: " + parseTimestampToDate(self.data['timestamp'].iloc[position]) + " | Sample: " + str(self.sample_start + position), fontdict={'fontsize': 10})

    def plot(self, save=False, show=False):
        """
        Starts process to create a animated data plot (video).
        Each video part generation progress is showed in a loading bar. 

        Args:
            save (bool, optional): if plot must be saved to a .mp4 file. Defaults to False.
            show (bool, optional): if plot must be showed in live plot. Defaults to False.
        """

        linesTuple = tuple(self.lines_all)
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

        anim = FuncAnimation(self.fig, animate, init_func=init, frames=self.count, repeat=False, interval=self.interval)

        if save:
            anim.save(os.path.join(videos_folder, "part_" + str(self.part) + ".mp4"), fps=self.fps, extra_args=['-vcodec', 'libx264'], progress_callback=progress)

        if show:
            plt.show()
