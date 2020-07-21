import pandas as pd

from settings import data_file, end_video, ini_video
from util import parseTimestampToDate

class DataSource:

    """ This class manages the data sources, including the loading of the datasets, adjust the data to be in the same time interval as the external environment video, in addition to determining general parameters."""

    data = None
    """ Loaded data """
    size = None
    """ Dataset size """
    fps = None
    """ Frames per second to create video """
    interval = None
    """ Interval between the samples in milisseconds """
    sample_start = 0
    """ Sample where start de video creation """

    def load(self):
        """
        Load the dataset and define global parameters.
        """

        data = pd.read_csv(data_file, float_precision="high")
        self.data = self.__cutData(data)
        self.size = len(self.data)
        self.interval = round(1000 * (self.data['timestamp'].values[-1] - self.data['timestamp'].values[0]) / self.size)
        self.fps = round(1000 / self.interval)

    def __cutData(self, data):
        """
        Cut the data to match the time interval of external environment video.

        Args:
            data (dataframe): the loaded dataset.

        Returns:
            dataframe: dataset adjusted.
        """

        ini_df = data[data['timestamp'] == ini_video].index
        end_df = data[data['timestamp'] == end_video].index

        ini_index = ini_df.values[0] if len(ini_df) > 0 else 0
        end_index = end_df.values[0] if len(end_df) > 0 else -1

        self.sample_start = ini_index

        return data[ini_index:end_index + 1]
