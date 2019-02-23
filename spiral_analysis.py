#==============================================================================#
#                     Copyright 2019 Alex Blunt                                #
#                                                                              #
#   Licensed under the Apache License, Version 2.0 (the "License");            #
#   you may not use this file except in compliance with the License.           #
#   You may obtain a copy of the License at                                    #
#                                                                              #
#       http://www.apache.org/licenses/LICENSE-2.0                             #
#                                                                              #
#   Unless required by applicable law or agreed to in writing, software        #
#   distributed under the License is distributed on an "AS IS" BASIS,          #
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.   #
#   See the License for the specific language governing permissions and        #
#   limitations under the License.                                             #
#==============================================================================#

# A program to read in a track from a swimming cell and output the curvature as
#  a function of time.
import numpy as np

input_file = 'track350_1.txt'
output_file = input_file.replace('track','curvature')

# Read in the input file, and get the number of points in the track
track = np.loadtxt(input_file)
num_points = track.shape[0]

#Initialise output array column layout: time curvature
curvature = np.zeros( ((num_points-1),2 )

# Function to calculate curvature from input splined x y z positions

np.savetxt(output_file,curvature,fmt='%10.10g')

#EOF
