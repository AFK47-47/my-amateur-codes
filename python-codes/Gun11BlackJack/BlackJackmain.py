import random
import BlackJackart
bakiye = 100
devam = False
kartlar = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
kullanicideste = []
bilgisayardeste = []
def kullanicibirmionbirmi():
    kartinsirasi = 0
    for kart in kullanicideste:
        if kullanicidestetoplam() > 21 and 11 in kullanicideste:
            if kart == 11:
                kartinsirasi = kullanicideste.index(kart)
                kullanicideste[kartinsirasi] = 1

def bilgisayarbirmionbirmi():
    kartinsirasi = 0
    for kart in bilgisayardeste:
        if bilgisayardestetoplam() > 21 and 11 in bilgisayardeste:
            if kart == 11:
                kartinsirasi = bilgisayardeste.index(kart)
                bilgisayardeste[kartinsirasi] = 1

def kullanicidestetoplam():
    kullanicidestetoplami = 0
    for kart in kullanicideste:
        kullanicidestetoplami += kart
    return kullanicidestetoplami

def bilgisayardestetoplam():
    bilgisayardestetoplami = 0
    for kart in bilgisayardeste:
        bilgisayardestetoplami += kart
    return bilgisayardestetoplami

def kartacma():
    acilank = random.choice(kartlar)
    return acilank

def durumyazdir():
    print(f"Senin desten:            {kullanicideste},     Anlık Toplam: {kullanicidestetoplam()}")
    print(f"Bilgisayarın destesi:    {bilgisayardeste},         Anlık Toplam: {bilgisayardestetoplam()}")
secimacgec = "aç"

if input("BlackJack oynamak ister misin?  e/h  ") == "e":
    devam = True
while devam == True:
    kullanicideste.append(kartacma())
    kullanicideste.append(kartacma())
    bilgisayardeste.append(kartacma())
    print(BlackJackart.logo)
    print(f"Bakiyeniz: {bakiye}TL")
    bahistutari = int(input("Oynamak istediğiniz bahis tutarını giriniz: "))
    if bahistutari > bakiye:
        print("Lütfen geçerli bir tutar giriniz!")
        devam = False
    if kullanicidestetoplam() != 21:
        durumyazdir()
    kullanicibirmionbirmi()
    if kullanicidestetoplam() > 21:
        bilgisayardeste.append(kartacma())
        print(f"Oyunu Kaybettiniz!\n -{bahistutari}TL")
        bakiye -= bahistutari
        devam = False
        print(f"Bakiyeniz {bakiye}TL")
    elif kullanicidestetoplam() == 21:
        bilgisayardeste.append(kartacma())
        if bilgisayardestetoplam() == kullanicidestetoplam():
            durumyazdir()
            print("Oyun Berabere!")
            devam = False
            print(f"Bakiyeniz {bakiye}TL")
        elif bilgisayardestetoplam() != kullanicidestetoplam():
            durumyazdir()
            print(f"Oyunu Kazandınız!\n+{bahistutari}TL")
            bakiye += bahistutari
            devam = False
            print(f"Bakiyeniz {bakiye}TL")
    elif kullanicidestetoplam() < 21:
        while secimacgec == "aç":
            if kullanicidestetoplam() > 21:
                print(f"Oyunu Kaybettiniz!\n-{bahistutari}TL")
                bakiye -= bahistutari
                devam = False
                secimacgec = "NON"
                print(f"Bakiyeniz {bakiye}TL")
            elif kullanicidestetoplam() < 21:
                secimacgec = input("Kart mı açacaksın yoksa geçecek misin? aç/geç  ")
                if secimacgec == "aç":
                    kullanicideste.append(kartacma())
                    kullanicibirmionbirmi()
                    durumyazdir()
            elif kullanicidestetoplam() == 21:
                print(f"Oyunu Kazandınız!\n+{bahistutari}TL")
                bakiye += bahistutari
                devam = False
                secimacgec = "NON"
                print(f"Bakiyeniz {bakiye}TL")
        if  secimacgec == "geç":
            while bilgisayardestetoplam() < 17:
                bilgisayardeste.append(kartacma())
                bilgisayarbirmionbirmi()
            if bilgisayardestetoplam() > 21:
                durumyazdir()
                print(f"Oyunu Kazandınız\n+{bahistutari}TL")
                bakiye += bahistutari
                devam = False
                print(f"Bakiyeniz {bakiye}TL")
            elif bilgisayardestetoplam() == 21:
                durumyazdir()
                print(f"Oyunu Kaybettiniz!\n -{bahistutari}TL")
                bakiye -= bahistutari
                devam = False
                print(f"Bakiyeniz {bakiye}TL")
            elif bilgisayardestetoplam() < 21:
                if 21 - bilgisayardestetoplam() > 21 - kullanicidestetoplam():
                    durumyazdir()
                    print(f"Oyunu Kazandınız!\n+{bahistutari}TL")
                    bakiye += bahistutari
                    devam = False
                    print(f"Bakiyeniz {bakiye}TL")
                elif 21 - bilgisayardestetoplam() < 21 - kullanicidestetoplam():
                    durumyazdir()
                    print(f"Oyunu kaybettiniz!\n-{bahistutari}TL")
                    bakiye -= bahistutari
                    devam = False
                    print(f"Bakiyeniz {bakiye}TL")
                elif 21 - bilgisayardestetoplam() == 21 - kullanicidestetoplam():
                    durumyazdir()
                    print("Oyun Berabere!")
                    devam = False
                    print(f"Bakiyeniz {bakiye}TL")
        if input("Yeniden oynamak ister misiniz?  e/h  ") == "e":
            print("\n" * 1000)
            devam = True
            kullanicideste = []
            bilgisayardeste = []
            secimacgec = "aç"
        else:
            print(f"Bakiyeniz: {bakiye}TL")
            devam = False
