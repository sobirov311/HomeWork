oilam={'onam':'Barno',
       't_yil':'1989',
       'yosh':'36',
       'y_joy':'Xorazm'}
print(f" {oilam['onam'].title()} ,\
 {oilam['t_yil']}-yilda tug'ilgan ,\
 {oilam['yosh']}-yoshda")
sevimli_t={
    'onam_t':'manti',
    'ukam_t':'osh',
    'otam_t':'barak'
}
print(f"Onam {sevimli_t['onam_t'].title()}ni yaxshi ko'radi")
print(f"Ukam {sevimli_t['ukam_t'].title()}ni yaxshi ko'radi")
print(f"Otam {sevimli_t['otam_t'].title()}ni yaxshi ko'radi")
py_lugat={
    'integer':'Butun son',
    'for':'Sikl(uchun)',
    'tuple':"O'zgarmas ro'yxat",
    'list':'Ro\'yxat',
    'else':'Aks holda',
    'float':'Butun son',
    'if':'agar',
    'boolen':'Mantiqiy qiymat'
}
kali_s=input("Kalit so'z kiriting: ").lower()
tarjima=py_lugat.get(kali_s)
if tarjima:
    print(tarjima)
else:print("Bunday so'z mavjud emas")
kalit=input("Kalit so'z kiriting: ")
if kalit in py_lugat:
    print(f"{kalit.title()} so'zi {py_lugat[kalit]} deb tarjima qilinadi")
else:
    print("Bunday so'z mavjud emas ")





