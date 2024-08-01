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
    # Create a dictionary to store the frequency of each input
    frequency_dict = defaultdict(lambda: defaultdict(int))

    for line in data:
        values = line.split()
        output = int(float(values[-1]))  # Convert the output to an integer
        input_modulo = int(values[0]) % repetition
        frequency_dict[input_modulo][output] += 1

    # Create a plot for each input
    for plot_number, (input_modulo, output_dict) in enumerate(frequency_dict.items(), start=1):
        # Calculate the total number of outputs for this input for percentage calculation
        total_outputs = sum(output_dict.values())

        # Create lists for the x and y values
        x_values = []
        y_values = []

        for output, frequency in output_dict.items():
            x_values.append(output)
            y_values.append((frequency / total_outputs) * 100)

        # Create a new figure with the specified size (in inches)
        plt.figure(plot_number, figsize=(16/2.54, 16/2.54))  # Convert cm to inches

        plt.bar(x_values, y_values, color='grey', edgecolor='black')
        plt.title(f'Frequency of input {input_modulo}')
        plt.xlabel('Outputs')
        plt.ylabel('Frequency (%)')

        # Set maximum y axis to 50%, and put a tick every 10% and subtick every 5%
        plt.ylim(0, 20)
        plt.gca().yaxis.set_major_locator(MultipleLocator(4))
        plt.gca().yaxis.set_minor_locator(MultipleLocator(2))

        # Add grids
        plt.grid(True)

        # Save the plot to a file with the specified dpi
        plt.savefig(f'frequency_outputs_{input_modulo}.png', dpi=600)

        # Close the figure
        plt.close()

    # Create a 2D numpy array for the heatmap data
    heatmap_data = np.zeros((max(frequency_dict.keys()) + 1, max(max(output_dict.keys()) for output_dict in frequency_dict.values()) + 1))

    for input_modulo, output_dict in frequency_dict.items():
        for output, frequency in output_dict.items():
            heatmap_data[input_modulo][output] = (frequency / sum(output_dict.values())) * 100

    # Create a new figure with the specified size (in inches)
    plt.figure(figsize=(30/2.54, 16/2.54))  # Convert cm to inches

    # Create the heatmap
    im = plt.imshow(heatmap_data, cmap='hot', interpolation='nearest')

    plt.title('Heatmap of frequencies')
    plt.xlabel('Outputs')
    plt.ylabel('Inputs')

    # Set ticks every 1 for both x and y axes
    plt.gca().xaxis.set_major_locator(MultipleLocator(1))
    plt.gca().yaxis.set_major_locator(MultipleLocator(1))

    # Shift grid to separate the values
    plt.gca().set_xticks([x - 0.5 for x in plt.gca().get_xticks()][1:], minor='true')
    plt.gca().set_yticks([y - 0.5 for y in plt.gca().get_yticks()][1:], minor='true')

    # Add a grid
    plt.grid(True, which='minor', color='black', linewidth=1)

    # Add a colorbar
    cbar = plt.colorbar(im, label='Frequency (%)', orientation='vertical')
    cbar.ax.tick_params(labelsize=6)  # Make colorbar labels smaller
    cbar.set_label('Frequency (%)', size=8)  # Reduce the size of the colorbar's label

    # Save the heatmap to a file with the specified dpi
    plt.savefig('heatmap2.png', dpi=600)

    # Close the figure
    plt.close()
   

# Process the data and create the plots
process_and_plot(data1)