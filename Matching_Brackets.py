def check_brackets(string: str) -> bool:
    brackets = {"{": "}", "(": ")", "[": "]"}
    queue = []
    for i in string:
        if i in brackets.keys():
            queue.append(i)
        elif i in brackets.values():
            if not queue:
                return False
            last_bracket = queue.pop()
            if brackets[last_bracket] != i:
                return False
    if queue:
        return False
    return True


if __name__ == '__main__':
    print(check_brackets("(a+[b*c]-{d/3})"))
    print(check_brackets("(a + [b * c) - 17]"))
    print(check_brackets("(((a * x) + [b] * y) + c"))
    print(check_brackets("auf(zlo)men [gy<psy>] four{s}"))






