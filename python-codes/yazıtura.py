import random
kullanici_yazıtura = int(input("Yazı tura oyununa hoşgeldiniz! Lütfen tahmininizi yapın. Yazı için 0, Tura için 1 "))
randomsayi = random.randint(0,1)
if randomsayi == 0:
    print("Yazı geldi!")
elif randomsayi == 1:
    print("Tura geldi!")
print(randomsayi)
if kullanici_yazıtura == randomsayi:
    print("Tebrikler, kazandınız!")
elif kullanici_yazıtura != randomsayi:
    print("Maalesef kaybettiniz. Yeniden denemek için yeniden başlat!")