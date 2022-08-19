def decrypt_char(char: str, key: int):
    return chr(ord("A") + (ord(char) - ord("A") + 26 - key) % 26)


def decrypter(cipher: str, key: int) -> str:
    cipher = cipher.upper()
    message = ""
    for char in cipher:
        if char not in " ,.":
            message += decrypt_char(char, key)
        else:
            message += char
    return message


if __name__ == '__main__':
    print(decrypter("YHQL YLGL YLFL.", 3))
    print(decrypter("HYHQ BRX EUXWXV.", 3))
    print(decrypter("ZCJSGH HVCI AS DSHSF TCIF GQCFS OBR GSJSB MSOFG OUC.", 14))
    print(decrypter("KVC KOBHG HC ZWJS TCFSJSF.", 14))
    print(decrypter("ASH O KCAOB OH HVS KSZZ HC IG WB CZRSB GHCFWSG HVS GSQFSH CT VSOHVSF OZS.", 14))
    print(decrypter("OBR GC MCI HCC PFIHIG HVS CBQS OBR TIHIFS YWBU.", 14))
    print(decrypter("HVOH OZZ ASB OFS QFSOHSR SEIOZ.", 14))
    print(decrypter("O ROM OH HVS FOQSG QOZZSR WH HVS FWGWBU GIB.", 14))






