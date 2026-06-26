
items = [(1, 4, 6), (2, 8, 12), (3, 3, 4), (4, 5, 3), (5, 9, 7),(6, 2, 1), (7, 3, 3), (8, 1, 2), (9, 5, 7), (10, 2, 3),  (11, 4, 4), (12, 2, 2), (13, 7, 10), (14, 10, 13), (15, 3, 5),(16, 13, 16), (17, 11, 14), (18, 8, 9)]
KNAPSACK_CAPACITY = 45  
n = len(items)          
best_value = 0
best_combination = []
best_total_weight = 0
num_combinations = 2 ** n  
for i in range(num_combinations):
    current_weight = 0
    current_value = 0
    current_items = []   
    for j in range(n):
        if (i >> j) & 1:
            item_id, weight, value = items[j]
            current_weight += weight
            current_value += value
            current_items.append(item_id)    
    if current_weight <= KNAPSACK_CAPACITY:
        if current_value > best_value:
            best_value = current_value
            best_combination = current_items
            best_total_weight = current_weight
print("--- 探索結果 ---")
print("選ばれた品物の組み合わせ（番号）:", best_combination)
print("総値段（最大値）:", best_value)
print("総容量:", best_total_weight)