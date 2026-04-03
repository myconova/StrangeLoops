# Theme: Dictionaries, sets, and frequency analysis
# Difficulty: Moderate
# Write a function that returns the number that appears most frequently in the list.
# if there is a tie, return the smallest number among those tied. 

# Solution A

from collections import Counter
input = list(map(int, input().split()))

def most_frequent(input):
    count = Counter(input)
    most_frequent = max(count.values())
    candidates = [k for k, v in count.items() if v == most_frequent]
    return min(candidates)
print(most_frequent(input))

# Solution B

input = list(map(int, input().split()))
def most_frequent(input):
    count = {}
    for i in input:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    most_frequent = max(count.values())
    candidates = [k for k, v in count.items() if v == most_frequent]
    return min(candidates)