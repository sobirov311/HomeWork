ismlar=["Sarvar","Bekzod","laziz","O'ktam"]
print(ismlar)
print(f"Salom {ismlar[0]} bugun kampyuter xonaga boramizmi ?")
print(f" {ismlar[1]}bugun maktabga borasanmi")
print(f"{ismlar[2]} nima gap")
print(f"{ismlar[3]} qayerdasan")
sonlar=( 18,30,-18,8)
print(sonlar[0] + 50)
print(sonlar[ 1] - 10)
print(sonlar[2]*5)
print(sonlar[3]/5)
t_shaxslar=["Gitler", "Amir Temur","Nikola Tesla"]
z_shaxslar=["Elon Musk", "Stiv Jobs", "Vlodimir Putin"]
t_shaxs=t_shaxslar.pop(0)
z_shaxs=z_shaxslar.pop(0)
print(f" Men tarixiy shaxslardan{t_shaxs[0]} bilan, \n zamonaviy shaxslardan esa {z_shaxs[0]} bilan suhbat qilishni istar edim")
print(f" Men tarixiy shaxslardan{t_shaxs[1]} bilan, \n zamonaviy shaxslardan esa {z_shaxs[1]} bilan suhbat qilishni istar edim")
print(f" Men tarixiy shaxslardan{t_shaxs[2]} bilan, \n zamonaviy shaxslardan esa {z_shaxs[2]} bilan suhbat qilishni istar edim")
#('Sarvar', 'O'ktam', 'Bekzod', 'Siroj', 'Bobur')
friends = []
friends.append('Sarvar')
friends.append("O'ktam")
friends.append('Bekzod')
friends.append('Siroj')
friends.append('Bobur')

friends.remove('Siroj')

friends.insert(0, 'Ali')
friends.insert(2, 'Kumush')
friends.append("Akbar")

mehmonlar = []
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(2))

print("Kelgan mehmonlar:", mehmonlar)



