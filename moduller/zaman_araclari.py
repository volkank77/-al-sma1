import time
import datetime

def calistir():
    while True:
        print("╔═══════════════════════╗")
        print("║   ZAMAN / TARİH MENÜ  ║")
        print("╠═══════════════════════╣")
        print("║ 1- Şu anki tarih-saat ║")
        print("║ 2- Geri sayım sayacı  ║")
        print("║ 3- Çıkış              ║")
        print("╚═══════════════════════╝")

        secim = input("Seçiminiz: ")

        if secim == "1":
            simdi = datetime.datetime.now()
            print("Şu an:", simdi.strftime("%d.%m.%Y %H:%M:%S"))
        elif secim == "2":
            saniye = int(input("Kaç saniyeden geriye sayılsın? "))
            for i in range(saniye, 0, -1):
                print(i)
                time.sleep(1)
            print("⏰ Süre doldu!")
        elif secim == "3":
            break
        else:
            print("Geçersiz seçim!")
