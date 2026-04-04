# Theme: Functions, return values, and edge-case reasoning
# Difficulty: Moderate
# write a function that returns the index of the first charater in a 
# string that appears exactly once. If no such character exists, return -1.

# Solution A

input = map(str, input().split())

def first_unique_char(s):
    if not s:
        return None
    count = {}
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    for i, char in enumerate(s):
        if count[char] == 1:
            return input.index(i)
    return -1


# Solution B

from collections import Counter

input = map(str, input().split())

def first_unique_char(s):
    if not s:
        return None
    count = Counter(s)
    for i, char in enumerate(s):
        if count[char] == 1:
            return input.index(i)
    return -1

# Both solutions are incorrect.

# Revised Solution A

def first_unique_char(s: str) -> int:
    if not s:
        return -1
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for i, char in enumerate(s):
        if count[char] == 1:
            return i
    return -1


# Revised Solution B

from collections import Counter

def first_unique_char(s: str) -> int:
    if not s:
        return -1
    count = Counter(s)
    for i, char in enumerate(s):
        if count[char] == 1:
            return i)
    return -1