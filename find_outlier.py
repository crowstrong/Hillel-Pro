def find_outlier(integers):
    odds = [i for i in integers if i % 2 == 0]
    evens = [i for i in integers if i % 2]
    return evens[0] if len(odds) > len(evens) else odds[0]


if __name__ == '__main__':
    assert (find_outlier([2, 4, 6, 8, 10, 3]) == 3)
    assert (find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]) == 11)
    assert (find_outlier([160, 3, 1719, 19, 11, 13, -21]) == 160)

    print("Done!")
