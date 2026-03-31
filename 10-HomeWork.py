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
