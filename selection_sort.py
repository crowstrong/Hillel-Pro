def selection_sort(data: str):
    list1 = data.split()
    mylist = []
    for i in list1:
        mylist.append(int(i))
    last = len(mylist)

    while last > 1:
        pos = 0
        temp = max(mylist)
        for i in range(0, last):
            if mylist[i] == temp:
                pos = i
                print(i)
        mylist[pos] = mylist[last - 1]
        mylist[last - 1] = temp
        mylist.pop()
        last -= 1


if __name__ == '__main__':
    print(selection_sort("31 41 59 26 53 58"))
