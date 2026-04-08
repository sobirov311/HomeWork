# 1-mashq
class User:
    def __init__(self, ism, foydalanuvchi_ismi, email):
        self.ism = ism
        self.foydalanuvchi_ismi = foydalanuvchi_ismi
        self.email = email
# 2-mashq
    def foy_ism(self):
       print(f"Foydalanuvchi ismi {self.ism}")
    def tolioq_malumot(self):
        print(f"Foydalanuvchi ismi: {self.ism}, "
              f"foydalanuvchi nomi: {self.foydalanuvchi_ismi}, email: {self.email}.")

    def email_f_nomi(self):
        print(f' Foydalanuvchi nomi: {self.foydalanuvchi_ismi}, '
              f'\n Foydalanuvchining email manzili {self.email}')
user0 = User('Azamat Sobirov', 'sobirov.311', 'sobirov.azamat.311@gmail.com')

user0.tolioq_malumot()

user0.email_f_nomi()
print("-----"*8)
# 3-mashq
foydalanuvchi=User('Valibek Aliyev','v_aliyev.213','aliyev_567@gmail.com')
foydalanuvchi1=User('Asadbek Valiyev','asadbek','asadbek_142@gmail.com')

foydalanuvchi.tolioq_malumot()

foydalanuvchi.email_f_nomi()
print("-----"*8)
foydalanuvchi1.foy_ism()

foydalanuvchi1.email_f_nomi()

