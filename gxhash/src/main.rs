extern crate gxhash;
use std::collections::HashSet;
use rand::Rng;
extern crate crc;
use crc::{crc32, Hasher32};
extern crate blake3;
use std::convert::TryInto;
extern crate sha3;
use sha3::{Digest, Sha3_256};
use std::env;

fn to_binary_and_int(n: u32, num_bits_to_show: usize) -> (String, u32) {
    let binary_str = format!("{:032b}", n);
    let least_significant_bits_binary = &binary_str[0..num_bits_to_show];
    let least_significant_bits_int = u32::from_str_radix(least_significant_bits_binary, 2).unwrap();
    (least_significant_bits_binary.to_string(), least_significant_bits_int)
}

const GOLDEN_RATIO_32: u32 = 0x9E3779B9; // This is 2^32 / φ (the golden ratio)

fn fibonacci_hash(hash: u64) -> u32 {
    let shift_amount = 32;
    let hash = hash ^ (hash >> shift_amount);
    (11400714819323198485u64.wrapping_mul(hash) >> 32) as u32
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let max_input_size: u32 = args[1].parse().unwrap();
    let num_bits_to_show: usize = args[2].parse().unwrap();

    let seed = 0i64;
    let mut rng = rand::thread_rng();

    // Sequential inputs with gxhash
    for i in 0u32..max_input_size {
        let bytes = i.to_le_bytes();
        let hash = gxhash::gxhash32(&bytes, seed);
        let (binary, integer) = to_binary_and_int(hash, num_bits_to_show);  // Pass the hash directly
        println!("{} {} {}", i, binary, integer);
    }

    println!();  // Print a new line

/*     // Random inputs with gxhash
    let mut generated_numbers = HashSet::new();
    for _ in 0u32..=32 {
        let mut random_input: u32 = rng.gen_range(0..32);
        while generated_numbers.contains(&random_input) {
            random_input = if random_input >= 31 { 0 } else { random_input + 1 };
        }
        generated_numbers.insert(random_input);

        let bytes = random_input.to_le_bytes();
        let hash = gxhash::gxhash32(&bytes, seed);
        let (binary, integer) = to_binary_and_int(hash);  // Pass the hash directly
        println!("{} {} {}", random_input, binary, integer);
    }

    println!();  // Print a new line */

/*     // Sequential inputs with optimal 4-bit hash function
    for i in 0u64..=32 {
        let hash = fibonacci_hash(i);
        let (binary, integer) = to_binary_and_int(hash);  // Pass the hash directly
        println!("{} {} {}", i, binary, integer);
    } */

/*     println!();  // Print a new line */

/*     for i in 0u64..=32 {
        let bytes = i.to_le_bytes();
        let mut sha3_hasher = Sha3_256::new();  // Declare sha3_hasher as mutable
        sha3_hasher.input(&bytes);
        let sha3_hash = sha3_hasher.result();
        let hash_bytes = sha3_hash.as_slice();
        let binary: Vec<String> = hash_bytes.iter().map(|byte| format!("{:08b}", byte)).collect();
        let binary_string = binary.join("");
        let first_four_bits = &binary_string[..4];
        let int_value = u8::from_str_radix(first_four_bits, 2).unwrap();
        println!("{} {} {}", i, first_four_bits, int_value);
    }
    println!();  // Print a new line */

/*     // Random inputs with optimal 4-bit hash function
    let mut generated_numbers = HashSet::new();
    for _ in 0u64..=32 {
        let mut random_input: u64 = rng.gen_range(0..32);
        while generated_numbers.contains(&random_input) {
            random_input = if random_input >= 31 { 0 } else { random_input + 1 };
        }
        generated_numbers.insert(random_input);

        let hash = fibonacci_hash(random_input);
        let (binary, integer) = to_binary_and_int(hash);  // Pass the hash directly
        println!("{} {} {}", random_input, binary, integer);
    } */
}