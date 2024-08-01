# bits of the output
bits=4
#inputs=81920
inputs=2048
random=0
hash_type=64

# 0 for sequential inputs, 1 for random inputs
./try $hash_type $inputs $random $bits  > result.txt
#python3 plot.py $((bits+1))