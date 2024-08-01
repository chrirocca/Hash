# bits of the output
bits=4
#inputs=81920
inputs=2048

RUSTFLAGS="-C target-cpu=native" cargo run $inputs $bits  > result.txt
#python3 plot.py $((bits+1))