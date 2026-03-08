def cek_digit_belakang(a:int, b:int, c:int):

    d1 = a % 10
    d2 = b % 10
    d3 = c % 10

    if d1 == d2 or d1 == d3 or d2 == d3:
        return True
    else:
        return False


a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
c = int(input("Masukkan angka ketiga: "))

print(cek_digit_belakang(a,b,c))