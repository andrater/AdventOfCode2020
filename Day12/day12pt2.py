import os

with open("input.txt",'r') as fh:
     all_lines = fh.read()

#print(all_lines.split())

coordinates = [0,0]
waypoint = [10,1]
degreeDir = 90
manhattanDist = 0
line = 0

def waypointMove(rotation, waypoint):
    if rotation == "R":
        
        degreeDir = degreeDir + int(directions[1:])
        if degreeDir >= 360:
            degreeDir = degreeDir - 360
    elif directions[0] == "L":
        degreeDir = degreeDir - int(directions[1:])
        if degreeDir < 0:
            degreeDir = degreeDir + 360

def nav(degreeDir):
    # if direction is north
    #print(coordinates)
    if degreeDir == 0:
        # add movement to y axis
        coordinates[1] += int(directions[1:])
        waypoint[1] += int(directions[1:])
    # if direction is east
    elif degreeDir == 90:
        # add movement to x axis
        coordinates[0] += int(directions[1:])
        waypoint[0] += int(directions[1:])
    # if direction is south
    if degreeDir == 180:
        # subtract movement from y axis
        coordinates[1] -= int(directions[1:])
        waypoint[1] += int(directions[1:])
    # if direction is west
    elif degreeDir == 270:
        # subtract movement from x axis
        coordinates[0] -= int(directions[1:])
        waypoint[0] += int(directions[1:])
    #print(f"coordinates after {coordinates}")

for directions in all_lines.split():
    #print(int(directions[1:]))
    print(f"directions line{line}: {directions}")
    print(f"coordinates before transform: {coordinates}")
    if directions[0] == "R":
        degreeDir = degreeDir + int(directions[1:])
        if degreeDir >= 360:
            degreeDir = degreeDir - 360
    elif directions[0] == "L":
        degreeDir = degreeDir - int(directions[1:])
        if degreeDir < 0:
            degreeDir = degreeDir + 360

    if directions[0] == "N":
        waypoint[1] += int(directions[1:])
    elif directions[0] == "S":
        waypoint[1] -= int(directions[1:])
    elif directions[0] == "E":
        waypoint[0] += int(directions[1:])
    elif directions[0] == "W":
        waypoint[0] -= int(directions[1:])
    elif directions[0] == "F":
        for i in range(int(directions[1:])):
            nav(degreeDir)
    
    #print(f"degree direction {degreeDir}")
    #print(f"coordinates after {coordinates}")
    line += 1
    #print(coordinates)

manhattanDist = abs(coordinates[0]) + abs(coordinates[1])

print(manhattanDist)
print(abs(waypoint[0] + abs(waypoint[1])))
    # if degreeDir not in [0,90,180,270]:
    #     print("oddball")
    # else:
    #     print("its a cardinal direction")


#print(degreeDir)
# if degreeDir == 0:
#     cardinalDir = "North"
# elif degreeDir == 90:
#     cardinalDir = "East"
# elif degreeDir == 180:
#     cardinalDir = "South"
# elif degreeDir == 270:
#     cardinalDir = "West"
#print(cardinalDir)