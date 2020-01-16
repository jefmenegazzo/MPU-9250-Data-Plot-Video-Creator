import pandas as pd

from settings import folder, data_file, ini_video, end_video

class DataSource:

    data = None
    size = None
    fps = None
    interval = None

    # Construtor
    def __init__(self):
        self.load()

    # Carregamento de dados
    def load(self):

        # Carrega os dados
        data = pd.read_csv(folder + data_file, float_precision="high")

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
        ini_index = data[data['timestamp'] == ini_video].index.values[0]
        end_index = data[data['timestamp'] == end_video].index.values[0]
        return data[ini_index: end_index + 1]
