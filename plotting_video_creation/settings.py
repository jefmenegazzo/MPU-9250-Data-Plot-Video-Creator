import os
from util import parseDateToTimestamp, createFolder

#######################################################################################

workspace = {
    "saveiro-1": {
        "folder": 'E:\\Dados Processados\\100 Hz\\PVS 1\\',
        "ini": "2019-12-24T17:21:14",
        "end": "2019-12-24T17:43:48"
    },
    "saveiro-2": {
        "folder": 'E:\\Dados Processados\\100 Hz\\PVS 2\\',
        "ini": "2019-12-24T17:59:54",
        "end": "2019-12-24T18:20:05"
    },
    "saveiro-3": {
        "folder": 'E:\\Dados Processados\\100 Hz\\PVS 3\\',
        "ini": "2019-12-24T18:37:14",
        "end": "2019-12-24T18:53:37"
    },
    "bravo-1": {
        "folder": 'E:\\Dados Processados\\100 Hz\\PVS 4\\',
        "ini": "2019-12-25T17:44:49",
        "end": "2019-12-25T18:08:38"
    },
    "bravo-2": {
        "folder": 'E:\\Dados Processados\\100 Hz\\PVS 5\\',
        "ini": "2019-12-25T18:17:05",
        "end": "2019-12-25T18:38:50"
    },
    "bravo-3": {
        
    },
    "palio-1": {
        
    },
    "palio-2": {
        
    },
    "palio-3": {
        
    },
}

#######################################################################################

dataset = workspace['saveiro-3']
folder = dataset['folder']

side = "left"
# side = "right"

ini_video = parseDateToTimestamp(dataset['ini'])
end_video = parseDateToTimestamp(dataset['end'])
data_file = os.path.join(folder, "dataset_gps_mpu_" + side + ".csv")
video_file = "video_dataset_" + side + ".mp4"
videos_folder = os.path.join(folder, "videos_" + side)
createFolder(videos_folder)