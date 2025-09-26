def draw_axis(const_mashtab=3, points=None, width=160, height=60, label_step=5):
    """
    Рисует ASCII-координатную систему.
    
    Параметры:
    - const_mashtab: шаг в символах между делениями осей (масштаб)
    - points: список точек [(x,y), (x,y,char)], где char — символ для точки
    - width, height: размер "экрана" в символах
    - label_step: подписывать каждое n-е деление осей
    """
    
    # Определяем центр экрана — это пересечение осей
    cx = width // 2
    cy = height // 2
    
    # Создаём пустой экран: двумерный массив символов
    screen = [[" " for _ in range(width)] for _ in range(height)]

    # Рисуем оси X и Y
    for x in range(width):
        screen[cy][x] = "_"  # горизонтальная ось X
    for y in range(height):
        screen[y][cx] = "|"  # вертикальная ось Y
    screen[cy][cx] = "+"  # точка пересечения осей

    # Сколько делений умещается по осям от центра
    x_extent = cx // const_mashtab
    y_extent = cy // const_mashtab

    # Рисуем деления и подписи на оси X
    for i in range(-x_extent, x_extent + 1):
        tx = cx + i * const_mashtab  # координата деления на экране
        if 0 <= tx < width:
            screen[cy][tx] = "|"  # вертикальная черточка деления
            # Подписываем деление, если оно кратно label_step и не в центре
            if i != 0 and i % label_step == 0 and cy + 1 < height:
                label = str(i)
                start = tx - len(label) // 2  # центрируем подпись
                for k, ch in enumerate(label):
                    pos = start + k
                    if 0 <= pos < width:
                        screen[cy + 1][pos] = ch  # выводим цифры под осью

    # Рисуем деления и подписи на оси Y
    for j in range(-y_extent, y_extent + 1):
        ty = cy - j * const_mashtab  # координата деления по Y
        if 0 <= ty < height:
            screen[ty][cx] = "_"  # горизонтальная черточка деления
            # Подписываем деление, если оно кратно label_step и не в центре
            if j != 0 and j % label_step == 0:
                label = str(j)
                left = cx - len(label) - 2  # сдвигаем подпись влево от оси
                if left < 0: left = 0
                for k, ch in enumerate(label):
                    pos = left + k
                    if 0 <= pos < width:
                        screen[ty][pos] = ch  # выводим цифры слева от оси

    # Рисуем точки на графике
    if points:
        for p in points:
            # Проверяем, что точка указана корректно
            if not (isinstance(p, (list, tuple)) and len(p) >= 2):
                continue
            x_raw, y_raw = p[0], p[1]  # координаты точки
            ch = p[2] if len(p) >= 3 else "#"  # символ для точки по умолчанию
            try:
                # Переводим координаты в экранные
                px = cx + int(round(float(x_raw) * const_mashtab))
                py = cy - int(round(float(y_raw) * const_mashtab))
            except Exception:
                continue
            # Проверяем, что точка в пределах экрана
            if 0 <= px < width and 0 <= py < height:
                screen[py][px] = str(ch)[0]  # ставим символ точки на экран

    # Выводим экран построчно
    for row in screen:
        print("".join(row))
