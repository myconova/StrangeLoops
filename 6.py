# Theme: Signal in the Noise 
# Difficulty: Moderate
# You are given a list of integers representing a noisy sensor stream.
# A signal is defined as any integer that appears more than n/3 times in the list.
# Return all such integers. 
# Constraints: you must produce two solutions. You may not sort. You may not use libraries that trivialize the problem. 
# Provide an explanation of each solution, and analyze their time and space complexity.

# Solution A

def find_signals(nums):
    if not nums:
        return []
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    signals = []
    for num, freq in count.items():
        if freq > len(nums) // 3:
            signals.append(num)
    return signals

# Solution B

def find_signals(nums):
    if not nums:
        return []
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    signals = []
    for num, freq in count.items():
        if freq > len(nums) // 3:
            signals.append(num)
    return signals

# explantion of solutions:
# Both solutions use a dictionary to count the frequency of each integer in the list.
# The first loop iterates through the list of integers and updates the count for each integer.  
# The second loop iterates through the dictionary of counts and checks if any integer appears more than n/3 times. If it does, it is added to the list of signals.  
# The time complexity of both solutions is O(n) because we iterate through the list of integers once to count the frequencies and then iterate through the dictionary of counts once to find the signals.
# The space complexity of both solutions is O(n) in the worst case, if all integers are unique, we would need to store the count for each integer in the dictionary.  
# 
# Line by Line Explanation:

'''
Solution A:
invoke a function "find_signals" that is passed the value "nums".
We test to ensure that nums contains values. If it does not, we return an empty list.
We initialize an empty dictionary to hold our counts while we loop. For each number, we store a key-value pair of the number and its count. Each time the number is found, the count increases by one. Then we initialize an empty list called "signals". For each number and its frequency from the count dictionary, we check if the frequency is greater than 1/3 the length of the list of numbers. If so, the number is appended to the signals list. Finally, the function returns the list of signals. 

Solution B
invoke a function "find_signals" that is passed the value "nums".
We test to ensure that nums contains values. If it does not, we return an empty list.
We initialize an empty dictionary called count to store key/value pairs of the number and the count. Then we run two sequential loops. First, for each number in nums, if it is in the count dictionary, increment its count by 1. If it is not in the dictionary, it is added, and its count is set to 1. Then we initialize an empty list called "signals". We run another sequential loop, first, for every number, checking its count. If its freq is greater than the len of nums divided by 3, the number is appended to the signals list. Finally, the signals list is returned.    
'''

# Solution A is correct. Solution B fails because it relies on syntax differences instead of algorithmic differences. 

# Revised Solution B - Hint Boyer-Moore Voting Approach

def find_signals(nums):
    if not nums:
        return []
    
    candidate1, count1 = None, 0
    candidate2, count2 = None, 0

    # identify candidates
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    # verify candidates
    count1, count2 = 0, 0
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1

    signals = []
    if count1 > len(nums) // 3:
        signals.append(candidate1)
    if count2 > len(nums) // 3:
        signals.append(candidate2)

    return signals


# Explanation of Revised Solution B:
# This solution uses the Boyer-Moore Voting Algorithm, which is an efficient way to find elements that appear more than n/3 times in a list.
# The algorithm works in two phases:    
# 1. Identify potential candidates for the majority element (those that appear more than n/3 times). We maintain two candidates and their counts.
# 2. Verify the candidates by counting their occurrences in the list.
# The time complexity of this solution is O(n) because we traverse the list a constant number of times (twice). The space complexity is O(1) because we only use a fixed amount of space for the candidates and their counts.

# Comparison / Constrast of both solutions:
# Solution A is a straightforward frequency map. It uses a dictionary to explicity count occurrences of every integer.
# The time complexity is O(n) because it performs one full pass to count and one pass to filter.
# The space complexity is O(n) in the worst case, since every distinct number must be stored.
# It directlys measures frequency rather than reasoning about structure. 

# Revised Solution B uses vote-cancellation instead of explicit counting.
# It maintains only two candidate slotes and two counters, giving it O(1) space.
# Time complexity is O(n) because it makes two linear passes. 
# Conceptually less intuitive: correctness relies on the invariant that any number appearing more than n/3 times 
# cannot be fully eliminated by pairwise cancellation.