# bits of the output
bits=4
#inputs=81920
inputs=2048
random=0

# 0 for sequential inputs, 1 for random inputs
./try $bits $random $inputs  > result.txt
python3 plot.py $bits