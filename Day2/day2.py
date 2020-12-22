with open("input.txt",'r') as fh:
     all_lines = fh.readlines()

validCount = 0

for line in all_lines:
    minOcc = int(line.split(' ')[0].split('-')[0])
    maxOcc = int(line.split(' ')[0].split('-')[1])
    char = line.split(' ')[1][0]
    password = line.split(' ')[2].splitlines()[0]
    if password.count(char) >= minOcc and password.count(char) <= maxOcc:
        validCount += 1

print(validCount)

validCount = 0
for line in all_lines:
    pos1 = int(line.split(' ')[0].split('-')[0])-1
    pos2 = int(line.split(' ')[0].split('-')[1])-1
    char = line.split(' ')[1][0]
    password = line.split(' ')[2].splitlines()[0]
    if password[pos1] == password[pos2]:
        pass
    elif password[pos1] != char and password[pos2] == char:
        validCount += 1
    elif password[pos1] == char and password[pos2] != char:
        validCount += 1
    else:
        pass
print(validCount)