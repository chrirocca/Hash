import matplotlib.pyplot as plt
import numpy as np

# Read the data from the file
with open('result.txt', 'r') as f:
    lines = f.readlines()

# Split the data into four sets at the blank lines
split_index1 = lines.index('\n')
#split_index2 = lines[split_index1+1:].index('\n') + split_index1 + 1
#split_index3 = lines[split_index2+1:].index('\n') + split_index2 + 1
data1 = lines[:split_index1]
#data2 = lines[split_index1+1:split_index2]
#data3 = lines[split_index2+1:split_index3]
#data4 = lines[split_index3+1:]

def process_and_plot(data, plot_number):
    y_values = []

    for line in data:
        values = line.split()
        y_values.append(float(values[-1]))

    # Use sequential x values
    x_values = list(range(len(y_values)))

    # Create a new figure with the specified size (in inches)
    plt.figure(plot_number, figsize=(16/2.54, 16/2.54))  # Convert cm to inches

    plt.scatter(x_values, y_values)
    plt.title(f'Plot {plot_number}')
    plt.xlabel('X values')
    plt.ylabel('Y values')

    # Set ticks every 1
    plt.xticks(np.arange(min(x_values), max(x_values)+1, 8))
    plt.yticks(np.arange(min(y_values), max(y_values)+1, 1))

    # Save the plot to a file with the specified dpi
    plt.savefig(f'plot_{plot_number}.png', dpi=600)

# Process the data and create the plots
process_and_plot(data1, 1)
#process_and_plot(data2, 2)
#process_and_plot(data3, 3)
#process_and_plot(data4, 4)