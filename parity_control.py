def check_char(number):
    bits = "{0:08b}".format(number)
    if int(bits[0]) == sum(map(int, bits[1:])) % 2:
        return number & 0x7f


def translate_line(line: str) -> str:
    ascii_codes = map(int, line.split())
    checked_values = [check_char(n) for n in ascii_codes]
    return "".join(chr(val) for val in checked_values if val)


if __name__ == '__main__':
    print(translate_line('65 238 236 225 46'))
