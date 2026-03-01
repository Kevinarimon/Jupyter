try:
    bulan = int(input("Masukkan bulan (1-12): "))

    if bulan == 1:
        hari = 31
    elif bulan == 2:
        hari = 29   # Tahun 2020 adalah tahun kabisat
    elif bulan == 3:
        hari = 31
    elif bulan == 4:
        hari = 30
    elif bulan == 5:
        hari = 31
    elif bulan == 6:
        hari = 30
    elif bulan == 7:
        hari = 31
    elif bulan == 8:
        hari = 31
    elif bulan == 9:
        hari = 30
    elif bulan == 10:
        hari = 31
    elif bulan == 11:
        hari = 30
    elif bulan == 12:
        hari = 31
    else:
        print("Bulan tidak valid")
        exit()

    print("Jumlah hari:", hari)

except:
    print("Input tidak valid")