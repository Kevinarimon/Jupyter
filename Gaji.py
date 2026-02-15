# Program perhitungan pendapatan Budi

gaji_per_jam = eval(input("Masukkan gaji per jam: "))
jam_per_minggu = eval(input("Masukkan jumlah jam kerja per minggu: "))

# Total kerja 5 minggu
pendapatan_kotor = gaji_per_jam * jam_per_minggu * 5

# Pajak 14%
pajak = 0.14 * pendapatan_kotor
pendapatan_bersih = pendapatan_kotor - pajak

# Pengeluaran
baju = 0.10 * pendapatan_bersih
alat_tulis = 0.01 * pendapatan_bersih

# Sisa uang
sisa_uang = pendapatan_bersih - baju - alat_tulis

# Sedekah
sedekah = 0.25 * sisa_uang

# Pembagian sedekah
anak_yatim = 0.30 * sedekah
kaum_dhuafa = 0.70 * sedekah

print("1. Pendapatan sebelum pajak =", pendapatan_kotor)
print("2. Pendapatan setelah pajak =", pendapatan_bersih)
print("3. Uang untuk baju & aksesoris =", baju)
print("4. Uang untuk alat tulis =", alat_tulis)
print("5. Jumlah uang yang disedekahkan =", sedekah)
print("6. Untuk anak yatim =", anak_yatim)
print("7. Untuk kaum dhuafa =", kaum_dhuafa)