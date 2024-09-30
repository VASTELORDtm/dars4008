# class Odam:
#     def __init__(self, ism):
#         self.ism = ism
#
#     def salomlashish(self):
#         print(f"Salom {self.ism}")
#
# ism = input("Ismingizni kiriting: ")
# odam = Odam(ism)
# odam.salomlashish()
# class Odam:
#     def __init__(self, ism):
#         self.ism = ism
#
#     def kuylash(self):
#         print(f"{self.ism} kuylamoqda...")
#         return f"{self.ism} kuylamoqda"
#
#     def eshitish(self, kuylovchi_javobi):
#         print(f"{self.ism} {kuylovchi_javobi} eshitdi!")
#         self.gapirish()
#
#     def gapirish(self):
#         print(f"{self.ism}: Salom, men sizni eshitdim!")
#
# odam1 = Odam("Azamjon")
# odam2 = Odam("Umid")
#
# tarqatish = odam1.kuylash()
# odam2.eshitish(tarqatish)
# import time
#
# class Odam:
#     def __init__(self, ism):
#         self.ism = ism
#
#     def yugurish(self):
#         print(f"{self.ism} yugurishni boshladi...")
#         time.sleep(5)
#         self.yiqilish()
#
#     def yiqilish(self):
#         print(f"{self.ism} yiqilib ketdi!")
#
# odam = Odam("Azamjon")
#
# odam.yugurish()
# class Odam:
#     def __init__(self, name):
#         self.name = name
#
#     def tepish(self, koptok):
#         print(f"{self.name} koptokni tepmoqda...")
#         koptok.uchish()
#
# class Koptok:
#     def uchish(self):
#         print("Koptok uchdi!")
#
# zokir = Odam("Zokir")
# koptok = Koptok()
#
# zokir.tepish(koptok)
# class Vaqt:
#     def __init__(self, soat, minut, sekund):
#         self.soat = soat
#         self.minut = minut
#         self.sekund = sekund
#
#     def __str__(self):
#         return f"{self.soat:02d}:{self.minut:02d}:{self.sekund:02d}"
#
#     def oshirish(self, soat=0, minut=0, sekund=0):
#         self.sekund += sekund
#         self.minut += minut + self.sekund // 60
#         self.soat += soat + self.minut // 60
#
#         self.sekund %= 60
#         self.minut %= 60
#         self.soat %= 24
#
#
# vaqt = Vaqt(10, 30, 55)
#
# vaqt.oshirish(soat=5, minut=5, sekund=5)
#
# print(vaqt)
# class Kitob:
#     def __init__(self, nom, muallif, narx, nashriyot):
#         self.nom = nom
#         self.muallif = muallif
#         self.narx = narx
#         self.nashriyot = nashriyot
#
#     def chiqarish(self):
#         print(f"Nom: {self.nom}, Muallif: {self.muallif}, Narx: {self.narx}, Nashriyot: {self.nashriyot}")
#
# kitoblar = [
#     Kitob("Kitob A", "Muallif Azamat", 10000, "Alfavit"),
#     Kitob("Kitob B", "Muallif Bekzod", 15000, "Boshqa"),
#     Kitob("Kitob C", "Muallif Charos", 20000, "Chet"),
#     Kitob("Kitob D", "Muallif Dilshod", 12000, "Dunyo"),
#     Kitob("Kitob E", "Muallif Elyor", 17000, "Eko"),
# ]
#
# for kitob in kitoblar:
#     if 'A' <= kitob.nashriyot[0] <= 'H':
#         kitob.chiqarish()
# class Kompyuter:
#     def __init__(self, nom, ram, narx, protsessor):
#         self.nom = nom
#         self.ram = ram
#         self.narx = narx
#         self.protsessor = protsessor
#
#     def chiqarish(self):
#         print(f"Nom: {self.nom}, RAM: {self.ram}GB, Narx: {self.narx} so'm, Protsessor: {self.protsessor}")
#
# # Obyektlarni yaratish
# kompyuterlar = [
#     Kompyuter("Kompyuter A", 8, 1500000, "Intel i5"),
#     Kompyuter("Kompyuter B", 16, 2500000, "Intel i7"),
#     Kompyuter("Kompyuter C", 4, 1000000, "AMD Ryzen 3"),
#     Kompyuter("Kompyuter D", 12, 5000000, "Intel i9"),
# ]
#
# for kompyuter in kompyuterlar:
#     if 4 < kompyuter.ram < 16:
#         kompyuter.chiqarish()
