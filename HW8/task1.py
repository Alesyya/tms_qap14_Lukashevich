# 1 Написать обычную функцию для факториала, генератор и рекурсию. Сравнить их время работы
import time


def decorator(func):
    def wrapper(a):
        start_time = time.time()
        result = func(a)
        print(time.time() - start_time)
        return result
    return wrapper

@decorator
def factorial(a):
    result = 1
    for i in range(1, a + 1):
        result *= i
    return result


print(factorial(5))

@decorator
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
        yield result


for f in factorial(5):
    print(f, end=' ')

@decorator
def factorial_recursive(n):
    if n == 1:
        return n
    else:
        return n*factorial_recursive(n-1)


print(factorial_recursive(7))