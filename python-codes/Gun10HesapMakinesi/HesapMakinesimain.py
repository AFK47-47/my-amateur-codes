import HesapMakinesiart
print(HesapMakinesiart.logo)
def topla(n1, n2):
    return n1 + n2
def cikar(n1, n2):
    return n1 - n2
def carp(n1, n2):
    return n1 *  n2
def bol(n1, n2):
    return n1 / n2
devam = True
n1 = int(input("İşlem yapmak istediğiniz sayıyı giriniz: "))
while devam == True:
    islem = input("+\n-\n*\n/\nLütfen bir işlem seçin: ")
    n2 = int(input("İşlemi tamamlamak için ikinci sayıyı giriniz: "))
    sozluk = {"+":topla(n1, n2), "-":cikar(n1, n2), "*":carp(n1, n2), "/":bol(n1, n2)}
    for sozler in sozluk:
        if sozler == islem:
            sonuc = sozluk[sozler]
            print(f"{n1} {islem} {n2} = {sonuc}")
            devammi = input(f"{sonuc} ile işlemlere devam etmek için d, işlemleri bitirmek için b yazınız: ")
            if devammi == "d":
                n1 = sonuc
                devam = True
            else:
                devam = False