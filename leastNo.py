# Problem Description:

# Given two arrays A and B of integers, the task is to find the smallest integer that appears in both arrays. If there is no such integer, return -1. 

def solution(A, B):
    A.sort()
    B.sort()
    i = 0
    for a in A:
        print("Current Element in A:", a)
        while i < len(B) and B[i] < a:      #if i < len(B) - 1 and B[i] < a: To iterate through all elements of array B that are less than the current element in array A.
            print("Current Element in B:", B[i])
            i += 1
        if  B[i] == a:       
            print("Common Integer Found:", a)
            return a
    print("No common integer found.")
    return -1

# # # Test Case 1: No common integer
# print(solution([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))
# # # Output: -1

# # # Test Case 2: Common integer in the middle
# print(solution([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]))
# # # Output: 4

# # # Test Case 3: Common integer at the beginning
# print(solution([1, 3, 5, 7, 9], [1, 2, 4, 6, 8]))
# # # Output: 1

# # # Test Case 4: Common integer at the end
print(solution([1, 3, 5, 7, 9], [2, 4, 6, 8, 9]))
# # # Output: 9

# # # Test Case 5: Arrays with negative integers
# print(solution([-5, -3, -1, 0, 1], [-4, -3, -2, -1, 0]))
# # # Output: -3



