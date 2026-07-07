
items = [(1, 4, 6), (2, 8, 12), (3, 3, 4), (4, 5, 3), (5, 9, 7),(6, 2, 1), (7, 3, 3), (8, 1, 2), (9, 5, 7), (10, 2, 3),(11, 4, 4), (12, 2, 2), (13, 7, 10), (14, 10, 13), (15, 3, 5),(16, 13, 16), (17, 11, 14), (18, 8, 9)]
KNAPSACK_CAPACITY = 45  
dp = [0] * (KNAPSACK_CAPACITY + 1)
chosen_history = [[] for _ in range(KNAPSACK_CAPACITY + 1)]
for item_id, weight, value in items:
    for w in range(KNAPSACK_CAPACITY, weight - 1, -1):      
        if dp[w - weight] + value > dp[w]:
            dp[w] = dp[w - weight] + value
            chosen_history[w] = chosen_history[w - weight] + [item_id]
best_value = dp[KNAPSACK_CAPACITY]
best_combination = chosen_history[KNAPSACK_CAPACITY]
print("最高の組み合わせ（番号）:", best_combination)
print("最高の値段:", best_value)