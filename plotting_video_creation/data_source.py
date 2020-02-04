import pandas as pd

from settings import data_file, ini_video, end_video
from util import parseTimestampToDate

class DataSource:

    data = None
    size = None
    fps = None
    interval = None
    sample_start = 0

    # Construtor
    def __init__(self):
        self.load()

    # Carregamento de dados
    def load(self):

        # Carrega os dados
        data = pd.read_csv(data_file, float_precision="high")

        # Corta Dados
        self.data = self.cutData(data)

        # Tamanho do Data Set
        self.size = len(self.data)

        # Intervalo de tempo entre as amostras - em milisegundos
        self.interval = round(1000 * (self.data['timestamp'].values[-1] - self.data['timestamp'].values[0]) / self.size)

        # Frames por segundo
        self.fps = round(1000 / self.interval)

    # Corta dados para ficar no intervalo de vídeo
    def cutData(self, data):

        ini_df = data[data['timestamp'] == ini_video].index
        end_df = data[data['timestamp'] == end_video].index

        ini_index = ini_df.values[0] if len(ini_df) > 0 else 0
        end_index = end_df.values[0] if len(end_df) > 0 else -1

        self.sample_start = ini_index

        return data[ini_index: end_index + 1]
