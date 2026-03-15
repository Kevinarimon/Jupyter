def ganjil(bawah, atas):
    if bawah < atas:
        for i in range(bawah + 1, atas):
            if i % 2 != 0:
                print(i, end = " ")
    else:
        for i in range(bawah, atas, -1):
            if i % 2 != 0:
                print(i, end = " ")
    print()

ganjil(10, 30)
ganjil(97, 82)