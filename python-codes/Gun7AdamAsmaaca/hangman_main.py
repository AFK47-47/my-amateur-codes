import random
from email.mime import image

from Gun7AdamAsmaaca import hangman_art, hangman_words

print(hangman_art.logo)
secilenkelime = random.choice(hangman_words.word_list)
can = 6
tahminmekani = []
for harfsayi in range(len(secilenkelime)):
    tahminmekani.append("_")
kazanma = False
print("".join(tahminmekani))
while can > 0 and kazanma == False:
    tahminedilenbuyukharf = input("Lütfen bir harf tahmin edin: ")
    tahminedilenharf = tahminedilenbuyukharf.lower()
    sayi = 0
    bulundu = False
    for harf in secilenkelime:
        if harf == tahminedilenharf:
            tahminmekani[sayi] = harf
            bulundu = True
        sayi += 1
    if bulundu == False:
        can -= 1
        print("************************  BU HARF KELİMEDE YOK!  ***********************")
    print(f"****************************{can}/6 CANIN KALDI****************************")
    print("".join(tahminmekani))
    if can == 6:
        print(hangman_art.stages[-1])
    if can == 5:
        print(hangman_art.stages[-2])
    if can == 4:
        print(hangman_art.stages[-3])
    if can == 3:
        print(hangman_art.stages[-4])
    if can == 2:
        print(hangman_art.stages[-5])
    if can == 1:
        print(hangman_art.stages[-6])
    if can == 0:
        print(hangman_art.stages[0])
        print("Canın Kalmadı Oyun Bitti!")
        print(f"Doğru kelime: {secilenkelime}")
    if "_" not in tahminmekani:
        kazanma = True
        print("Kazandınız!")
