def is_prima(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

n = int(input("Masukkan bilangan n: "))

for terdekat in range(n-1, 1, -1):
    if is_prima(terdekat):
        print(f"Bilangan prima terdekat < {n} adalah {terdekat}")
        break