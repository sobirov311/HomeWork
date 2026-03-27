# 1 vazifa
ismlar = ['Jasur', "Javohir", "Kirill"]
print("Salom", ismlar[0])
print("Kaleysan", ismlar[1])
print(ismlar[2], "nma gap")
# 2 vazifa
sonlar = [10, 12.5, 76, 90]
print(sonlar[0] + sonlar[2])
print(sonlar[1] - sonlar[0])
print(sonlar[3] / sonlar[0])
print(sonlar[2] * sonlar[0])
# 3 vazifa
t_shahslar = ["Napoleon", "Stalin"]
z_shahslar = ["Pavel Durov", "Linus Torvalds"]
pop1 = t_shahslar.pop(0)
pop2 = z_shahslar.pop(1)
print("Men tarixiy shahslardan", pop1, "bilan,\n zamonaviy shahslardan esa", pop2, "bilansuhbat qilishni istar edim")
# 4 vazifa
friends = []
friends.append('Bunyod')
friends.append('Rasul')
friends.append('Anvar')
friends.append('Abdullox')
friends.append('Zafar')
friends.append('Aziz')
print("Dostlar  royhati:", friends)
friends.remove('Aziz')
friends.remove('Zafar')
print("Keladiganlar:", friends)
friends.insert(0, 'Muhammadali')
friends.insert(len(friends) // 2, 'Jasur')
friends.append('Javohit')
print("Yangi royhat:", friends)
mehmonlar = []
mehmonlar.append(friends.pop())
mehmonlar.append(friends.pop())
print("Mehmonlar royhati:", mehmonlar)
print("Dostlar royhati:", friends)