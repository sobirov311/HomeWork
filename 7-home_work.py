# # # 1-vazifa
# py_lugat = {
#     "Boolean": "Mantiqiy qiymat",
#     "Float": "O'nlik son",
#     "For": "Biror amalni qayta-qayta bajarish tsikli",
#     "If": "Shartlarni tekshirish operatori",
#     "List": "Ro'yxat, bir nechta qiymatlarni saqlash uchun",
#     "Function": "Ma'lum bir vazifani bajaruvchi kod bloki",
#     "Integer": "Butun son",
#     "String": "Matn ko'rinishidagi ma'lumot turi",
#     "Dictionary": "Lug'at, kalit va qiymat juftligi",
#     "Tuple": "O'zgarmas ro'yxat",
#
# }
#
# print("python lug'ati")
# for py in sorted(py_lugat.keys()):
#     print(f"{py} - {py_lugat[py]}")
#
# #     print( )
# #
# # # 2-vazifa
# davlatlar_pay={
#     "AQSH": "Washington D.C.",
#     "Italiya": "Rim",
#     "Qirg'iziston": "Bishkek",
#     "Qozog'iston": "Nursulton",
#     "Malayziya": "Kuala-Lumpur",
#     "O'zbekiston": "Toshkent",
#     "Singapur": "Singapur",
#     "Tojikiston": "Dushanbe",
#     "Rossiya": "Moskva",
# }
# for dav in davlatlar_pay.keys():
#     print(dav)
# #
# # print("\nDavlatlarning poytaxtlari:")
# # for poytaxt in sorted(davlatlar_pay.values()):
# #         print(poytaxt)
# #
# # davlatlar={
# #    "qirg'iziston": "bishkek",
# #     "qozog'iston": "nursulton",
# #     "malayziya": "kuala-lumpur",
# #     "o'zbekiston": "toshkent",
# #     "singapur": "singapur",
#     "tojikiston": "dushanbe",
#     "rossiya": "moskva",
# }
#
# savol = input("Qaysi davlatning poytaxtini bilishni istaysiz?: ").lower()
#
# poytaxt = davlatlar.get(savol)
#
# if poytaxt in davlatlar:
#     print(f"{poytaxt.title()}ning poytaxti {davlatlar[poytaxt]}")
# else:
#     print("Kechirasiz, bizda bu davlat haqida ma'lumot yo'q")
# taomlar={
#     'non':'4000',
#     'suv':'3000',
#     'choy':'4000',
#     'manti':'20000',
#     'osh':'35000',
#     'shashlik':'12000',
#     'so\'msa':'13000'
# }
# print("3 ta taom buyurtma bering ")
# buyurtmalar = []
#
# for i in range(1, 4):
#     taom = input(f"{i}-taom: ").lower()
#     buyurtmalar.append(taom)
#
# for buyurtma in buyurtmalar:
#     if buyurtma in taomlar:
#         print(f"{buyurtma.title()} {taomlar[buyurtma]} so'm")
#     else:
#         print(f"Kechirasiz, bizda {buyurtma} yo'q.")
#
# #
