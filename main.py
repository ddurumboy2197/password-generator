import secrets
import string

def tasodifiy_parol():
    uzunlik = 12  # Parol uzunligini belgilaymiz
    harflar = string.ascii_letters + string.digits + string.punctuation
    parol = ''.join(secrets.choice(harflar) for _ in range(uzunlik))
    return parol

print(tasodifiy_parol())
```

Kodni ishga tushirganda, siz tasodifiy kuchli parolni konsolga chiqariladi.
