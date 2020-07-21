import os
from util import parseDateToTimestamp, createFolder
"""
This is the settings file.

The **workspace** describe the path location of each dataset, and the time when starts and ends external environment video.

Here are define the paramters of which one datase will be plotted, and the side.

"""

workspace = {
    "pvs-1": {
        "description": "saveiro-1",
        "folder": 'E:\\DataSets\\100 Hz\\PVS 1\\',
        "ini": "2019-12-24T17:21:14",
        "end": "2019-12-24T17:43:48"
    },
    "pvs-2": {
        "description": "saveiro-2",
        "folder": 'E:\\DataSets\\100 Hz\\PVS 2\\',
        "ini": "2019-12-24T17:59:54",
        "end": "2019-12-24T18:20:05"
    },
    "pvs-3": {
        "description": "saveiro-3",
        "folder": 'E:\\DataSets\\100 Hz\\PVS 3\\',
        "ini": "2019-12-24T18:37:14",
        "end": "2019-12-24T18:53:37"
    },
    "pvs-4": {
        "description": "bravo-1",
        "folder": 'E:\\DataSets\\100 Hz\\PVS 4\\',
        "ini": "2019-12-25T17:44:49",
        "end": "2019-12-25T18:08:38"
    },
    "pvs-5": {
        "description": "bravo-2",
        "folder": 'E:\\DataSets\\100 Hz\\PVS 5\\',
        "ini": "2019-12-25T18:17:05",
        "end": "2019-12-25T18:38:50"
    },
    "pvs-6": {
        "description": "bravo-3",
        "folder": 'E:\\DataSets\\100 Hz\\PVS 6\\',
        "ini": "2019-12-25T18:44:21",
        "end": "2019-12-25T18:59:57"
    },
    "pvs-7": {
        "description": "palio-1",
        "folder": 'E:\\DataSets\\100 Hz\\PVS 7\\',
        "ini": "2019-12-26T18:24:10",
        "end": "2019-12-26T18:45:09"
    },
    "pvs-8": {
        "description": "palio-2",
        "folder": 'E:\\DataSets\\100 Hz\\PVS 8\\',
        "ini": "2019-12-26T18:51:04",
        "end": "2019-12-26T19:11:17"
    },
    "pvs-9": {
        "description": "palio-3",
        "folder": 'E:\\DataSets\\100 Hz\\PVS 9\\',
        "ini": "2019-12-26T19:23:32",
        "end": "2019-12-26T19:38:31"
    },
}

######################################### CHANGE HERE #########################################

dataset = workspace['pvs-1']
# side = "left"
side = "right"

###############################################################################################

folder = dataset['folder']
ini_video = parseDateToTimestamp(dataset['ini'])
end_video = parseDateToTimestamp(dataset['end'])
data_file = os.path.join(folder, "dataset_gps_mpu_" + side + ".csv")
video_file = "video_dataset_" + side + ".mp4"
videos_folder = os.path.join(folder, "videos_" + side)
createFolder(videos_folder)