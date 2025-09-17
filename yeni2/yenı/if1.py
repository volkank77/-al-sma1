# Notların geçerli olup olmadığını kontrol et
not1 = 45
not2 = 80
if not1 > 100 or not1 < 0 or not2 > 100 or not2 < 0 :
    print("Girilen puanlar 0 ile 100 arası olmalı")
else:
    # Ortalama hesapla
    ortalama = (not1 + not2) / 2
    print(f"Ortalaman: {ortalama}")

    # Ortalama üzerinden değerlendirme
    if ortalama > 90:
        print("Süpersin.")
    elif ortalama >= 50:  # 50 ile 90 arası
        print("Geçtin.")
    else:  # 50'nin altı
        print("Kaldın.")
