#Напишите декоратор, который проверял бы тип параметров функции, конвертировал их если надо и складывал:
def typed(data_type):
    def decorator(func):
        def wrapper(*args):
            for arg in args:
                if not type(arg) == float:
                    args = (data_type(arg) for arg in args)
                    return func(*args)
                else:
                    return func(*args)
        return wrapper
    return decorator


@typed(data_type=str)
def add_two_symbols(a, b):
    return a + b


print(add_two_symbols('3', 5))
print(add_two_symbols(5, 5))
print(add_two_symbols('a', 'b'))


@typed(data_type=int)
def add_three_symbols(a, b, c):
    return a + b + c


print(add_three_symbols(5, 6, 7))
print(add_three_symbols('3', 5, 0))
print(add_three_symbols(0.1, 0.2, 0.4))