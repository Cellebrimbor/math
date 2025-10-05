#==================================#
import pyfiglet
import os
import sympy as sp
import time
#==================================#
from mathematic import calculation
from paint_logic import draw_axis
#==================================#


print(pyfiglet.figlet_format("antany"))

while True:
    input_ = input('Введите функцию: y=')
    
    # Массив точек
    points = []
    for x in range(-26*11,26*11):
        try:
            points.append(calculation(input_, x/11))
        except:
            pass
    os.system('clear')
    draw_axis(const_mashtab=3, points=points, label_step=1) # построение графика
    ans = input("Для продолжения нажмите Enter или введите: exit. Чтобы ввести анимацию введите: Diff ")

    if ans == "exit":
        break

    # Анимация производной функции
    if ans == "Diff":
        x = sp.Symbol('x')
        func = sp.sympify(input_)
        diff_func = sp.diff(func) # производная функции

        for i in range(len(points)):
            if i % 25 == 0:
                point = points[i]
                # Уравнение прямой : y = f'(x0)*(x-x0)+f(x0)
                line_equation = calculation(diff_func, point[0])[1] * (x-point[0]) + calculation(func, point[0])[1]
                print(line_equation)
                points_of_line = [calculation(line_equation, i/150) for i in range(-26*150,26*150)]
                draw_axis(const_mashtab=3, points=points_of_line+points, label_step=1) # построение графика
                time.sleep(0.1)
                os.system('clear') # очищаем консоль
