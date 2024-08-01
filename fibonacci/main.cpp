#include <iostream>
#include <vector>
#include <bitset>
#include <algorithm>
#include <cstdlib>

// Fibonacci hash function
size_t fibonacci_hash(size_t key, int num_bits) {
    // Shift amount
    size_t shift_amount = 64 - num_bits;

    // Hash calculation
    key ^= key >> shift_amount;
    return (11400714819323198485llu * key) >> shift_amount;
}
// Main function to test the hash function
int main(int argc, char* argv[]) {
    if (argc < 4) {
        std::cerr << "Usage: " << argv[0] << " num_bits input_type test_size" << std::endl;
        std::cerr << "input_type: 0 for sequential, 1 for random" << std::endl;
        return 1;
    }

    int num_bits = std::atoi(argv[1]);
    int input_type = std::atoi(argv[2]);
    int test_size = std::atoi(argv[3]); // Get test_size from command line

    std::vector<int> inputs(test_size);
    if (input_type == 0) {
        // Sequential inputs
        for (int i = 0; i < test_size; ++i) {
            inputs[i] = i;
        }
    } else if (input_type == 1) {
        // Random inputs
        for (int i = 0; i < test_size; ++i) {
            inputs[i] = i;
        }
        std::random_shuffle(inputs.begin(), inputs.end());
    } else {
        std::cerr << "Invalid input_type. Use 0 for sequential, 1 for random." << std::endl;
        return 1;
    }

    std::vector<int> output_sequence(test_size);
    for (int i = 0; i < test_size; ++i) {
        output_sequence[i] = fibonacci_hash(inputs[i], num_bits);
    }

    // Print the output sequence
    for (int i = 0; i < test_size; ++i) {
        std::cout << inputs[i] << " " << std::bitset<8>(output_sequence[i]) << " " << output_sequence[i] << std::endl;
    }
    std::cout << std::endl;

    return 0;
}