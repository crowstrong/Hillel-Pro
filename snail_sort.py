def snail(snail_map):
    snail_list = []
    while snail_map:
        snail_list.append(snail_map.pop(0))
        snail_map = list(map(list, zip(*snail_map)))[::-1]
        result = [j for i in snail_list for j in i]
    return result


if __name__ == '__main__':
    array = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
    expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert (snail(array) == expected)

    array = [[1, 2, 3],
             [8, 9, 4],
             [7, 6, 5]]
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert (snail(array) == expected)

    print("Done!")