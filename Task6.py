import sys
from tabulate import tabulate

# Дані про їжу
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Жадібний алгоритм
def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    total_calories = 0
    chosen_items = []

    for item, info in sorted_items:
        if info["cost"] <= budget:
            chosen_items.append(item)
            total_calories += info["calories"]
            budget -= info["cost"]

    return chosen_items, total_calories

# Динамічне програмування
def dynamic_programming(items, budget):
    dp = [0] * (budget + 1)
    chosen_items_tracker = [[] for _ in range(budget + 1)]

    for item, info in items.items():
        item_cost = info["cost"]
        item_calories = info["calories"]
        for current_budget in range(budget, item_cost - 1, -1):
            if dp[current_budget - item_cost] + item_calories > dp[current_budget]:
                dp[current_budget] = dp[current_budget - item_cost] + item_calories
                chosen_items_tracker[current_budget] = chosen_items_tracker[current_budget - item_cost] + [item]

    max_calories = dp[budget]
    chosen_items = chosen_items_tracker[budget]
    return chosen_items, max_calories

# Запит бюджету у користувача
try:
    budget = int(input("Введіть ваш бюджет: "))
    if budget <= 0:
        print("Бюджет повинен бути більше 0.")
        sys.exit()
except ValueError:
    print("Будь ласка, введіть ціле число.")
    sys.exit()

# Виконання жадібного алгоритму
greedy_items, greedy_calories = greedy_algorithm(items, budget)

# Виконання алгоритму динамічного програмування
dp_items, dp_calories = dynamic_programming(items, budget)

# Виведення результатів у вигляді таблиці
table_data = [
    ["Жадібний алгоритм", ", ".join(greedy_items), greedy_calories],
    ["Динамічне програмування", ", ".join(dp_items), dp_calories]
]

print(tabulate(table_data, headers=["Метод", "Вибрані страви", "Сумарна калорійність"], tablefmt="pretty"))
