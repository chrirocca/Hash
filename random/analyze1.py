import matplotlib.pyplot as plt
import numpy as np
import argparse
from collections import defaultdict
from matplotlib.ticker import MultipleLocator

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("repetition", help="The repetition value", type=int)
args = parser.parse_args()

# Calculate the repetition value
repetition = 2 ** args.repetition

# Read the data from the file
with open('result.txt', 'r') as f:
    lines = f.readlines()

# Split the data into four sets at the blank lines
split_index1 = lines.index('\n')
data1 = lines[:split_index1]

def process_and_plot(data):
    # Create a dictionary to store the frequency of each output
    frequency_dict = defaultdict(lambda: defaultdict(int))

    for line in data:
        values = line.split()
        output = int(float(values[-1]))  # Convert the output to an integer
        input_modulo = int(values[0]) % repetition
        frequency_dict[output][input_modulo] += 1

    # Create a plot for each output
    for plot_number, (output, input_modulo_dict) in enumerate(frequency_dict.items(), start=1):
        # Calculate the total number of inputs for this output for percentage calculation
        total_inputs = sum(input_modulo_dict.values())

        # Create lists for the x and y values
        x_values = []
        y_values = []

        for input_modulo, frequency in input_modulo_dict.items():
            x_values.append(input_modulo)
            y_values.append((frequency / total_inputs) * 100)

        # Create a new figure with the specified size (in inches)
        plt.figure(plot_number, figsize=(16/2.54, 16/2.54))  # Convert cm to inches

        plt.bar(x_values, y_values, color='grey', edgecolor='black')
        plt.title(f'Frequency of output {output}')
        plt.xlabel('Inputs')
        plt.ylabel('Frequency (%)')

        # Set ticks every 4 and subticks every 1 for x axis
        plt.gca().xaxis.set_major_locator(MultipleLocator(4))
        plt.gca().xaxis.set_minor_locator(MultipleLocator(1))

        # Set maximum y axis to 50%, and put a tick every 10% and subtick every 5%
        plt.ylim(0, 10)
        plt.gca().yaxis.set_major_locator(MultipleLocator(2))
        plt.gca().yaxis.set_minor_locator(MultipleLocator(1))

        # Add grids
        plt.grid(True)

        # Save the plot to a file with the specified dpi
        plt.savefig(f'frequency_inputs_{output}.png', dpi=600)

        # Close the figure
        plt.close()

    # Create a heatmap
    heatmap_data = np.zeros((max(frequency_dict.keys()) + 1, repetition))
    for output, input_modulo_dict in frequency_dict.items():
        for input_modulo, frequency in input_modulo_dict.items():
            heatmap_data[output][input_modulo] = (frequency / total_inputs) * 100

    plt.figure(figsize=(30/2.54, 16/2.54))  # Convert cm to inches
    im = plt.imshow(heatmap_data, cmap='hot', interpolation='nearest')
    plt.title('Heatmap of frequencies')
    plt.xlabel('Inputs')
    plt.ylabel('Outputs')

    # Set ticks every 1 for both x and y axes
    plt.gca().xaxis.set_major_locator(MultipleLocator(1))
    plt.gca().yaxis.set_major_locator(MultipleLocator(1))

    # Shift grid to separate the values
    plt.gca().set_xticks([x - 0.5 for x in plt.gca().get_xticks()][1:], minor='true')
    plt.gca().set_yticks([y - 0.5 for y in plt.gca().get_yticks()][1:], minor='true')

    # Add a grid
    plt.grid(True, which='minor', color='black', linewidth=1)

    # Add a colorbar
    cbar = plt.colorbar(im, label='Frequency (%)', orientation='horizontal')
    cbar.ax.tick_params(labelsize=6)  # Make colorbar labels smaller
    cbar.set_label('Frequency (%)', size=8)  # Reduce the size of the colorbar's label

    plt.savefig('heatmap.png', dpi=600)

# Process the data and create the plots
process_and_plot(data1)