# Theme: Arrays, Indexing, and the Shape of Data
# Difficulty: Easy
# You are given a list of integers nums. A list is considered index-stable if:
# For every index i, the value at nums[i] appears exactly once in the list segemnt from index 0 to index i.

# Write two distinct solutions to determine if the list index-stable.
# Solution A should a direct, brute-force approach.
# Solution B should use structural insight, avoid repeated scanning, must be stictly more efficient than A. 


# Solution A - O(n^2) 

def is_index_stable_a(nums):
    for i in range(len(nums)):
        if nums[i] in nums[:i]:
            return False
    return True


# Solution B - O(n)

def is_index_stable_b(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return False
        seen.add(num)
    return True


# Solution C - O(n log n)

def is_index_stable_c(nums):
    nums_copy = nums[:]
    nums_copy.sort()
    for i in range(1, len(nums_copy)):
        if nums_copy[i] == nums_copy[i - 1]:
            return False
    return True