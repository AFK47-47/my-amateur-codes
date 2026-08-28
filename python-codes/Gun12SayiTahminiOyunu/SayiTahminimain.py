import random
import SayiTahminiart
print(SayiTahminiart.logo)
secimhakki = 0
print("Sayı tahmin oyununa hoş geldin!")
kolaymizormu = input("Kolay mod mu, Zor mod mu? k/z  ")
rastegesayi = random.randint(1,100)
if kolaymizormu == "k":
    secimhakki = 10
elif kolaymizormu == "z":
    secimhakki = 5
while secimhakki > 0:
    print(f"{secimhakki} hakkın kaldı.")
    tahmin = int(input("Lütfen tahmininizi yazınız: "))
    if tahmin - rastegesayi < 0:
        print("Daha yukarıda!")
        secimhakki -= 1
    elif tahmin - rastegesayi > 0:
        print("Daha aşağıda!")
        secimhakki -= 1
    elif tahmin - rastegesayi == 0:
        print("Kazandın!")
        secimhakki = -1
if secimhakki == 0:
    print("Kaybettin!")