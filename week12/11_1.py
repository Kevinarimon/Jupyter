dictionary = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

print(f"{'key':<6}{'value':<8}{'item'}")

for key, value in dictionary.items():
    print(f"{key:<6}{value:<8}{key}")

    