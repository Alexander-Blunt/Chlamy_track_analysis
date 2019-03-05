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
output_file = input_file.replace('track', 'curvature')

# Read in the input file and get the number of points in the track
track = np.loadtxt(input_file, dtype='float')
num_points = track.shape[0]

#Initialise output array with column layout: time curvature
curvature = np.zeros( (num_points-2, 2) )

#========== Calculating curvature from track position coordinates =============#

# Function to calculate the tangent to the spiral at a point between x1, y1, z1
# and x2, y2, z2
def calc_tan( x1, x2, y1, y2, z1, z2 ):
   tan = np.array([x2-x1, y2-y1, z2-z1])
   ds = ( tan[0]**2 + tan[1]**2 + tan[2]**2 )**0.5
   tan /= ds
   return tan

# Function to calculate the curvature vector between tangents tan1 and tan2
def calc_curv( x1, x2, x3, y1, y2, y3, z1, z2, z3 ):
   tan1 = calc_tan(x1, x2, y1, y2, z1, z2)
   tan2 = calc_tan(x2, x3, y2, y3, z2, z3)

   # calculate which two points the tangent was calculated for
   x1 = (   track[i,4] + track[i+1,4] ) /2
   x2 = ( track[i+1,4] + track[i+2,4] ) /2
   y1 = (   track[i,5] + track[i+1,5] ) /2
   y2 = ( track[i+1,5] + track[i+2,5] ) /2
   z1 = (   track[i,6] + track[i+1,6] ) /2
   z2 = ( track[i+1,6] + track[i+2,6] ) /2

   # calculate distance along the curve and calculate curvature vector
   ds = ( (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2 )**0.5
   curv_vect = (tan2-tan1) /ds
   return curv_vect

for i in range(0, num_points-2):
   curv_vect = calc_curv(track[i,4], track[i+1,4], track[i+2,4], track[i,5],
                         track[i+1,5], track[i+2,5], track[i,6], track[i+1,6],
                         track[i+2,6])

   # calculate time and curvature scalar and store in curvature array
   curvature[i,0] = ( track[i,0] + 2*track[i+1,0] + track[i+2,0] ) /4 # time
   curvature[i,1] = ( curv_vect[0]**2 + curv_vect[1]**2 + curv_vect[2]**2 )**0.5

np.savetxt(output_file, curvature, fmt='%10.10g')

#EOF
