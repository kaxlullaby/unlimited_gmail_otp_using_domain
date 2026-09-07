import random
import string

def generate_unlimited_email(domain="vldey.site"):
    #Generate random string 8-12 karakter
    length = random.randint(8, 12)
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    return f"{username}@{domain}"

#contoh pakai
for i in range(10):
    email = generate_unlimited_email()
    print (f"[+] Akun ke-{i+1}: {email}")
