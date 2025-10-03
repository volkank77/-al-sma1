def toplama(a, b):
    return a + b

def cikarma(a, b):
    return a - b

def carpma(a, b):
    return a * b

def bolme(a, b):
    if b == 0:
        return "Sıfıra bölme hatası!"
    return a / b

def calistir():
    while True:
        print("╔═════════════════════╗")
        print("║   Hesap Makinesi    ║")
        print("║═════════════════════║")
        print("║  1-Toplama          ║")
        print("║  2-Çıkarma          ║")
        print("║  3-Bölme            ║")
        print("║  4-Çarpma           ║")
        print("║  5-Çıkış            ║")
        print("╚═════════════════════╝")

        secim = input("İşlem seçiniz (1/2/3/4/5): ")

        if secim == "5":
            print("Hesap makinesinden çıkılıyor...")
            break

        sayi1 = float(input("Birinci sayıyı giriniz: "))
        sayi2 = float(input("İkinci sayıyı giriniz: "))

        if secim == "1":
            print("Sonuç:", toplama(sayi1, sayi2))
        elif secim == "2":
            print("Sonuç:", cikarma(sayi1, sayi2))
        elif secim == "3":
            print("Sonuç:", bolme(sayi1, sayi2))
        elif secim == "4":
            print("Sonuç:", carpma(sayi1, sayi2))
        else:
            print("Geçersiz seçim!")
