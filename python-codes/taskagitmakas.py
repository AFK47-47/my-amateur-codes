import random
hamleler = ["    _______\n---'   ____)\n      (_____)\n      (_____)\n      (____)\n---.__(___) ", "    _______\n---'   ____)_____\n           ______)\n          _______)\n         _______)\n---.__________)", "    _______\n---'   ____)____\n          ______)\n       __________)\n      (____)\n---.__(___)"]
kullanicitaskamak = int(input("Oynamak için bir şekil seçin. Taş için 0, kağıt için 1, makas için 2:  "))
if kullanicitaskamak == 0:
    print("Seçtiğin hamle:\n" + hamleler[0])
elif kullanicitaskamak == 1:
    print("Seçtiğin hamle:\n" + hamleler[1])
elif kullanicitaskamak == 2:
    print("Seçtiğin hamle:\n" + hamleler[2])

randomhamle = random.randint(0,2)
if randomhamle == 0:
    print("Bilgisayarın seçtiği hamle:\n" + hamleler[0])
elif randomhamle == 1:
    print("Bilgisayarın seçtiği hamle:\n" + hamleler[1])
elif randomhamle == 2:
    print("Bilgisayarın seçtiği hamle:\n" + hamleler[2])

if randomhamle == kullanicitaskamak:
    print("Sonuç berabere!")
elif kullanicitaskamak == 0 and randomhamle == 1:
    print("Kaybettiniz.")
elif kullanicitaskamak == 0 and randomhamle == 2:
    print("Kazandınız!")
elif kullanicitaskamak == 1 and randomhamle == 0:
    print("Kazandınız!")
elif kullanicitaskamak == 1 and randomhamle == 2:
    print("Kaybettiniz!")
elif kullanicitaskamak == 2 and randomhamle == 0:
    print("Kaybettiniz!")
elif kullanicitaskamak == 2 and randomhamle == 1:
    print("Kazandınız!")
