import cityhash
import sys

def to_binary_and_int(n, bitset_size):
    binary_str = format(n, '0{}b'.format(bitset_size))
    most_significant_bits_binary = binary_str[:bitset_size]
    most_significant_bits_int = int(most_significant_bits_binary, 2)
    return most_significant_bits_binary, most_significant_bits_int

def main():
    num_inputs = int(sys.argv[1])
    bitset_size = int(sys.argv[2])

    # Sequential inputs
    for i in range(num_inputs):
        hash = cityhash.CityHash32(str(i))
        binary, integer = to_binary_and_int(hash, bitset_size)
        print(i, binary, integer)

# Commented out the random inputs
# print()  # Print a new line

# Random inputs
# generated_numbers = set()
# for _ in range(33):
#     random_input = random.randint(0, 32)
#     while random_input in generated_numbers:
#         random_input = random.randint(0, 32)
#     generated_numbers.add(random_input)

#     hash = cityhash.CityHash32(str(random_input))
#     binary, integer = to_binary_and_int(hash, 32)
#     print(random_input, binary, integer)

if __name__ == "__main__":
    main()