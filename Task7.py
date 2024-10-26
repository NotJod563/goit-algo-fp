import random
import matplotlib.pyplot as plt
from tabulate import tabulate

# Параметри симуляції
num_rolls = 1000000  # Кількість кидків кубиків
results = {i: 0 for i in range(2, 13)}  # Ініціалізація словника для підрахунку результатів

# Симуляція кидків двох кубиків
for _ in range(num_rolls):
    roll = random.randint(1, 6) + random.randint(1, 6)  # Обчислюємо суму двох кубиків
    results[roll] += 1  # Збільшуємо кількість випадків для цієї суми

# Обчислення ймовірностей
table_data = []
for sum_, count in results.items():
    probability = (count / num_rolls) * 100  # Переведення в проценти
    table_data.append([sum_, f"{probability:.2f}%", f"({count}/{num_rolls})"])

# Вивід результатів у вигляді таблиці
print(tabulate(table_data, headers=["Сума", "Ймовірність", "Частота"], tablefmt="grid"))

# Відображення ймовірностей на графіку
probabilities = [count / num_rolls * 100 for count in results.values()]  # Відсотки для графіка
plt.bar(results.keys(), probabilities, color='skyblue')
plt.xlabel('Сума')
plt.ylabel('Ймовірність (%)')
plt.title('Ймовірність випадіння суми двох кубиків за допомогою методу Монте-Карло')
plt.grid(axis='y')
plt.show()
