import sys
import numpy as np

def to_binary_and_int(n):
    binary = bin(n)[2:]  # Convert to binary and remove the '0b' prefix
    return n, binary, int(binary, 2)

def main():
    num_numbers = int(sys.argv[1])
    lower_bound = int(sys.argv[2])
    upper_bound = int(sys.argv[3])

    for i in range(num_numbers):
        number = np.random.randint(lower_bound, upper_bound)
        n, binary, integer = to_binary_and_int(number)
        print(f"{i} {binary} {integer}")

if __name__ == "__main__":
    main()