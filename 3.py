# Theme: Linear-time filtering & structural contrast
# Difficulty: Moderate
# rewrite the two solutions from 2 with the following constraints:
    # you may not use collections.Counter
    # you may not sort the list
    # you may not use any library funtions that implicitly sort
    # you may use Python built-ins that operate in linear time 

# Solution A - O(n)

input = list(map(int, input().split()))
viewed = set()
solos = set()

for i in input:
    if i not in viewed:
        viewed.add(i)
        solos.add(i)
    else:
        solos.discard(i)

print(list(solos))


# Solution B - O(n)

input = list(map(int, input().split()))
viewed = set()
duplicates = set()

for i in input:
    if i in viewed:
        duplicates.add(i)
    else:
        viewed.add(i)

solos = [i for i in viewed if i not in duplicates]
print(solos)