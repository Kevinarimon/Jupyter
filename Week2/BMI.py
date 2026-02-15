tinggi = eval(input("Masukkan tinggi badan (meter): "))
bmi = eval(input("Masukkan BMI yang diharapkan: "))

berat = bmi * (tinggi ** 2)

print("Berat badan yang diperlukan adalah", berat, "kg")