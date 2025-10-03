import moduller.oyun as oyun
import moduller.hesapmakinesi as hesapmakinesi
import moduller.zaman_araclari as zaman_araclari
import moduller.donusturucu as donusturucu

def anaekran():
    while True:
        print("\033[1;30;40m╔════════════════════════╗")
        print("║\033[1;32;40m      VEKTOREL APP \033[1;30;40m     ║")
        print("╠════════════════════════╣")
        print("║   1-Oyunlar            ║")
        print("║   2-Zaman / Tarih      ║")
        print("║   3-Dönüştürücüler     ║")
        print("║   4-Hesap Makinesi     ║")
        print("║   5-                   ║")
        print("║   6-                   ║")
        print("║   7- Çıkış             ║")
        print("║    Seçiminiz?          ║")
        print("╚════════════════════════╝")

        secim = input("Seçiminiz: ")

        if secim == "1":
            oyun.menü()
        elif secim == "2":
            zaman_araclari.calistir()
        elif secim == "3":
            donusturucu.calistir()
        elif secim == "4":
            hesapmakinesi.calistir()
        elif secim == "7":
            print("Program sonlandırılıyor...")
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.")

anaekran()
print("Program sonlandı.")
