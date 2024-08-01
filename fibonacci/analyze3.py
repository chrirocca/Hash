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

# Split the data into sets at the blank lines
data_sets = []
current_set = []

for line in lines:
    if line.strip() == '':
        if current_set:
            data_sets.append(current_set)
            current_set = []
    else:
        current_set.append(line.strip())

if current_set:
    data_sets.append(current_set)

# Extract the inputs and outputs from the file
inputs_outputs = []
for data_set in data_sets:
    for line in data_set:
        parts = line.split()
        if parts:
            input_value = int(parts[0])
            output_value = int(parts[-1])  # Convert to integer
            inputs_outputs.append((input_value, output_value))

# Count the occurrences of each output
output_counts = defaultdict(int)
repetition_counts = defaultdict(lambda: defaultdict(int))

max_repetition_index = 0

for input_value, output_value in inputs_outputs:
    repetition_index = input_value // repetition
    output_counts[output_value] += 1
    repetition_counts[repetition_index][output_value] += 1

    # Keep track of the maximum repetition index
    max_repetition_index = max(max_repetition_index, repetition_index)

# Normalize the counts by the maximum repetition index
normalized_counts = {output: count / (max_repetition_index + 1) for output, count in output_counts.items()}

# Calculate average collisions per repetition
average_collisions = defaultdict(list)
for repetition_index, counts in repetition_counts.items():
    for output, count in counts.items():
        average_collisions[output].append(count)

average_collisions = {output: np.mean(counts) for output, counts in average_collisions.items()}

# Extract collisions for repetition_index = 0
collisions_repetition_0 = repetition_counts[0]

# Sort the outputs for consistent plotting
sorted_outputs = sorted(normalized_counts.keys())
normalized_counts_sorted = [normalized_counts[output] for output in sorted_outputs]
average_collisions_sorted = [average_collisions[output] for output in sorted_outputs]
collisions_repetition_0_sorted = [collisions_repetition_0.get(output, 0) for output in sorted_outputs]

# Plot overall normalized collisions
fig, ax = plt.subplots(figsize=(16/2.56, 16/2.56))
ax.bar(sorted_outputs, normalized_counts_sorted, color='grey')
ax.set_xlabel('Output')
ax.set_ylabel('Collisions')
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(1))
ax.set_ylim(0, 6)
plt.savefig('normalized_collisions.png')
plt.close(fig)

# Plot average collisions per repetition
fig, ax = plt.subplots(figsize=(16/2.56, 16/2.56))
ax.bar(sorted_outputs, average_collisions_sorted, color='grey')
ax.set_xlabel('Output')
ax.set_ylabel('Collisions')
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(1))
ax.set_ylim(0, 6)
plt.savefig('average_collisions.png')
plt.close(fig)

# Plot collisions for repetition_index = 0
fig, ax = plt.subplots(figsize=(16/2.56, 16/2.56))
ax.bar(sorted_outputs, collisions_repetition_0_sorted, color='grey')
ax.set_xlabel('Output')
ax.set_ylabel('Collisions')
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(1))
ax.set_ylim(0, 6)
plt.savefig('collisions_repetition_0.png')
plt.close(fig)
