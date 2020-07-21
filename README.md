<div align="center">

[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://img.shields.io/badge/Project_Status-Active-green?style=flat-square&color=success)](https://github.com/Intelligent-Vehicle-Perception/MPU-9250-Data-Plot-Video-Creator)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg?style=flat-square&color=success)](https://github.com/Intelligent-Vehicle-Perception/MPU-9250-Data-Plot-Video-Creator)
[![GitHub](https://img.shields.io/github/license/Intelligent-Vehicle-Perception/MPU-9250-Data-Plot-Video-Creator?style=flat-square&color=success)](LICENSE)
![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/Intelligent-Vehicle-Perception/MPU-9250-Data-Plot-Video-Creator?style=flat-square) 
![pypi](https://img.shields.io/pypi/v/pybadges.svg?style=flat-square)
![versions](https://img.shields.io/pypi/pyversions/pybadges.svg?style=flat-square)

[![GitHub issues](https://img.shields.io/github/issues/Intelligent-Vehicle-Perception/MPU-9250-Data-Plot-Video-Creator?style=flat-square)](https://github.com/Intelligent-Vehicle-Perception/MPU-9250-Data-Plot-Video-Creator/issues)
[![GitHub forks](https://img.shields.io/github/forks/Intelligent-Vehicle-Perception/MPU-9250-Data-Plot-Video-Creator?style=flat-square)](https://github.com/Intelligent-Vehicle-Perception/MPU-9250-Data-Plot-Video-Creator/network/members)
[![GitHub stars](https://img.shields.io/github/stars/Intelligent-Vehicle-Perception/MPU-9250-Data-Plot-Video-Creator?style=flat-square)](https://github.com/Intelligent-Vehicle-Perception/MPU-9250-Data-Plot-Video-Creator/stargazers)
[![GitHub watchers](https://img.shields.io/github/watchers/Intelligent-Vehicle-Perception/MPU-9250-Data-Plot-Video-Creator?style=flat-square)](https://github.com/Intelligent-Vehicle-Perception/MPU-9250-Data-Plot-Video-Creator/watchers)
[![GitHub contributors](https://img.shields.io/github/contributors/Intelligent-Vehicle-Perception/MPU-9250-Data-Plot-Video-Creator?style=flat-square&color=success)](https://github.com/Intelligent-Vehicle-Perception/MPU-9250-Data-Plot-Video-Creator/graphs/contributors/)
[![HitCount](http://hits.dwyl.io/Intelligent-Vehicle-Perception/MPU-9250-Data-Plot-Video-Creator/badges.svg)](https://github.com/Intelligent-Vehicle-Perception/MPU-9250-Data-Plot-Video-Creator)

</div>

# MPU-9250 Data Plot Video Creator

This is an application that creates videos with data plotted in graph through the libraries matplotlib and ffmpeg. The plotted data correspond to samples from the sensors embedded in the module MPU-9250 (accelerometer, gyroscope and magnetometer) and GPS data (speed). 

## Table of Contents
- [Instalation](#Instalation)
- [How To Use](#How-To-Use)
- [Example](#Example)

## Instalation
 
First, clone this repository:

```bash
git clone https://github.com/Intelligent-Vehicle-Perception/MPU-9250-Data-Plot-Video-Creator.git
```

Next, you need to download [ffmpeg](https://ffmpeg.org/download.html) and add to environment variables. 

## How To Use

To generate the videos, first configure the variables in the file **settings.py**:

- **dataset**: dataset to be plotted.
    - **folder**: folder where the data is.
    - **ini**: time the plot starts.
    - **end**: time the plot ends.
- **side**: side to be plotted (left or right).

After configuration, run the following command to create the video:

```bash
python src/plot_video.py
```

Or run the following command to show live graph:

```bash
python src/plot_show.py
```

## Example

Below, an example of a frame from one of the generated videos.

<div align="center">
    <img src="./doc/signals.png" alt="Sensor Hardware Network" align="center"/>
</div>
