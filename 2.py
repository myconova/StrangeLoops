# Theme: Frequency maps & linear-time reasoning
# Difficulty: Moderate
# rewrite the two solutions from 1 so that each runs in linear time, O(n).

# Solution A - O(n)

import collections
input = list(map(int, input().split()))
output = collections.Counter(input)
output = [k for k, v in output.items() if v == 1]

print(output)

# Solution B - O(n)

input = list(map(int, input().split()))
output = [k for k, v in collections.Counter(input).items() if v == 1]

print(output)
