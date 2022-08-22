def palindrome(string: str) -> str:
    string_length = len(string)
    signs = " ,-?!"
    for sign in signs:
        string = string.lower().replace(sign, "")
    reverse = string[::-1]
    if string != reverse:
        return "N"
    return "Y"


if __name__ == '__main__':
    print(palindrome("Aektzuxyaurik-rviey e Ivrki, yuayxuztkea"))
    print(palindrome("Zk, xqs-Ruvjob-meoaeseuruurueseaoembovv Ursqxkz"))
    print(palindrome("Sbguqmpz-Dcumyve jan-ueovkykv, Oeunaje, v, Ym, U C dkpmq-ugbs"))
    print(palindrome("Oplqhxfea ekyolyiimmlrdydrlmmiiyloykerefxhqlp o"))
    print(palindrome("Uo Cekvooecx, Cagga-cxceoo-Vkecou"))
    print(palindrome("Qvtzgao, t, H Tejqo Yrcc-ryoqj-eth-toagztv-q"))
    print(palindrome("Rytexf Ssxjqssv-vzugew, oowegu, Zvvssqjss, Fx, Etyr"))
    print(palindrome("Ogy Hjiycyxdaxiqoavogibi g, ova, Oqixadxycyhjhygo"))
    print(palindrome("Onqxoioggre zeerg, goi, oxqn, O"))
    print(palindrome("Ai, uwidt, ow-mt-re, h uyyuher-t, Mwotiwui-A"))
    print(palindrome("H, x, aufi-T, ifuax-H"))
    print(palindrome("Ofzsyychpdq Fzfimkmrlnx-Qa-aqxnl, rmkmifzfqdphcyys Zfo"))
    print(palindrome("Otc Gupgs-Nriom, Oujeomrwtgpkk-Pgt-zr-moejuomoirnsgpugcto"))
    print(palindrome("Ukewybnayoxyjauaj Yxoygnby, Wek, u"))
    print(palindrome("Ehe Bxph-fcnkzzkncfh-Pxbehe"))
    print(palindrome("Lxhuib-yxaxu Eexaxyb-iuhxl"))
