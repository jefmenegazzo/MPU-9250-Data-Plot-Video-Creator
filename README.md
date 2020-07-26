[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://img.shields.io/badge/Project_Status-Active-green?style=flat-square&color=success)](https://github.com/Intelligent-Vehicle-Perception/MPU-9250-Data-Plot-Video-Creator)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg?style=flat-square&color=success)](https://github.com/Intelligent-Vehicle-Perception/MPU-9250-Data-Plot-Video-Creator)
[![GitHub](https://img.shields.io/github/license/Intelligent-Vehicle-Perception/MPU-9250-Data-Plot-Video-Creator?style=flat-square&color=success)](LICENSE)
![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/Intelligent-Vehicle-Perception/MPU-9250-Data-Plot-Video-Creator?style=flat-square) 
![pypi](https://img.shields.io/pypi/v/pybadges.svg?style=flat-square)
![versions](https://img.shields.io/pypi/pyversions/pybadges.svg?style=flat-square)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.3960614-blue?style=flat-square)](https://doi.org/10.5281/zenodo.3960614)
[![GitHub issues](https://img.shields.io/github/issues/Intelligent-Vehicle-Perception/MPU-9250-Data-Plot-Video-Creator?style=flat-square)](https://github.com/Intelligent-Vehicle-Perception/MPU-9250-Data-Plot-Video-Creator/issues)
[![GitHub forks](https://img.shields.io/github/forks/Intelligent-Vehicle-Perception/MPU-9250-Data-Plot-Video-Creator?style=flat-square)](https://github.com/Intelligent-Vehicle-Perception/MPU-9250-Data-Plot-Video-Creator/network/members)
[![GitHub stars](https://img.shields.io/github/stars/Intelligent-Vehicle-Perception/MPU-9250-Data-Plot-Video-Creator?style=flat-square)](https://github.com/Intelligent-Vehicle-Perception/MPU-9250-Data-Plot-Video-Creator/stargazers)
[![GitHub watchers](https://img.shields.io/github/watchers/Intelligent-Vehicle-Perception/MPU-9250-Data-Plot-Video-Creator?style=flat-square)](https://github.com/Intelligent-Vehicle-Perception/MPU-9250-Data-Plot-Video-Creator/watchers)
[![GitHub contributors](https://img.shields.io/github/contributors/Intelligent-Vehicle-Perception/MPU-9250-Data-Plot-Video-Creator?style=flat-square&color=success)](https://github.com/Intelligent-Vehicle-Perception/MPU-9250-Data-Plot-Video-Creator/graphs/contributors/)
[![HitCount](http://hits.dwyl.io/Intelligent-Vehicle-Perception/MPU-9250-Data-Plot-Video-Creator/badges.svg)](https://github.com/Intelligent-Vehicle-Perception/MPU-9250-Data-Plot-Video-Creator)

# MPU-9250 Data Plot Video Creator

This is an application that creates videos with data plotted in graph through the libraries matplotlib and ffmpeg. The plotted data correspond to samples from the sensors embedded in the module MPU-9250 (accelerometer, gyroscope and magnetometer) and GPS data (speed). 

## Table of Contents
- [Instalation](#Instalation)
- [How To Use](#How-To-Use)
- [Example](#Example)
- [How To Cite](#How-To-Cite)

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

To join videos side by side, we used the following command:

```bash
ffmpeg -i video1.mp4 -i video2.mp4 -filter_complex '[0:v]pad=iw*2:ih[int];[int][1:v]overlay=W/2:0[vid]' -map [vid] -c:v libx264 -crf 23 -preset veryfast output.mp4
```
<!-- 
ffmpeg -i video_environment.mp4 -i video_dataset_left.mp4 -filter_complex '[0:v]scale=iw*1.25:ih*1.25,pad=iw*2:ih[int];[int][1:v]overlay=W/2:0[vid]' -map [vid] -c:v libx264 -crf 23 -preset veryfast video_environment_dataset_left.mp4

ffmpeg -i video_environment.mp4 -i video_dataset_right.mp4 -filter_complex '[0:v]scale=iw*1.25:ih*1.25,pad=iw*2:ih[int];[int][1:v]overlay=W/2:0[vid]' -map [vid] -c:v libx264 -crf 23 -preset veryfast video_environment_dataset_right.mp4 -->

## How To Cite

To cite this repository, use the reference below:

```bibtex
@software{menegazzo3960614,
    author = {Jeferson Menegazzo and Aldo von Wangenheim},
    title = {{MPU-9250 Data Plot Video Creator}},
    month = jul,
    year = 2020,
    publisher = {Zenodo},
    version = {1.0.5},
    doi = {10.5281/zenodo.3960614},
    url = {https://github.com/Intelligent-Vehicle-Perception/MPU-9250-Data-Plot-Video-Creator}
}
```
