#!/bin/bash

source /opt/ros/lyrical/setup.bash
source ./install/setup.bash
ros2 run reseq temperature_logger &
ros2 run reseq temperature_sensor &