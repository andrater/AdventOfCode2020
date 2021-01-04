import re

with open('input.txt', 'r') as fd:
    content = fd.read()
    lines = content.split("\n\n")
    input = [line.replace("\n", " ") for line in lines]

# Part 1
ValidTerms = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
ValidPassports = 0
for passport in input:
    if all(x in passport for x in ValidTerms):
        ValidPassports += 1

print("Part 1: The amount of valid passports is: " + str(ValidPassports))
