with open("input.txt",'r') as fh:
     all_lines = fh.readlines()

map = []
tabogPos = []
trees = 0
right = 3
down = 1
i = 0

for line in all_lines:
    
    if i > 0:
        if i*right+1 < len(line):
            if line[i*right]+1 == '#':
                # print(f'line {i} {line[i*right]}')
                trees+=1
    print(f'line {i}')
    print(line.splitlines())
    
    i+=1

print(trees)