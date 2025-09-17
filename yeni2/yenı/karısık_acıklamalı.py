print("Ankara",end="xx") # default end="\n"
print("Vektörel","Akademi",sep="**",end="")
print("Vektörel","Akademi","\nKursu",sep="")   

#print("Merhaba")               # Normal yazdırma
#print("A", "B", sep="-")       # A-B   (sep: ayırıcı)
#print("Son", end="...")        # Son... (end: satır sonuna ekleme)

#sep → print içinde değerlerin arasına ne koyar (default=" ").

#end → satır sonunda ne koyar (default="\n" yani satır atlama).
#int tam sayı (10,5)
#float ondalık sayı (3.14)
#str string / yazı ("merhaba")
#bool mantıksal (true, false )
# Değişkenler
x = 5
y = 3.2
isim = "Ali"

#== eşit mi?

#!= eşit değil mi?

#>, <, >=, <=

#and, or, not

#len("Merhaba")     # 7
#len([1,2,3])       # 3

liste = [1, 2, 3]            # Liste
tuple_ = (1, 2, 3)           # Demet (değiştirilemez)
kume = {1, 2, 3}             # Küme (tekrar yok)
sozluk = {"ad":"Ali", "yas":20}  # Sözlük

if x > 0:
    print("Pozitif")
elif x == 0:
    print("Sıfır")
else:
    print("Negatif")


for i in range(5):
    print(i)   # 0 1 2 3 4  #range(5) → 0’dan başlayıp 5’e kadar olan sayıları üretir (5 dahil değil).
#Yani: 0  1  2  3  4
 
                         #for i in range(5):  i değişkeni sırasıyla bu değerleri alır.


                           #print(i)  her adımda iyi yazdırır.
while x < 5:
    print(x)
    x += 1

#While ekranı  while → koşul doğru olduğu sürece döngüyü tekrarlar.

#x < 5 → x 5’ten küçük olduğu sürece döngü çalışır.

#print(x) → mevcut x değerini yazdırır.x += 1 → x’i 1 artırır, yoksa döngü sonsuz çalışır.
# Özellik           for                                    while                                     |

#Döngü sayısı       Genellikle **önceden belli** (`range`)   Koşula bağlı, **dinamik**                 |
#Kullanım           Liste, dizi veya range üzerinden tekrar  Koşul doğru olduğu sürece tekrar          |
#Sonsuz döngü riski  Düşük                                   Koşulu yanlış ayarlarsan **sonsuz döngü** |



def topla(a, b):
    return a + b

print(topla(3,4))   # 7

#ef topla(a, b):

#def → Python’da fonksiyon tanımlamak için kullanılır.

#topla → fonksiyonun adı.

#(a, b) → fonksiyonun parametreleri, yani dışarıdan alacağı değerler.

#2️⃣ return a + b

#Fonksiyonun yaptığı iş: a ile b’yi toplamak.

#return → fonksiyonun sonucunu geri verir.

#Bu değer başka bir yerde kullanılabilir veya yazdırılabilir.

#3️⃣ print(topla(3,4))

#Fonksiyonu çağırıyoruz: topla(3,4) → a=3, b=4

#Fonksiyon 3 + 4 = 7 değerini geri döndürür.

#print() ile ekrana yazdırıyoruz. 
#Fonksiyon = tekrar tekrar kullanabileceğin kod bloğu

#def ile tanımlanır, return ile değer geri döndürülür

#Parametreler = fonksiyonun içine gönderdiğin değerler

#Fonksiyon çağrıldığında parametreler yerine gerçek değerler gelir
#input kullanıdan veri alır 
    

















