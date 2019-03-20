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
# A program to output a histogram of data from an input list of directories
#==============================================================================

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

#==============================================================================
# Read in data from files
#==============================================================================
# Read in configuration file
config_file = 'hist_paths.txt'
path_list = np.loadtxt(config_file, dtype=str, skiprows=1)

num_paths = path_list.shape[0] # set number of paths to be read from

# Declare empty array to fill with data for plotting
data = np.empty(0, dtype=float)

# Populate data array
for i in range(0, num_paths):
    # Create array of files to be read
    file_paths = np.array( sorted( Path(path_list[i,0]).glob('*.txt') ) )
    column = int(path_list[i,1]) -1

    # Read data
    for item in file_paths:
        content = np.loadtxt(item, dtype=str, usecols=column)
        data = np.append(data, content)

#==============================================================================
# Plot data as histogram
#==============================================================================
# Set parameters for histogram plot
fig, ax = plt.subplots() # set up figure and axes objects for plotting
num_bins = 20 # number of bins in histogram
hist_file = 'vel_hist.eps'

# Create histogram
n, bins, patches = ax.hist(data, num_bins, density=False)

# Plot histogram
ax.plot(bins)
ax.set_xlabel(r'Speed ($\mu$m/s)')
ax.set_ylabel('Number of Cells')
ax.set_title('Histogram of C.reinhardtii cell velocities')

fig.tight_layout() # tweak spacing to prevent ylabel clipping
plt.savefig(hist_file)

#EOF
