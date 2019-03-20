#==============================================================================
#                     Copyright 2019 Alex Blunt
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#==============================================================================
# A program to read in a track from a swimming cell and output its velocity and
#  speed as a function of time.
#==============================================================================
import numpy as np

#==============================================================================
# Function to calculate speed in 1 dimension from input positions and times
#==============================================================================
def calc_speed(time1,time2,pos1,pos2):
    distance = pos2-pos1
    time = time2-time1
    speed = distance/time
    return speed

#==============================================================================
# Function to output speed data to file
#==============================================================================
def output_velocity( input_file )
    # Read in the input file, and get the number of points in the track
    track = np.loadtxt(input_file)
    num_points = track.shape[0]

    # Initialise output array column layout: time vx vy vz speed
    velocity = np.zeros( ((num_points-1),5) )

    for i in range(0,num_points-1):
        velocity[i,0] = (track[i,0] + track[i+1,0])/2 # calculate time
        for j in range(1,4): # Find speed in each direction from splined track
            velocity[i,j] = calc_speed(track[i,0],track[i+1,0],track[i,j+3],
                                       track[i+1,j+3])
        velocity[i,4] = 
                (velocity[i,1]**2 + velocity[i,2]**2 + velocity[i,3]**2)**0.5

    return velocity
#EOF
