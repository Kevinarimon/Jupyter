data = ("Kevin Ariel Solomon", "71251208", "Jogja, DI Yogyakarta")

nama, nim, alamat = data

print("NIM :", nim)
print("NAMA :", nama)
print("ALAMAT :", alamat)
print()

nim_tuple = tuple(nim)
print("NIM:", nim_tuple)

nama_depan = nama.split()[0] 
nama_depan_tuple = tuple(nama_depan.lower())
print("NAMA DEPAN:", nama_depan_tuple)


nama_terbalik = tuple(nama.split()[::-1])
print("NAMA TERBALIK:", nama_terbalik)


