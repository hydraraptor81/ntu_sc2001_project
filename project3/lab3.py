def unbounded_knapsack(C, weights, profits):
    n = len(weights)
    dp = [0] * (C + 1)
    
    for c in range(1, C+1):
        for i in range(n):
            if weights[i] <= c:
                dp[c] = max(dp[c], dp[c - weights[i]] + profits[i])
    return dp

# (4a) Example: wi = [4,6,8], pi = [7,6,9], C = 14
weights1 = [4, 6, 8]
profits1 = [7, 6, 9]
C1 = 14
dp1 = unbounded_knapsack(C1, weights1, profits1)
print("P(14) with weights [4,6,8], profits [7,6,9]:", dp1[C1])
print("DP table:", dp1)

# (4b) Example: wi = [5,6,8], pi = [7,6,9], C = 14
weights2 = [5, 6, 8]
profits2 = [7, 6, 9]
C2 = 14
dp2 = unbounded_knapsack(C2, weights2, profits2)
print("P(14) with weights [5,6,8], profits [7,6,9]:", dp2[C2])
print("DP table:", dp2)
