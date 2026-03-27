dav=["Turkiya","O'zbekiston","Shimoliy Kareya ","AQSH","Xitoy"]
print(dav)
len(dav)
print(len(dav) )
print()

tartib=sorted(dav)
print(f"sorted() funksiyasi yordamida tartiblangan ro'yxat: {tartib}")
tes_tar=sorted(dav,reverse=True)

print()

print(f"sorted() funksiyasi yordamida teskari tartiblangan ro'yxat: {tes_tar}")
print(f"Asl ro'yhat: {dav}")

print()

dav.reverse()
print(f"reverese() funksiyasi yordamida aylantirib qoyilgan jadval: {dav}")

print()

dav.sort()
print(f"sort() funksiyasi yordamida alifbo boyicha royhat: {dav}")

print()

dav.sort(reverse=True)
print(f"sort() funksiyasi yordamida alifboga teskari ro'yhat: {dav}")
sonlar=list(range(120,1201,2))
print(sonlar)
yigindi=sum(sonlar)
eng_past=min(sonlar)
eng_baland=max(sonlar)
print(yigindi)
print(eng_past,"+",eng_baland, eng_baland+eng_past)

print("Ro'yhat ichida", (len(sonlar)), "element bor")

print("Boshidagi 20ta qiymat", sonlar[:20])
print("Oxiridagi 20ta qiymat", sonlar[-20:])

taomlar = ['manti', 'osh', 'chuchvara', "so'msa", "sho'rva"]
print(taomlar)

nonushta = taomlar[:]
print(nonushta)

nonushta.remove("osh")
nonushta.remove("chuchvara")
nonushta.remove("so'msa")
nonushta.remove("sho'rva")

nonushta.append("saryog'")
nonushta.append("asal")

print(nonushta)

print(taomlar, "va", nonushta)

nonushta[0] = 'qaymoq va non'
nonushta = (tuple(nonushta))
print(nonushta)

