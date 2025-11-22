import random
import math

print("=== 21-masala: 6 xonali tasodifiy parol (faqat raqamlar) ===")
parol = ""
for _ in range(6):
    parol += str(random.randint(0, 9))
print("Parol:", parol)


print("\n=== 22-masala: 1 dan 10 gacha son → faktoriali ===")
son1 = random.randint(1, 10)
print("Tasodifiy son:", son1)
print("Faktorial:", math.factorial(son1))


print("\n=== 23-masala: Berilgan satrdan tasodifiy harf tanlash ===")
satr = input("Satr kiriting: ")
harf = random.choice(satr)
print("Tasodifiy tanlangan harf:", harf)


print("\n=== 24-masala: 0–50 gacha son → 7 ga bo‘linishini tekshirish ===")
son2 = random.randint(0, 50)
print("Tasodifiy son:", son2)
if son2 % 7 == 0:
    print("Bu son 7 ga bo'linadi.")
else:
    print("Bu son 7 ga bo'linmaydi.")


print("\n=== 25-masala: 1–4 gacha son → mos xabar ===")
son3 = random.randint(1, 4)
print("Tasodifiy son:", son3)

if son3 == 1:
    print("Bu 1 — Juda yaxshi!")
elif son3 == 2:
    print("Bu 2 — Davom eting!")
elif son3 == 3:
    print("Bu 3 — Yaxshi tanlov!")
else:
    print("Bu 4 — A'lo!")
