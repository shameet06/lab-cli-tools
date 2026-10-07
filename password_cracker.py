import zipfile
import zlib


passwords = []

with open("Ashley-Madison.txt", encoding="utf-8") as f:
    for line in f:
        passwords.append(line.strip())


count = 0

for password in passwords:
    count += 1

    if count % 10000 == 0:
        print(count, password)

    try:
        with zipfile.ZipFile("whitehouse_secrets.zip") as zf:
            zf.extractall(pwd=password.encode())

        print("Password found:", password)
        break

    except (RuntimeError, zipfile.BadZipFile, zlib.error):
        continue