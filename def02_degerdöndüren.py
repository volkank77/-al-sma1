def böl(a, b):
    print("Bölme:", a / b)
    return "Kivi"

def topla(a, b):
    print("Toplam:", a + b)
    return "Dana"

def çarp(a, b):
    print("Çarpım:", a * b)
    return "Tavuk"

def çıkar(a, b):
    print("Fark:", a - b)
    return "Tavşan"  


# Kullanıcıdan seçim al
print("Yapmak istediğiniz işlemi seçin:")
print("1 - Toplama")
print("2 - Çıkarma")
print("3 - Çarpma")
print("4 - Bölme")

secim = input("Seçiminiz (1/2/3/4): ")

a = float(input("1. sayıyı girin: "))
b = float(input("2. sayıyı girin: "))

if secim == "1":
    print(topla(a, b))
elif secim == "2":
    print(çıkar(a, b))
elif secim == "3":
    print(çarp(a, b))
elif secim == "4":
    if b != 0:
        print(böl(a, b))
    else:
        print("Sıfıra bölme hatası!")
else:
    print("Geçersiz seçim yaptınız.")


