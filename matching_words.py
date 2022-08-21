def matching_words(string: str):
    mylist = string.split()

    empty_list = []
    unique_list = []

    for i in mylist:
        if i not in empty_list:
            empty_list.append(i)
        else:
            unique_list.append(i)
    uni = list(set(unique_list))
    uni.sort()
    print(" ".join(uni))


if __name__ == '__main__':
    print(matching_words("nun lam mip tex bal pif sot bal bod tex end"))

