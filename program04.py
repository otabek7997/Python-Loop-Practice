import random

# Maxfiy 3 xonali raqam
secret_code = random.randint(100, 999)

# Urinishlar
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    guess = int(input(f"{attempts + 1}-urinish. Maxfiy 3 xonali raqamni kiriting: "))
    attempts += 1

    if guess == secret_code:
        print(f"✅ To'g'ri! Maxfiy raqam: {secret_code}")
        break
    elif guess < secret_code:
        print("❌ Noto'g'ri. Maxfiy raqam bundan *katta*. Yana urinib ko'ring.")
    else:
        print("❌ Noto'g'ri. Maxfiy raqam bundan *kichik*. Yana urinib ko'ring.")

# Agar topolmasa
if guess != secret_code:
    print(f"🔒 Yutqazdingiz. Maxfiy raqam: {secret_code}")


