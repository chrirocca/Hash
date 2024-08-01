#include <iostream>
#include <vector>
#include <cmath>
#include <bitset>
#include <cstdlib>
#include <algorithm>
#include <unordered_map>
#include <cmath>

// Function to find the closest power of 2 greater than a number
int next_power_of_2(int n) {
    return pow(2, ceil(log2(n)));
}

// Function to find the closest power of 2 less than or equal to a number
int closest_power_of_2(int n) {
    return pow(2, floor(log2(n)));
}

// Function to reverse the bits of a number
int bit_reversal(int n, int num_bits) {
    int reversed_bits = 0;
    for (int i = 0; i < num_bits; ++i) {
        if ((n >> i) & 1) {
            reversed_bits |= 1 << (num_bits - 1 - i);
        }
    }
    return reversed_bits;
}

// Function to convert a number to its Gray code
int gray_code(int n) {
    return n ^ (n >> 1);
}

// Function to generate the initial pattern using bit reversal and Gray code
std::vector<int> generate_initial_pattern(int num_bits) {
    int size = 1 << num_bits;
    std::vector<int> pattern(size);
    for (int i = 0; i < size; ++i) {
        int reversed_n = bit_reversal(i, num_bits);
        int gray_n = gray_code(reversed_n);
        pattern[i] = gray_n;
    }
    return pattern;
}

// Function to swap elements in the pattern based on a given group size
std::vector<int> swap_pattern(const std::vector<int>& pattern, int group_size) {
    int size = pattern.size();
    std::vector<int> new_pattern = pattern;
    for (int i = 0; i < size; i += 2 * group_size) {
        for (int j = 0; j < group_size && i + group_size + j < size; ++j) {
            std::swap(new_pattern[i + j], new_pattern[i + group_size + j]);
        }
    }
    return new_pattern;
}

// Function to determine the maximum swap group size based on the number of bits
int max_swap_size(int num_bits) {
    return 1 << (num_bits - 1);
}

// Function to get the next pattern by applying different swaps based on the iteration
std::vector<int> get_next_pattern(std::vector<int>& previous_previous_pattern, std::vector<int>& previous_pattern, std::vector<int>& initial_pattern, std::vector<int>& base_pattern, std::vector<int>& power_2_base_pattern, int iteration, int max_size, int num_bits) {
    int group_size;
    std::vector<int> new_pattern;
    bool performed_swap_8 = false;

    if (iteration % 2 == 1) {
        group_size = 1;
    } else {
        int cycle_index = ((iteration / 2) - 1) % (1 << (num_bits - 2));
        group_size = 2 * (cycle_index + 1);
    }

    if ((group_size & (group_size - 1)) != 0) {
        int swap_size = 4;

        // Find the closest power of 2 that is smaller than group_size
        int start = closest_power_of_2(group_size);

        int next_power = next_power_of_2(group_size);
        int max_swap_size = (next_power - start) / 2;

        int swap_8_counter = 0; // Counter for performed_swap_8

        bool performed_swap_8 = false; // Assuming this flag is defined elsewhere

        for (int i = 0; i < group_size - start; i += 2) {
            if (i % 4 == 2) {
                if (swap_size == 8) {
                    if (performed_swap_8) {
                        if (swap_8_counter == 0) {
                            swap_size = 16;
                        } else {
                            swap_size = 16 * 2 *swap_8_counter;
                        }
                        new_pattern = swap_pattern(power_2_base_pattern, swap_size);
                        swap_8_counter++;
                        if (swap_size == max_swap_size) {
                            swap_8_counter = 0; // Reset counter if max swap size is reached
                            power_2_base_pattern = new_pattern;
                        }
                        base_pattern = new_pattern;
                        performed_swap_8 = false; // Reset flag after performing swap
                    } else {
                        // Swap base pattern with swap size of 8
                        new_pattern = swap_pattern(base_pattern, 8);
                        base_pattern = new_pattern;
                        performed_swap_8 = true; // Set flag after performing swap 8
                    }
                    swap_size = 4;
                } else {
                    // Swap base pattern with increasing swap size
                    new_pattern = swap_pattern(base_pattern, swap_size);
                    swap_size *= 2;
                }
            } else {
                // Swap previous pattern with fixed swap size of 2
                new_pattern = swap_pattern(previous_previous_pattern, 2);
            }
        }
        return new_pattern;
    }

    // Handle cases where group_size is a power of 2
    if (group_size == 1) {
        return swap_pattern(previous_pattern, group_size);
    } else {
        new_pattern = swap_pattern(initial_pattern, group_size);
        if (group_size == max_size) {
            initial_pattern = new_pattern;
        }
        if (group_size % 4 == 0) {
            base_pattern = new_pattern;
            power_2_base_pattern = base_pattern;
        }
        return new_pattern;
    }
}
// Cache to store precomputed patterns
std::unordered_map<int, std::vector<int>> pattern_cache;

// Function to precompute and cache the first 2^num_bits patterns
void precompute_patterns(int num_bits = 5) {
    int set_size = 1 << num_bits; // 2^num_bits
    int max_size = max_swap_size(num_bits);
    std::vector<int> initial_pattern = generate_initial_pattern(num_bits);
    std::vector<int> base_pattern;
    std::vector<int> current_pattern = initial_pattern;
    std::vector<int> previous_pattern;
    std::vector<int> pw_2_base_pattern;

    for (int i = 0; i < set_size; ++i) {
        pattern_cache[i] = current_pattern;
        if (i!=0) {
            previous_pattern = pattern_cache[i-1];
        }
        current_pattern = get_next_pattern(previous_pattern, current_pattern, initial_pattern, base_pattern, pw_2_base_pattern, i + 1, max_size, num_bits);
    }
}

// Hash function that uses the initial pattern and generates new patterns as needed
int hash_function(int n, int num_bits = 5, int repetition = 1) {
    int set_size = 1 << num_bits; // 2^num_bits
    int set_index = (n / set_size) / repetition;
    int position_in_set = n % set_size;

    // If the patterns are not precomputed, precompute them
    if (pattern_cache.empty()) {
        precompute_patterns(num_bits);
    }

    return pattern_cache[set_index%set_size][position_in_set];
}

// Main function to test the hash function
int main(int argc, char* argv[]) {
    if (argc < 6) {
        std::cerr << "Usage: " << argv[0] << " num_bits input_type test_size repetition start_point" << std::endl;
        std::cerr << "input_type: 0 for sequential, 1 for random" << std::endl;
        return 1;
    }

    int num_bits = std::atoi(argv[1]);
    int input_type = std::atoi(argv[2]);
    int test_size = std::atoi(argv[3]); // Get test_size from command line
    int repetition = std::atoi(argv[4]); // Get repetition from command line
    int start_point = std::atoi(argv[5]); // Get start_point from command line

    std::vector<int> inputs(test_size);
    if (input_type == 0) {
        for (int i = 0; i < test_size; ++i) {
            inputs[i] = i + start_point;
        }
    } else if (input_type == 1) {
        for (int i = 0; i < test_size; ++i) {
            inputs[i] = i + start_point;
        }
        std::random_shuffle(inputs.begin(), inputs.end());
    } else {
        std::cerr << "Invalid input_type. Use 0 for sequential, 1 for random." << std::endl;
        return 1;
    }

    std::vector<int> output_sequence(test_size);
    for (int i = 0; i < test_size; ++i) {
        output_sequence[i] = hash_function(inputs[i], num_bits, repetition);
    }

    // Print the output sequence
    for (int i = 0; i < test_size; ++i) {
        std::cout << inputs[i] << " " << std::bitset<8>(output_sequence[i]) << " " << output_sequence[i] << std::endl;
    }
    std::cout << std::endl;

    return 0;
}