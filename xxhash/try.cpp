#include <iostream>
#include <bitset>
#include <sstream>
#include <cstdlib>
#include <ctime>
#include "xxhash.h"
#include <set>
#include <string>

std::pair<std::string, std::string> toBinaryAndInt(uint64_t n, int bitsetSize, int numBitsToShow) {
    std::bitset<64> binary(n);
    std::string binaryStr = binary.to_string();
    std::string mostSignificantBitsBinary = binaryStr.substr(0, numBitsToShow);

    std::bitset<64> mostSignificantBitsBitset(mostSignificantBitsBinary);
    std::stringstream ss;
    ss << mostSignificantBitsBitset.to_ulong();
    std::string mostSignificantBitsInt = ss.str();

    return {mostSignificantBitsBinary, mostSignificantBitsInt};
}

int main(int argc, char* argv[]) {
    uint64_t seed = 0;  // You can change the seed to any value you want
    srand(time(0));  // Initialize random number generator

    std::string hashType = "64";
    int numHashes = 32;
    int inputType = 0;  // 0 for sequential, 1 for random
    int numBitsToShow = 4;  // Number of bits of the hash to show

    if (argc > 1) {
        hashType = argv[1];
    }
    if (argc > 2) {
        numHashes = std::stoi(argv[2]);
    }
    if (argc > 3) {
        inputType = std::stoi(argv[3]);
    }
    if (argc > 4) {
        numBitsToShow = std::stoi(argv[4]);
    }

    if (inputType == 0) {
        // Sequential inputs
        for (int i = 0; i < numHashes; ++i) {
            uint64_t hash;
            if (hashType == "32") {
                hash = XXH32(&i, sizeof(i), seed);
            } else {
                hash = XXH3_64bits_withSeed(&i, sizeof(i), seed);
            }
            auto [binary, integer] = toBinaryAndInt(hash, hashType == "32" ? 32 : 64, numBitsToShow);
            std::cout << i << " " << binary << " " << integer << std::endl;
        }
    } else if (inputType == 1) {
        // Random inputs
        std::set<int> generatedNumbers;
        for (int i = 0; i < numHashes; ++i) {
            int randomInput = rand() % numHashes;  // Generate a random number between 0 and numHashes
            while (generatedNumbers.find(randomInput) != generatedNumbers.end()) {
                randomInput = rand() % numHashes;  // Generate a new number if the previous one was already generated
            }
            generatedNumbers.insert(randomInput);

            uint64_t hash;
            if (hashType == "32") {
                hash = XXH32(&randomInput, sizeof(randomInput), seed);
            } else {
                hash = XXH3_64bits_withSeed(&randomInput, sizeof(randomInput), seed);
            }
            auto [binary, integer] = toBinaryAndInt(hash, hashType == "32" ? 32 : 64, numBitsToShow);
            std::cout << randomInput << " " << binary << " " << integer << std::endl;
        }
    }

    return 0;
}