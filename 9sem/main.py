l1 = ['1', '123', '123', '12', '1', '123']
l2 = [2, 4, -2, -3, 0 , 11 , 3 -1]
d4 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
d5 = {'a': 3, 'b': 4, 'c': 5, 'd': 6, 'e': 7, 'f': 8, 'g': 9}
d6 = {'e': 20, 'f': 21, 'g': 22, 'h': 23, 'i': 24, 'j': 25, 'k': 26, 'l': 27}


def n413(l1):
    new_l1 = [len(x) for x in l1]
    return new_l1


def n414(l1):
    n = sum(1 for i in l1 if len(i) > 2)
    return n


def n415(d4):
    out = sum(i * j for i, j in d4.items())
    return out


def n416(d6, d5):
    d7 = {i: j for i, j in d6.items() if i not in d5}
    return d7


def n417(l2):
    new_l2 = [(i + 1) * j if j is not None and i is not None else j for i, j in enumerate(l2)]
    return new_l2


def n418(l2):
    new_l2 = [i for i in l2 if i >= 0]
    return new_l2


def n419(l2):
    new_l2 = [i + 1 if j < 0 else j for i, j in enumerate(l2)]
    return new_l2


def n51(a, b):
    return a * b


def n52(*arg):
    n = 1
    for i in arg:
        n *= i
    return n


def n53(*arg):  #54
    result = 1
    for num in arg:
        result *= num
    return result


def n55_add(x, y):
    return x + y


def n55_sub(x, y):
    return x - y


def n55_mul(x, y):
    return x * y


def n55_div(x, y):
    return x / y


def n56(arg):
    a, znak, b = arg.split()
    a = int(a)
    b = int(b)
    if znak == '+':
        return a + b
    elif znak == '-':
        return a - b
    elif znak == '*':
        return a * b
    elif znak == '/':
        return a // b
    elif znak == '%':
        return a % b
    return a ** b


def n59(str):
    numbers = {
        'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6, 'семь': 7, 'восемь': 8,
        'девять': 9, 'десять': 10, 'одиннадцать': 11, 'двенадцать': 12, 'тринадцать': 13, 'четырнадцать': 14,
        'пятнадцать': 15, 'шестнадцать': 16, 'семнадцать': 17, 'восемнадцать': 18, 'девятнадцать': 19,
        'двадцать': 20, 'тридцать': 30, 'сорок': 40, 'пятьдесят': 50, 'шестьдесят': 60, 'семьдесят': 70,
        'восемьдесят': 80, 'девяносто': 90}
    parts = str.split()
    out = 0
    for i in parts:
        if i in numbers.keys():
            out += numbers[i]
    return out


print(n59('девяносто два'))