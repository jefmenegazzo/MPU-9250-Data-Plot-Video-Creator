[![GitHub](https://img.shields.io/github/license/Intelligent-Vehicle-Perception/MPU-9250-Data-Plot-Video-Creator)](LICENSE) 
![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/Intelligent-Vehicle-Perception/MPU-9250-Data-Plot-Video-Creator) 
![pypi](https://img.shields.io/pypi/v/pybadges.svg)
![versions](https://img.shields.io/pypi/pyversions/pybadges.svg)
![GitHub issues](https://img.shields.io/github/issues/Intelligent-Vehicle-Perception/MPU-9250-Data-Plot-Video-Creator) 

# MPU-9250 Data Plot Video Creator

This is an application that creates videos with a plot of the data sampled from the sensors of the MPU-9250 (accelerometer, gyroscope and magnetometer) and GPS data (speed). The libraries matplotlib and ffmpeg are used. To use the functionality, you need to download [ffmpeg](https://ffmpeg.org/download.html) and add to environment variables. Next, just configure the variables in **settings.py**:

- **dataset**: dataset to be plotted.
    - **folder**: folder where the data is.
    - **ini**: time the plot starts.
    - **end**: time the plot ends.
- **side**: side to be plotted (left or right).

After configuration, just run with the command:

```bash
python main.py
```