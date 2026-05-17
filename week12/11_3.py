nama_file = input("Masukkan nama file: ")

file = open(nama_file)

histogram = {}

for baris in file:
    if baris.startswith("From "):
        kata = baris.split()
        email = kata[1]

        histogram[email] = histogram.get(email, 0) + 1

print(histogram)

