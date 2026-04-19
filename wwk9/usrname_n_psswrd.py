import re
import random
import string

teks = input("Masukkan teks yang berisi email: ")

pola_email = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emails = re.findall(pola_email, teks)

for email in emails:
    username = email.split("@")[0]
    karakter = string.ascii_letters + string.digits
    password = ''.join(random.choice(karakter) for _ in range(8))
    print(f"{email} username: {username}, password: {password}")
