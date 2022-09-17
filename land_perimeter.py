def land_perimeter(arr):
    result = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == "X":
                result += 4
                if j > 0 and arr[i][j - 1] == "X":
                    result -= 2
                if i > 0 and arr[i - 1][j] == "X":
                    result -= 2

    return f"Total land perimeter: {result}"


if __name__ == '__main__':
    assert (land_perimeter(
        ["OXOOOX", "OXOXOO", "XXOOOX", "OXXXOO", "OOXOOX", "OXOOOO", "OOXOOX", "OOXOOO", "OXOOOO", "OXOOXX"]) ==
            "Total land perimeter: 60")
    assert (land_perimeter(
        ["OXOOO", "OOXXX", "OXXOO", "XOOOO", "XOOOO", "XXXOO", "XOXOO", "OOOXO", "OXOOX", "XOOOO", "OOOXO"]) ==
            "Total land perimeter: 52")
    assert (land_perimeter(["XXXXXOOO", "OOXOOOOO", "OOOOOOXO", "XXXOOOXO", "OXOXXOOX"]) ==
            "Total land perimeter: 40")
    assert (land_perimeter(["XOOOXOO", "OXOOOOO", "XOXOXOO", "OXOXXOO", "OOOOOXX", "OOOXOXX", "XXXXOXO"]) ==
            "Total land perimeter: 54")
    assert (land_perimeter(["OOOOXO", "XOXOOX", "XXOXOX", "XOXOOO", "OOOOOO", "OOOXOO", "OOXXOO"]) ==
            "Total land perimeter: 40")

    print("Done!")
