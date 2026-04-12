# Theme: Recursion, invariants, and the shape of thought
# Difficulty: Moderate
# You are given a list of strings. Each string may contain:
# - lowercase letters
# - uppercase letters 
# - spaces
# - punctuation
# - repeated characters
# - missing characters.
# Return True if all strings in the list reduce to the same normalized form, otherwise return False.
# You must produce two solutions, a clean, direct, procedural approach, and a structurally different approach.

# Solution A
import re

def normalize_string(strings):
    if not strings:
        return True
    normCheck = []
    for s in strings:
        collapsed = re.sub(r'(.)\1+', r'\1', s)
        normalized = ''.join(char for char in collapsed if char.isalpha()).lower()
        if normalized not in normCheck:
            normCheck.append(normalized)
    if len(normCheck) > 1:
        return False
    else:
        return True
    

# Solution B
import itertools

def normalize_string(strings):
    if not strings:
        return True
    normCheck = set()
    for s in strings:
        collapsed = ''.join(char for char, _ in itertools.groupby(s))
        normalized = ''.join(char for char in collapsed if char.isalpha()).lower()
        normCheck.add(normalized)
    return len(normCheck) == 1

# Both solutions are correct.
# Solution A uses regex to collapse repeated characters, then filters alpha characters, then lowercase. It tracks unique normalized forms in a list, a set would be more idiomatic.
# Solution B uses itertools.groupby to collapse repeated characters, then filters alpha characters, then lowercase. It tracks unique normalized forms in a set, which is more idiomatic.
# groupby is a classic Pythonic way to collapse consecutive duplicates. 
