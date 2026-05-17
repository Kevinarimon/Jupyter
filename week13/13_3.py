fname = "mbox-short.txt"

try:
    fhand = open(fname)
except FileNotFoundError:
    print("File tidak bisa dibuka:", fname)
    quit()

counts = dict()

for line in fhand:
    if not line.startswith("From "):
        continue
    kata = line.split()
    waktu = kata[5]
    jam = waktu.split(":")[0]
    counts[jam] = counts.get(jam, 0) + 1

lst = sorted(counts.items())
for jam, jumlah in lst:
    print(jam, jumlah)

