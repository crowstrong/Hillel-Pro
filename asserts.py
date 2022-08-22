import time


def new_format(string) -> str:
    out = [string[0]]
    for i in range(1, len(string)):
        if (len(string) - i) % 3 == 0:
            out.append('.')
        out.append(string[i])
    return ''.join(out)


if __name__ == '__main__':
    print(new_format("10000000000000000000"))
    print(type(new_format("10000000000000000000")))
    assert (new_format("1000000") == "1.000.000")
    assert (new_format("100") == "100")
    assert (new_format("1000") == "1.000")
    assert (new_format("100000") == "100.000")
    assert (new_format("10000") == "10.000")
    assert (new_format("0") == "0")
    print('SUCCESS!')


def custom_format(num) -> str:
    return "{:,}".format(num)


if __name__ == '__main__':
    print(custom_format(100000))
    print(type(custom_format(100000)))


if __name__ == '__main__':
    start = time.perf_counter()
    first = new_format("100000000000000000")
    end = time.perf_counter()
    print(end - start)

    start = time.perf_counter()
    second = custom_format(100000000000000000)
    end = time.perf_counter()
    print(end - start)




