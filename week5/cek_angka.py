def cek_angka(a:int, b:int, c:int):
    if a == b or b == c or a == c:
        angka = False
    else:
        if a + b == c or b + c == a or a + c == b:
            angka = True
        else:
            angka = False
    return angka

print(cek_angka(2,3,5))
print(cek_angka(4,5,9))
print(cek_angka(3,3,6))