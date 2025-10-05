import math

def normalize_input(input_: str) -> str:
    '''Заменяет символы в исходной строке на другие, понятные питону'''
    input_ = input_.replace('^', '**')
    input_ = input_.replace(',', '.')
    return input_

def calculation(input_: str, x: float) -> list:
    ''' Подставляет конкретный х в выражение и 
    выдает пару [x,значение выражения] '''
    input_ = normalize_input(str(input_)) # обернем input_ в str чтобы избежать проблем при исп sympy
    input_ = input_.replace('x', '('+str(x)+')')
    safe_dict = {
        'abs': abs, 'max': max, 'min': min, 'pow': pow, 'round': round,
        'cos': math.cos, 'sin': math.sin, 'tan': math.tan,
        'acos': math.acos, 'asin': math.asin, 'atan': math.atan,
        'sqrt': math.sqrt, 'exp': math.exp, 'log': math.log, 'log10': math.log10,
        'pi': math.pi, 'e': math.e
    }

    safe_dict['__builtins__'] = None
    return (x, eval(input_, safe_dict))
