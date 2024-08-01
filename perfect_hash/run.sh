# bits of the output
bits=8
repetition=1
inputs=65536
#inputs=819200
random=0

# 0 for sequential inputs, 1 for random inputs
./try $bits $random $inputs $repetition 0 > result.txt
#python3 plot.py $bits