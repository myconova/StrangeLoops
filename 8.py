# Theme: structural reasoning, invariants, and pattern detection
# Difficulty: Easy
# Your task is to determine whether each string in a list is a mirror-symmetric string.
# irror Rules: A string is mirror-symmetric if it reads the same forwards and backwards, ignoring non-alphabetic characters
# You are given the following mapping:
# - 'A' <-> 'A'
# - 'H' <-> 'H'
# - 'I' <-> 'I'
# - 'M' <-> 'M'
# - 'O' <-> 'O'
# - 'T' <-> 'T'
# - 'U' <-> 'U'
# - 'V' <-> 'V'
# - 'W' <-> 'W'
# - 'X' <-> 'X'
# - 'Y' <-> 'Y'
# - 'b' <-> 'd'
# - 'p' <-> 'q'


# Write a function that, for each string in the list, returns True or False depending on whether it is mirror-symmetric.

# Solution A

def is_mirror_symmetric(s: str) -> bool:
    mirror_map = {
        'A': 'A', 'H': 'H', 'I': 'I', 'M': 'M', 'O': 'O',
        'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X',
        'Y': 'Y', 'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'
    }

    filtered = ''.join(char for char in s if char.isalpha())
    
    if not all(ch in mirror_map for ch in filtered):
        return False
    
    return all(
        mirror_map[left] == right
        for left, right in zip(filtered, reversed(filtered))
    )
   

# Solution B
def is_mirror_symmetric_two_pointer(s: str) -> bool:
    mirror_map = {
        'A': 'A', 'H': 'H', 'I': 'I', 'M': 'M', 'O': 'O',
        'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X',
        'Y': 'Y', 'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'
    }

    filtered = ''.join(ch for ch in s if ch.isalpha())

    for ch in filtered:
        if ch not in mirror_map:
            return False

    left, right = 0, len(filtered) - 1
    while left < right:
        if mirror_map[filtered[left]] != filtered[right]:
            return False
        left += 1
        right -= 1

    return True

# for both

def check_all(strings: list, fn) -> list:
    return [fn(s) for s in strings]
        