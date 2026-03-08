celcius_ke_fahrenheit = lambda C: (9/5) * C + 32
celcius_ke_reamur = lambda C: 0.8 * C

C = float(input("Masukkan suhu dalam Celcius: "))

print("Fahrenheit =", celcius_ke_fahrenheit(C))
print("Reamur =", celcius_ke_reamur(C))