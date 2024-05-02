# Problem Explanation:

# The function solution(R, V) calculates the initial balance of two accounts (A and B) after a series of transactions represented by lists R (recipients) and V (values).

# Each transaction involves transferring money from one account to another. The recipient is either 'A' or 'B', and the value represents the amount of money transferred.

# The function returns the initial balances of accounts A and B.

# Assumptions:
# The lists R and V are equal.
# The only recipients are A and B.

def solution(R, V):
    A_balance = 0
    B_balance = 0

    for i in range(len(R)-1, -1, -1):
        print("Transaction:", i+1)
        print("Recipient:", R[i])
        print("Value:", V[i])
        if R[i] == 'A':
            A_balance += V[i]
            B_balance -= V[i]
        else:
            A_balance -= V[i]
            B_balance += V[i]
        print("Current Balance (A, B):", A_balance, B_balance)
        A_balance = max(A_balance, 0)
        B_balance = max(B_balance, 0)
        print("Updated Balance (A, B):", A_balance, B_balance)
        
    return [A_balance, B_balance]

# Test Case 1: Basic case
print(solution(['B', 'A', 'A', 'B', 'A'], [2, 4, 1, 1, 2]))  # Output should be [4, 2]

# # Test Case 2: Single transaction
# print(solution(['A'], [100]))  # Output should be [100, 0]

# # Test Case 3: No transactions
# print(solution([], []))  # Output should be [0, 0]

# # Test Case 4: All transactions for one recipient
# print(solution(['A', 'A', 'A'], [10, 5, 10]))  # Output should be [25, 0]

# # Test Case 5: All transactions for the other recipient
# print(solution(['B', 'B', 'B'], [10, 5, 10]))  # Output should be [0, 25]


