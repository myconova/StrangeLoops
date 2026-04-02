# Theme: Lists & reasoning about structure
# Difficulty: Small but rich
# given a list of integers, return a new list with the numbers that appear only once.

# Solution A

input = list(map(int, input().split()))
output = []

for i in range(1, len(input)):
    if input[i] not in output:
        output.append(input[i])

print(output)

# Solution B 

input = list(map(int, input().split()))
output = []

for i in input:
    if i not in output:
        output.append(i)

print(output)

# solutions A and B are both incorrect 

# revised solution A
input = list(map(int, input().split()))
output = []

for i in input:
    if input.count(i) == 1:
        output.append(i)

print(output)

# revised solution B
input = list(map(int, input().split()))
output = []

for i in range(0, len(input)):
    if input.count(input[i]) == 1:
        output.append(input[i])

print(output)
