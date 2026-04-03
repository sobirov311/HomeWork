def foydalanuvchi_malumotlari (ism, familiya, tugilgan_yil, tugilgan_joy, telefon=None,email=None):
    """foydalanuvchining ism familiya tugilgan yili  tugilgan joyi telefon raqami va emailini oziga qabul qilib soraydi"""
    hozirgi_yil =2026
    yosh = hozirgi_yil - tugilgan_yil

    malumot={
        'ism':ism,
        'familiya':familiya,
        'tugilgan_yil':tugilgan_yil,
        'tugilgan_joy':tugilgan_joy,
        'telefon':telefon,
        'email':email
    }
    if email:
        malumot["email"] = email
    if telefon:
        malumot["telefon"] = telefon

    return malumot

foyda = foydalanuvchi_malumotlari(
    "Ali",
    "Valiyev",
    2000,
    "Toshkent",
    "+998878416662",
    email="ali@mail.com"
)

print(foyda)
# 2-mashq

mijozlar = []

n = int(input("Nechta mijoz kiritasiz: "))
i = 0

while i < n:
    print(f"\n{i+1}-mijoz ma'lumotlari:")

    ism = input("Ism: ")
    familiya = input("Familiya: ")
    yil = int(input("Tug'ilgan yil: "))
    joy = input("Tug'ilgan joy: ")

    # ixtiyoriy maydonlar
    tel = input("Telefon (bo'sh qoldirish mumkin): ")
    email = input("Email (bo'sh qoldirish mumkin): ")

    yosh = 2026 - yil

    mijoz = {
        "ism": ism,
        "familiya": familiya,
        "yil": yil,
        "joy": joy,
        "yosh": yosh,
        "tel": tel,
        "email": email
    }

    mijozlar.append(mijoz)
    i += 1

# Natijani chiqarish
print("\nMijozlar ro'yxati:\n")

for m in mijozlar:
    print(f"{m['ism'].title()} {m['familiya'].title()}, {m['yosh']} yosh, {m['joy'].title()}")
    if m['tel']:
        print(f"Tel: {m['tel']}")
    if m['email']:
        print(f"Email: {m['email']}")
    print("------"*3)



def kattasini_top(x, y, z):
    """Uchta sondan eng kattasini qaytaruvchi funksiya."""
    return max(x, y, z)


print(f"Eng kattasi: {kattasini_top(10, 25, 15)}")


def aylana_info(radius, pi=3.14159):
    """Aylana haqidagi ma'lumotlarni lug'atda qaytaradi."""
    aylana = {
        'radius': radius,
        'diametr': 2 * radius,
        'perimetr': 2 * pi * radius,
        'yuza': pi * (radius ** 2)
    }
    return aylana


print(aylana_info(5))


def tub_sonlar_top(min_son, max_son):
    tub_sonlar = []
    for n in range(min_son, max_son + 1):
        if n < 2:
            continue
        tub = True
        for x in range(2, int(n ** 0.5) + 1):
            if n % x == 0:
                tub = False
                break
        if tub:
            tub_sonlar.append(n)
    return tub_sonlar


print(f"Tub sonlar: {tub_sonlar_top(1, 20)}")


def fibonacci_gen(n):
    sonlar = []
    for x in range(n):
        if x == 0 or x == 1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x - 1] + sonlar[x - 2])
    return sonlar


miqdor = int(input("Nechta Fibonachchi soni kerak? "))
print(fibonacci_gen(miqdor))