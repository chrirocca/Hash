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
        plt.ylim(0, 10)
        plt.gca().yaxis.set_major_locator(MultipleLocator(2))
        plt.gca().yaxis.set_minor_locator(MultipleLocator(1))

        # Add grids
        plt.grid(True)

        # Save the plot to a file with the specified dpi
        plt.savefig(f'frequency_outputs_{input_modulo}.png', dpi=600)

        # Close the figure
        plt.close()

# Process the data and create the plots
process_and_plot(data1)