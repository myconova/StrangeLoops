# Theme: Cyclic transformations and hidden symmetries
# Difficulty: Moderate
# You are given a string s consisting of letters, digits, and punctuation.
# Define a cyclic shift of a string as moving the last character to the front, or the first character to the end.
# A string is considered shift-stable if at least one of the following is true:
#1. After any number of left shifts, the string becomes a palindrome.
#2. After any number of right shifts, the string becomes a palindrome.
# Constraints: ignore non-alphanumberic characters; case insensitive; you may assume the string length after filtering is >= 1; you must not mutate the original string in place.


# Solution A

def is_shift_stable_a(s):
    filtered = ''.join(ch.lower() for ch in s if ch.isalnum())
    for shift in range(len(filtered)):
        candidate = filtered[shift:] + filtered[:shift]
        if candidate == candidate[::-1]:
            return True
    return False

    
# Solution B

def is_shift_stable_b(s):
    filtered = ''.join(ch.lower() for ch in s if ch.isalnum())

    n = len(filtered)
    if filtered == filtered[::-1]:
        return True

    for c in range(0, n):
        d = 0
        while d <= (n-1)//2:
            left = (c - d) % n
            right = (c + d) % n
            if filtered[left] != filtered[right]:
                break
            d += 1
        else:
            return True  

    for c in range(0, n):
        d = 0
        while d <= (n-1)//2:
            left = (c - d) % n
            right = (c + 1 + d) % n
            if filtered[left] != filtered[right]:
                break
            d += 1
        else:
            return True
    return False
        
    
        


