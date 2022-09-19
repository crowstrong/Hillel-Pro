def relief(data):
    y_start = None
    y_min = None
    d = None
    h = None
    y_prev = None
    for i in data:
        if y_prev != None:
            if data[i] <= y_prev:
                if y_start == None:
                    y_start = y_prev
                    y_min = y_prev
                    print("y_start", y_start)
                else:
                    if data[i] < y_min:
                        y_min = data[i]
            else:
                if y_start != None and data[i] >= y_start:
                    print("y_end", data[i])
                    h = y_start - y_min
                    # print("h", h)
                    if d == None or h > d:
                        d = h
                    y_start = None
        y_prev = data[i]
    return d


data = {1: 1,
        2: 2,
        3: 5,
        4: 6,
        5: 1,
        6: 2,
        7: 2,
        8: 3,
        9: 0,
        10: 1,
        11: 5,
        12: 6,
        13: 7,
        14: 5,
        15: 5,
        15.5: 7,
        16: 8,
        17: 8,
        18: 2,
        19: 0}

print(relief(data))
