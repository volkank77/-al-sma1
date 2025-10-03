def calistir():
    while True:
        print("╔═══════════════════════╗")
        print("║   DÖNÜŞTÜRÜCÜ MENÜ    ║")
        print("╠═══════════════════════╣")
        print("║ 1- Sıcaklık (C <-> F) ║")
        print("║ 2- Uzunluk (km <-> mil)║")
        print("║ 3- Para (TL <-> USD)  ║")
        print("║ 4- Çıkış              ║")
        print("╚═══════════════════════╝")

        secim = input("Seçiminiz: ")

        if secim == "1":
            c = float(input("Celsius: "))
            f = c * 9/5 + 32
            print(f"{c} °C = {f:.2f} °F")
        elif secim == "2":
            km = float(input("Kilometre: "))
            mil = km * 0.621371
            print(f"{km} km = {mil:.2f} mil")
        elif secim == "3":
            tl = float(input("TL miktarı: "))
            usd = tl / 41.68  # Güncel 3.10.2025 Gününde olan kur 
            print(f"{tl} TL ≈ {usd:.2f} USD")
        elif secim == "4":
            break
        else:
            print("Geçersiz seçim!")
