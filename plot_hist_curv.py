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
# A program to output a histogram of curvature data from an input list of
# directories
#==============================================================================

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

#==============================================================================
# Function to plot data as histogram
#==============================================================================
# data = np.array of floats, out_file = string containing output file name
#==============================================================================
def plot_histogram( data, out_file, graph_title, x_label, y_label ):
    # Set parameters for histogram plot
    fig, ax = plt.subplots() # set up figure and axes objects for plotting

    # Automatically calculate bin edges
    bin_edges = np.histogram_bin_edges( data, bins='doane', 
                                  range=( np.nanmin(data),np.nanmax(data) ) )

    # Create histogram
    n, bins, patches = ax.hist(data, bin_edges, density=False,
                               edgecolor='black')

    # Set axis and graph titles
    ax.set_title(graph_title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    # Save graph to file
    plt.savefig(out_file)

#==============================================================================
# Read in data from files and plot histogram
#==============================================================================
# Read in configuration file
config_file = 'hist_config_curv.csv'
path_list = np.loadtxt(config_file, dtype=str, delimiter=',', skiprows=1, 
                       ndmin=2)

# Set number of paths to be read from
num_paths = path_list.shape[0]

# Declare empty array to fill with data for plotting
data = np.empty(0, dtype=float)

# Populate data array
for i in range(0, num_paths):
    # Create array of files to be read
    file_paths = np.array( sorted( Path(path_list[i,0]).glob('*.txt') ) )
    column = int(path_list[i,1]) -1

    # Read data
    for item in file_paths:
        content = np.loadtxt(item, dtype=float, usecols=column)
        data = np.append(data, content)

out_file = 'curv_hist(D).eps'
graph_title = ''
x_label = 'Curvature'
y_label = 'Number of Instances'

plot_histogram( data, out_file, graph_title, x_label, y_label )

#EOF
