import numpy as np




#     If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
#     If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.


with open("input.txt",'r') as fh:
     all_lines = fh.read()
    

print(all_lines)

cycles = 6
