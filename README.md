# MPU-9250 Data Plot Creator

This is an application that creates videos with a plot of the sampled signals from inertial sensors (MPU-9250). The libraries matplotlib and ffmpeg are used. To use the functionality, just configure the variables in **settings.py**:

- **dataset**: dataset to be plotted.
    - **folder**: folder where the data is.
    - **ini**: time the plot starts.
    - **end**: time the plot ends.
- **side**: side to be plotted (left or right).

After configuration, just run with the command:

```bash
python main.py
```