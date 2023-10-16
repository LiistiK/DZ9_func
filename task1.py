num = int(input('Введите натуральное целое число: '))


def factorial(n):
    k = 1
    for i in range(n, 0, -1):
        k *= i
    return k


def list_f(f):
    return [factorial(i) for i in range(f, 0, -1)]


print(list_f(factorial(num)))