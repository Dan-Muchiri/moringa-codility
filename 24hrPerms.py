# Problem Description:

# Given four integers A, B, C, and D, representing the digits of a 24-hour clock, the task is to find all possible valid time combinations that can be formed using these digits. Each digit can only be used once, and a valid time combination consists of two digits forming the hour (between 0 and 23) and two digits forming the minute (between 0 and 59).

import itertools

def solution(A, B, C, D):
    def valid_time(hour, minute):
        return 0 <= hour < 24 and 0 <= minute < 60

    arr = [A, B, C, D]
    count = 0

    perms = set(itertools.permutations(arr))

    for perm in perms:
        hour = perm[0] * 10 + perm[1]
        minute = perm[2] * 10 + perm[3]
        if valid_time(hour, minute):
            count += 1

    return count

# Test cases
print(solution(1, 8, 3, 2))  # Output should be 6
print(solution(2, 3, 3, 2))  # Output should be 3
print(solution(6, 2, 4, 7))  # Output should be 0
print(solution(0, 0, 0, 0))  # Output should be 1
print(solution(1, 2, 3, 4))  # Output should be 10
print(solution(5, 5, 5, 5))  # Output should be 0
