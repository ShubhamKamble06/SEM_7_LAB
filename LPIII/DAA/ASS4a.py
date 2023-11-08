# 0/1 Knapsack problem using dynamic programming

def knapSack(W, wt, val, n):
    dp = [0 for _ in range(W + 1)]

    for i in range(1, n + 1):
        for w in range(W, 0, -1):
            if wt[i - 1] <= w:
                dp[w] = max(dp[w], val[i - 1] + dp[w - wt[i - 1]])

    return dp[W]

# Take user input for the number of items
n = int(input("Enter the number of items: "))

# Initialize empty lists for values and weights
val = []
wt = []

# Input values and weights from the user
for i in range(n):
    item_val = int(input(f"Enter the value of item {i + 1}: "))
    item_wt = int(input(f"Enter the weight of item {i + 1}: "))
    val.append(item_val)
    wt.append(item_wt)

# Take user input for the knapsack capacity
W = int(input("Enter the knapsack capacity: "))

# Call the knapSack function and print the result
result = knapSack(W, wt, val, n)
print("Maximum value that can be obtained:", result)