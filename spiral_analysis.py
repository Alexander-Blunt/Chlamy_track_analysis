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

# A program to read in a track from a swimming cell and output the curvature as
#  a function of time.
import numpy as np

#==============================================================================
# Function to calculate the tangent to the spiral at a point between point1 and
# point2
#==============================================================================
def calc_tan( point1, point2 ):
    tan = point2 - point1
    distance = ( tan[0]**2 + tan[1]**2 + tan[2]**2 )**0.5
    tan /= distance
    return tan

#==============================================================================
# Function to calculate the curvature vector between tangents tan1 and tan2
#==============================================================================
def calc_curv( point1, point2, point3 ):
    tan1 = calc_tan(point1, point2)
    tan2 = calc_tan(point2, point3)

    # calculate which two points the tangent was calculated for
    tan_point1 = point2 - point1
    tan_point2 = point2 - point3

    # calculate distance along the curve and calculate curvature vector
    disp = tan_point2 - tan_point1 # displacement between points on the curve
    distance = ( disp[0]**2 + disp[1]**2 + disp[2]**2 )**0.5
    curv_vect = (tan2-tan1) / distance
    return curv_vect

#==============================================================================
# Function to read all points in a file and output the curvature to a new file
#==============================================================================
def output_curv( input_file ):
    output_file = input_file.replace('track', 'curvature')

    # Read in the input file and get the number of points in the track
    track = np.loadtxt(input_file, dtype='float')
    num_points = track.shape[0]

    #Initialise output array with column layout: time curvature
    curvature = np.zeros( (num_points-2, 2) )

    for i in range(0, num_points-2):
        curv_vect = calc_curv(track[i,3:], track[i+1,3:], track[i+2,3:])

        # calculate time and curvature scalar and store in curvature array
        curvature[i,0] = ( track[i,0] + 2*track[i+1,0] + track[i+2,0] ) /4
        curvature[i,1] =
                ( curv_vect[0]**2 + curv_vect[1]**2 + curv_vect[2]**2 ) **0.5

    # Output curvature array to file
    np.savetxt(output_file, curvature, fmt='%10.10g')

#EOF
