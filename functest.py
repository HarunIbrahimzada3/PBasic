import turtle

# Функция для рисования координатных осей
def draw_axes():
    turtle.speed(0)  # Быстрое рисование
    turtle.penup()
    turtle.goto(-300, 0)  # Начало оси X
    turtle.pendown()
    turtle.goto(300, 0)  # Окончание оси X
    turtle.penup()
    turtle.goto(0, -300)  # Начало оси Y
    turtle.pendown()
    turtle.goto(0, 300)  # Окончание оси Y
    turtle.penup()

# Функция для рисования графика y = kx + b
def draw_graph(k, b):
    turtle.penup()
    scale = 50  # Масштаб оси, определяет как будет отображаться значение x и y

    # Печатаем точки от -300 до 300 на оси X
    for x in range(-300, 301):  # Берем значения x от -300 до 300
        y = k * x + b  # Вычисляем y по формуле
        # Масштабируем координаты для правильного отображения на экране
        turtle.goto(x * scale / 300, y * scale / 300)  # Масштабируем координаты X и Y
        turtle.pendown()  # Рисуем точку
        turtle.dot(5, "blue")  # Рисуем точку на графике
    turtle.penup()

# Основной код
def main():
    turtle.setup(600, 600)  # Устанавливаем размер окна
    turtle.bgcolor("white")  # Белый фон
    turtle.title("График функции y = kx + b")  # Название окна
    
    draw_axes()  # Рисуем оси

    k = float(input("Введите коэффициент k: "))  # Получаем коэффициент k
    b = float(input("Введите коэффициент b: "))  # Получаем коэффициент b

    draw_graph(k, b)  # Рисуем график функции y = kx + b

    turtle.done()  # Завершаем рисование

if __name__ == "__main__":
    main()
