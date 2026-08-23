
import sezarşifreart
print(sezarşifreart.logo)
alfabe = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
devam_et= "evet"
while devam_et == "evet":
    sifresonuc = []
    desifresonuc = []
    sifreyadadesifre = input("Lütfen şifrelemek için 'şifre' veya deşifrelemek için 'deşifre' yazınız:\n").lower()
    yazi = input("Metni giriniz:\n").lower()
    kaydirmasayi = int(input("Kaydırma sayısını giriniz:\n"))

    if sifreyadadesifre == "şifre":
        sifrelemesecimi = yazi

    elif sifreyadadesifre == "deşifre":
        desifrelemesecimi = yazi



    def sifreleme(sifrelemesecimi, kaydirmasayi):
        for harf in sifrelemesecimi:
            if harf in alfabe:
                yeniharf=alfabe.index(harf) + kaydirmasayi
                if yeniharf > len(alfabe) - 1:
                    yeniharf -= len(alfabe)
                sifresonuc.append(alfabe[yeniharf])
            else:
                sifresonuc.append(harf)
        print("".join(sifresonuc))

    def desifreleme(desifrelemesecimi, kaydirmasayi):
        for harf in desifrelemesecimi:
            if harf in alfabe:
                yeniharf=alfabe.index(harf) - kaydirmasayi
                desifresonuc.append(alfabe[yeniharf])
            else:
                desifresonuc.append(harf)
        print("".join(desifresonuc))


    if sifreyadadesifre == "şifre":
        sifreleme(sifrelemesecimi, kaydirmasayi)

    elif sifreyadadesifre == "deşifre":
        desifreleme(desifrelemesecimi, kaydirmasayi)
    devam_et= input("Başka bir işleminiz var mıydı? evet/hayır")





