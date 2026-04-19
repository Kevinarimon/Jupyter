import re
from datetime import datetime
teks = input("Masukkan teks yang berisi tanggal (format YYYY-MM-DD): ")
pola = r"\d{4}-\d{2}-\d{2}"
tanggal_ditemukan = re.findall(pola, teks)
tanggal_sekarang = datetime(2026, 4, 19)

for t in tanggal_ditemukan:
    dt = datetime.strptime(t, "%Y-%m-%d")
    format_baru = dt.strftime("%d-%m-%Y")
    selisih = (tanggal_sekarang - dt).days
    print(f"{t} -> {format_baru}, selisih {selisih} hari")
