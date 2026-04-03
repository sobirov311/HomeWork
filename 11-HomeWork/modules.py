# 1-mashq
def kopaytma(*sonlar):
    """sonlarning ko'paytmasini hisoblaydigan funksiya"""
    natija = 1
    for son in sonlar:
        natija *= son
    return natija
# 2-mashq
def talaba_malumot(ism,familiya,otasining_ismi=None,t_yil=None):
    """talaba xaqida ma'lumot tolpadigan funksiya"""
    talaba= {
        "ism":ism,
        "familiya":familiya,
        "otasining ismi":otasining_ismi,
        "t_yil":t_yil
    }
    return talaba


def talaba_kirit():
    """Foydalanuvchiga avto_info funksiyasi yordamida bir nechta avtolar haqida ma'lumotlarni bitta ro'yxatga joylash imkonini beruvchi funksiya"""
    talabalar=[] # salondagi avtolar uchun bo'sh ro'yxat
    while True:
        print("\nQuyidagi ma'lumotlarni kiriting",end=' ')
        ism=input("Talabaning ismini: ")
        familiya=input(f"{ism.title()}ning familiyasini kiriting: ")
        otasining_ismi=input(f"Otasini ismini kiriting: ")
        t_yil=int(input("tugilgan  yilini kiriting: "))

        talabalar.append(talaba_malumot(ism, familiya, otasining_ismi, t_yil,))
        # Yana avto qo'shish-qo'shmaslikni so'raymiz
        javob = input("Yana talaba qo'shasizmi? (yes/no): ")
        if javob=='no':
            break
    return talabalar
# 3-mashq
def chegirma_hisoblash(*narx, **chegirma):
    jami = sum(narx)

    chegirma = chegirma.get('chegirma', 0)

    if chegirma:
        jami -= jami * (chegirma / 100)

    return jami
# 4-mashq
def Matnlarni_birlashtirish(*matn, **belgi):
    belgi = belgi.get("belgi", " ")
    return belgi.join(matn)

