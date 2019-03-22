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
# A program to read in tracks and output curvature and velocity to files.
#==============================================================================
import numpy as np
import spiral_analysis as sa
import velocity_calculation as vc
from pathlib import Path

#==============================================================================
# Read in the list of paths to search for tracks
#==============================================================================
path_list = 'path_list.csv'
in_path = np.loadtxt(path_list, dtype=str, delimiter=',', skiprows=1)

#==============================================================================
# Search paths for tracks
#==============================================================================
for i in range(0, in_path.size):
    # Create array of paths to be read from
    track_paths = np.array( sorted( Path(in_path[i]).glob('track*.txt') ) )

    # Create array to store output paths for each track
    out_path = np.empty(track_paths.shape, dtype=str)

    # Determine curvature output directory and create if it doesn't exist
    curv_dir = Path(in_path[i]).parent.parent.joinpath('curvature')
    Path(curv_dir).mkdir(parents=False, exist_ok=True)

    # Determine velocity output directory and create if it doesn't exist
    vel_dir = Path(in_path[i]).parent.parent.joinpath('velocity')
    Path(vel_dir).mkdir(parents=False, exist_ok=True)

    #==========================================================================
    # Output curvatures and velocities for all tracks in current path
    #==========================================================================
    for track in track_paths:
        track_name = Path(track).name
        file_name = track_name.replace('track', 'curv')
        out_path = Path(curv_dir).joinpath(file_name)

        # Calculate curvatures and output to file
        curvature = sa.output_curv(track)
        np.savetxt(Path(out_path), curvature, fmt='%10.10g')

        #Output velocities
        file_name = track_name.replace('track', 'velocity')
        out_path = Path(vel_dir).joinpath(file_name)

        # Calculate velocities and output to file
        velocity = vc.output_velocity(track)
        np.savetxt(Path(out_path), velocity, fmt='%10.10g')

#EOF
