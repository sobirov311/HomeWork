# # Quyidagi ma’lumotdan har bir o‘quvchining o‘rtacha bahosini hisoblang.

students = {
    "Ali": [80, 90, 85],
    "Vali": [70, 60, 75],
    "Sami": [95, 88, 92]
}

for ism,ball in students.items():
 print(f"{ism} ning ortacha bahosi: ")

 orta = sum(ball) / len(ball)

 print("O‘rtacha:", int(orta))

print("*"*20)

# # Narxi 100 dan katta bo‘lgan mahsulotlarni chiqaring.
#
products = [
    {"name":"olma", "price":120},
    {"name":"anor", "price":90},
    {"name":"banan", "price":150}
]
for product in products:
    if product['price'] >100:
        print(product)

print('-*'*20)

# # 18 yoshdan katta foydalanuvchilarni chiqaring.
#
users = [
    {"name":"Ali", "age":20},
    {"name":"Vali", "age":16},
    {"name":"Sami", "age":25}
]
for user in users:
    if user['age']>18:
        print(f'18 yoshdan kattalar:{user}')
print('_______'*5)
# # Har bir kursdagi o‘quvchilar sonini aniqlang.
#
courses = {
    "python": ["Ali","Vali","Sami"],
    "django": ["Ali","Sami"],
    "ai": ["Vali","Sami","Jasur"]
}
for kurs,oquvchi in courses.items():
    print(f"{kurs.title()} kursida {len(oquvchi)} o'qiydi")

print('______'*5)

#
# # Eng katta sonni toping:
#
numbers = [
    [4,7,2],
    [9,1,5],
    [3,8,6]
]
max_number = numbers[0][0]

for qator in numbers:
    for number in qator:
        if number > max_number:
            max_number = number
print(max_number)
#
# # Faqat active foydalanuvchilarni chiqaring.
#
data = {
    "users":[
        {"name":"Ali", "active":True},
        {"name":"Vali", "active":False},
        {"name":"Sami", "active":True}
    ]
}
for d in data['users']:
 if d['active']== True:
     print(f"{d}")