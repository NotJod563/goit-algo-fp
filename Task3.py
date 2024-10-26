import heapq

# Алгоритм Дейкстри
def dijkstra(graph, start):
    # Ініціалізуємо відстані як нескінченність для всіх вершин, крім початкової
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Пріоритетна черга (heap) для зберігання мінімальних відстаней до вершин
    priority_queue = [(0, start)]  # (відстань, вершина)

    while priority_queue:
        # Вибираємо вершину з найменшою відстанню
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо поточна відстань більше записаної, пропускаємо
        if current_distance > distances[current_vertex]:
            continue

        # Оновлення відстаней до сусідніх вершин
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Якщо нова відстань менша, оновлюємо і додаємо в чергу
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Створення графа у вигляді словника суміжності
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Запуск алгоритму Дейкстри для початкової вершини
start_vertex = 'A'
distances = dijkstra(graph, start_vertex)

# Виведення найкоротших відстаней від початкової вершини
print(f"Найкоротші відстані від вершини {start_vertex}:")
for vertex, distance in distances.items():
    print(f"Відстань до {vertex}: {distance}")
