from util import parseDateToTimestamp, createFolder

#######################################################################################

# # Saveiro 1
# folder = 'E:\\Dados Processados\\100 Hz\\2019-12-24 17-21-12 - Saveiro Cenário 1\\'
# ini = "2019-12-24T17:21:14"
# end = "2019-12-24T17:43:48"

# Saveiro 2
folder = 'E:\\Dados Processados\\100 Hz\\2019-12-24 17-59-52 - Saveiro Cenário 2\\'
ini = "2019-12-24T17:59:54"
end = "2019-12-24T18:20:05"

#######################################################################################

# Data Selection
data_file = "dataset_gps_mpu_left.csv"
# data_file = "dataset_gps_mpu_right.csv"

# Video Settings
ini_video = parseDateToTimestamp(ini)
end_video = parseDateToTimestamp(end)
video_file = "dataset_left.mp4"
videos_folder = folder + "videos\\"
createFolder(videos_folder)