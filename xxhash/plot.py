import matplotlib.pyplot as plt
import numpy as np

# Read the data from the file
with open('result_32.txt', 'r') as f:
    lines = f.readlines()

# Print the data
#print("Data read from file:")
#print(''.join(lines))

# Split the data into two sets at the blank line
split_index = lines.index('\n')
data1 = lines[:split_index]
data2 = lines[split_index+1:]

# Function to process the data and plot
def process_and_plot(data, plot_number):
    y_values = []

    for line in data:
        values = line.split()
        y_values.append(float(values[-1]))

    # Use sequential x values
    x_values = list(range(len(y_values)))

    plt.figure(plot_number)
    plt.scatter(x_values, y_values)
    plt.title(f'Plot {plot_number}')
    plt.xlabel('X values')
    plt.ylabel('Y values')

    # Set ticks every 1
    plt.xticks(np.arange(min(x_values), max(x_values)+1, 2))
    plt.yticks(np.arange(min(y_values), max(y_values)+1, 1))

    # Save the plot to a file
    plt.savefig(f'plot_{plot_number}.png')

# Process the data and create the plots
process_and_plot(data1, 1)
process_and_plot(data2, 2)