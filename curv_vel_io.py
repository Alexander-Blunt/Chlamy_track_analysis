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

# A program to read in tracks and output curvature and velocity.

import numpy as np
import spiral_analysis as sa
from pathlib import Path

# Read in the list of paths to search for tracks
path_list = 'path_list.txt'
in_path = np.loadtxt(path_list, dtype=str, skiprows=1)

# Search paths for tracks
for i in range(0, in_path.size):
    track_paths = np.array(sorted(Path(in_path[i]).glob('track*.txt')))

    # Determine output path for curvature and velocity
    out_path = np.empty(track_paths.shape, dtype=str)

    # Determine output directory and create if it doesn't exist
    directory = Path(in_path[i]).parent.parent.joinpath('curvature')
    Path(directory).mkdir(parents=False, exist_ok=True)

    # Output curvatures for all tracks in current path
    for track in track_paths:
        file_name = Path(track).name
        file_name = file_name.replace('track', 'curv')
        out_path = Path(directory).joinpath(file_name)

        # Calculate curvatures and output to file
        curvature = sa.output_curv(track)
        np.savetxt(Path(out_path), curvature, fmt='%10.10g')

#EOF
