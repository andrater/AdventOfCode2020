with open("input.txt",'r') as fh:
     all_lines = fh.read()

timestamp = int(all_lines.split()[0])
busses = list(filter(lambda x : x != 'x', all_lines.split()[1].split(',')))
pairs = {}

#create a dictionary pair of the bus ID the soonest time after the timestamp
for times in busses:
     diff = (int(timestamp/int(times))+1)*int(times)
     pairs[times] = diff

smallest = (min(pairs.items(), key=lambda x: x[1]))
solution = (int(smallest[0]))*(smallest[1]-timestamp)

print(solution)
print(timestamp)