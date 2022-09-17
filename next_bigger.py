def next_bigger(n):
    digits = list(str(n))
    res = []
    while sorted(digits[1:], reverse=True) != digits[1:]:
        res.append(digits.pop(0))
    step = min(d for d in digits if d > digits[0])
    digits.remove(step)
    res += [step] + sorted(digits)
    return int(''.join(res))


if __name__ == '__main__':
    assert (next_bigger(12) == 21)
    assert (next_bigger(513) == 531)
    assert (next_bigger(2017) == 2071)
    assert (next_bigger(414) == 441)
    assert (next_bigger(144) == 414)
    print("Done!")
