#==================================#
import pyfiglet
import os
#==================================#
from mathematic import calculation
from paint_logic import draw_axis
#==================================#


print(pyfiglet.figlet_format("antany"))

while True:
    input_ = input('Введите функцию: y=')

    # Массив точек
    points = []
    for x in range(-100000,100000):
        try:
            points.append(calculation(input_, x/100))
        except:
            pass
    draw_axis(const_mashtab=3, points=points, label_step=1)
    if input("Для продолжения нажмите Enter или введите: exit ... ") == "exit":
        break

    os.system('clear')
