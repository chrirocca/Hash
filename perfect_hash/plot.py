import matplotlib.pyplot as plt
import numpy as np
import argparse

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

def process_and_plot(data, plot_number):
    y_values = []

    for line in data:
        values = line.split()
        y_values.append(float(values[-1]))

    # Use sequential x values
    x_values = list(range(len(y_values)))

    # Create a new figure with the specified size (in inches)
    plt.figure(plot_number, figsize=(128/2.54, 16/2.54))  # Convert cm to inches

    plt.scatter(x_values, y_values)
    plt.title(f'Plot {plot_number}')
    plt.xlabel('X values')
    plt.ylabel('Y values')

    # Set ticks every 1
    plt.xticks(np.arange(min(x_values), max(x_values)+1, 8))
    plt.yticks(np.arange(min(y_values), max(y_values)+1, 1))

    # Highlight the y line for every 32 x tick
    for i in range(min(x_values), max(x_values)+1, repetition):
        plt.axvline(x=i, color='r', linestyle='--')

    # Print the value of the x value over the dot
    for i, txt in enumerate(x_values):
        plt.text(txt, y_values[i], str(txt % repetition), ha='center')

    # Add grids
    plt.grid(True)

    # Save the plot to a file with the specified dpi
    plt.savefig(f'plot_{plot_number}.png', dpi=600)

# Process the data and create the plots
process_and_plot(data1, 1)