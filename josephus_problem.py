def josephus(n: int, k: int) -> int:
    if n == 1:
        return 1
    else:
        return (josephus(n - 1, k) + k - 1) % n + 1


if __name__ == '__main__':
    print(josephus(79, 4))













