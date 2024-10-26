import turtle
import math

def draw_tree(t, branch_length, level):
    if level == 0:
        return

    # Намалювати основну гілку
    t.forward(branch_length)

    # Повороти і довжина для нових гілок
    angle = 45
    new_length = branch_length * math.sqrt(2) / 2

    # Ліва гілка
    t.left(angle)
    draw_tree(t, new_length, level - 1)
    t.right(angle)  # Повернутися до початкового кута

    # Права гілка
    t.right(angle)
    draw_tree(t, new_length, level - 1)
    t.left(angle)  # Повернутися до початкового кута

    # Повернутися до початкової точки
    t.backward(branch_length)

# Ініціалізація Turtle
def draw_pythagoras_tree(level):
    screen = turtle.Screen()
    screen.title("Дерево Піфагора")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.color("brown")
    t.left(90)  # Повернути на 90 градусів для початку малювання

    # Початкова довжина гілки
    initial_length = 100
    draw_tree(t, initial_length, level)

    screen.mainloop()

# Запитати у користувача рівень рекурсії
level = int(input("Введіть рівень рекурсії для дерева Піфагора: "))
draw_pythagoras_tree(level)
