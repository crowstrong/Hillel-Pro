relief_data = [1, 2, 5, 6, 1, 2, 2, 2, 3, 0, 1, 5, 6, 7, 5, 5, 7, 8, 8, 2, 0]


def relief(data: list) -> int:
    start = None
    end = None
    deep = None
    height = None
    prev = None
    for i in data:
        if prev != None:
            if i <= prev:
                if start == None:
                    start = prev
                    end = prev
                    # print("start", start)
                else:
                    if i < end:
                        end = i
            else:
                if start != None and i >= start:
                    # print("end", i)
                    height = start - end
                    if deep == None or height > deep:
                        deep = height
                    start = None
        prev = i
    return deep


if __name__ == '__main__':
    print(relief(relief_data))
