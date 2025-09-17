# string biçimleme /şekillendşrme
aa= "Vektörel Bilişim"
metin = f"Ankara [2024-1923] yıl önce başkent oldu"
metin1 = "Ankara [2024-1923] yıl önce başkent oldu"
print (aa)
print (metin)
print (metin1)
#f format demek üslü parantez olmadan çıkarmaz

# string biçimleme/şekillendirme
ad = input("Adınızı girin?")
##print(ad*3)
##print((ad+"**")*3)
# input bilgiyi string olarak alır.
dy = input(f"Adın güzelmiş {ad}. \nHangi yılda doğdun?")
#print(f"Demek{2025-dy} yaşındasın.")
print(f"Demek {2025-int(dy)} yaşındasın.")


