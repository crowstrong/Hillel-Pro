def sum_of_intervals(intervals):
    intervals.sort()
    result = []
    start, end = intervals[0][0], intervals[0][1]
    for i, interval in enumerate(intervals[1:]):
        s, e = interval[0], interval[1]
        if s > end:
            result.append([start, end])
            start, end = s, e
        else:
            end = max(e, end)
    result.append([start, end])

    answer = 0
    for s, e in result:
        answer += e - s
    return answer


if __name__ == '__main__':
    assert (sum_of_intervals([(1, 5)]) == 4)
    assert (sum_of_intervals([(1, 5), (6, 10)]) == 8)
    assert (sum_of_intervals([(1, 5), (1, 5)]) == 4)
    assert (sum_of_intervals([(1, 4), (7, 10), (3, 5)]) == 7)
    assert (sum_of_intervals([(-1_000_000_000, 1_000_000_000)]) == 2_000_000_000)
    assert (sum_of_intervals([(0, 20), (-100_000_000, 10), (30, 40)]) == 100_000_030)
    print("Done!")