# 0/1 Knapsack problem using recursive approach

def knapSack(W, wt, val, n):
    if n == 0 or W == 0:
        return 0
    if wt[n - 1] > W:
        return knapSack(W, wt, val, n - 1)
    else:
        return max(val[n - 1] + knapSack(W - wt[n - 1], wt, val, n - 1),
                   knapSack(W, wt, val, n - 1))

# Take user input for the number of items
n = int(input("\n Enter the number of items: "))

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