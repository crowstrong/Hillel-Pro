def bit_counter(num: int):
    counter = lambda x: (x + (1 << 32)) % (1 << 32)
    res = bin(counter(num))
    return res.count('1')


if __name__ == '__main__':
    print(bit_counter(1))
    print(bit_counter(100))
    print(bit_counter(-1))




