import random

def sayi_tahmin():
    print("\n=== Sayı Tahmin Oyunu ===")
    gizli = random.randint(1, 50)
    hak = 5
    while hak > 0:
        tahmin = int(input("Tahminin: "))
        if tahmin == gizli:
            print("🎉 Bildin!")
            return
        elif tahmin < gizli:
            print("Daha büyük bir sayı dene.")
        else:
            print("Daha küçük bir sayı dene.")
        hak -= 1
    print("Hakkın bitti. Doğru sayı:", gizli)

def tas_kagit_makas():
    print("\n=== Taş-Kağıt-Makas ===")
    secenekler = ["taş", "kağıt", "makas"]
    bilgisayar = random.choice(secenekler)
    oyuncu = input("Seç (taş/kağıt/makas): ").lower()
    print("Bilgisayar:", bilgisayar)
    if oyuncu == bilgisayar:
        print("Berabere!")
    elif (oyuncu == "taş" and bilgisayar == "makas") or \
         (oyuncu == "kağıt" and bilgisayar == "taş") or \
         (oyuncu == "makas" and bilgisayar == "kağıt"):
        print("Kazandın! 🎉")
    else:
        print("Kaybettin 😢")

def menü():
    while True:
        print("\n╔══════════════════╗")
        print("║     OYUNLAR      ║")
        print("╠══════════════════╣")
        print("║ 1- Sayı Tahmin   ║")
        print("║ 2- Taş Kağıt Makas║")
        print("║ 3- Çıkış         ║")
        print("╚══════════════════╝")
        secim = input("Seçimin: ")

        if secim == "1":
            sayi_tahmin()
        elif secim == "2":
            tas_kagit_makas()
        elif secim == "3":
            print("Oyun menüsünden çıkılıyor...")
            break
        else:
            print("Geçersiz seçim!")
