def func1(x):
    return x + x


def func2(y):
    return y + y


def mapper(d, func1, func2):
    for i in d:
        yield (func1(i), func2(d[i]))


if __name__ == '__main__':
    d_1 = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
    for i in mapper(d_1, func1, func2):
        print(i)
