#Değişken
a = 10
b = 2
# \n new line
# \t tab boşluk (birkaç boşluk) yapar
print("""Son\tuç:""",a/3,'''\n//:''',a//3,3>5)



# Program ana menusu
##print("╔")
baslik = "PROGRAM ANA MENU sdfşlajk"
print(baslik)
#print(len("Ankara"))
##print(len(baslik))
##print("Ankara "*3)
##print("Ankara "*len("Ankara "))
##print("╔","═"*len(baslik),"╗")
print("╔","═"*(len(baslik)+2),"╗",sep="")
print("║",baslik,"║")
print("╠","═"*(len(baslik)+2),"╣",sep="")

for a in range(5):
    print("║"," "*len(baslik),"║")
print("Seçiminiz")

   


# Proje ana ekran tasarımı
print("╔════════════════════════╗")
print("║      VEKTOREL APP      ║")
print("╠════════════════════════╣")
print("║   1-Oyunlar            ║")
print("║   2-Çizimler           ║")
print("║   3-Hesaplamalar       ║")
print("║   4-                   ║")
print("║   5-                   ║")
print("║   6-                   ║")
print("║   7-                   ║")
print("║    Seçiminiz?          ║")
print("╚════════════════════════╝")
secim = input()