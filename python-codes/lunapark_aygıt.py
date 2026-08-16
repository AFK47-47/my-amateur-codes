kullanici_yasi = int(input("Lütfen yaşınızı giriniz. "))
kullanici_boyu = int(input("Lütfen boyunuzu cm cinsinden giriniz. "))
foto_tutar = 5
if input("Fotoğraf ister misiniz? E/H") == "E":
    foto_isteme = True
else :
    foto_isteme = False
odenecek_tutar = 0
aygita_binebilir = True
if kullanici_boyu >= 120:
    aygita_binebilir = True
else:
    aygita_binebilir = False

if aygita_binebilir == True:
    if kullanici_yasi <= 8:
        odenecek_tutar = 15

    elif 8 < kullanici_yasi <= 17:
        odenecek_tutar = 20

    elif 45 > kullanici_yasi >= 18:
        odenecek_tutar = 25

    elif 45 <= kullanici_yasi <= 55:
        odenecek_tutar = 0
        foto_tutar = 0
        print("Sizlere parkımız ücretsizdir!")

elif aygita_binebilir == False:
    print("Maalesef aygıta binemezsiniz. Binebileceğiniz uzunlukta görüşürüz!")

toplam_tutar = odenecek_tutar + foto_tutar
if aygita_binebilir == True:
    if foto_isteme == True:
        print(f"Aygıta binebilirsiniz!\nÖdenecek tutar = " + str(odenecek_tutar) + " + fotoğraf tutarı (5TL) = " + str(toplam_tutar) + "TL")
    elif foto_isteme == False:
        print(f"Aygıta binebilirsiniz!\nÖdenecek tutar " + str(odenecek_tutar) + "TL")
