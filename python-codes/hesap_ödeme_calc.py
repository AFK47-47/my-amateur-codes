print("Hoşgeldiniz!")
fatura = float(input("Hesap ne kadar tuttu?"))
bahsis_yuzdelik = int(input("Hesabın yüzde kaçını bahşiş olarak vermek istersin?"))
odeyecek_kisi_sayisi = int(input("Hesabı kaç kişi bölüşeceksiniz?"))
verilecek_bahsis = fatura * (bahsis_yuzdelik) / 100
bahsisle_ucret = fatura + verilecek_bahsis
kisi_basına_ucret = bahsisle_ucret / odeyecek_kisi_sayisi
print("Kişi başına ödenecek ücret = " + str((round(kisi_basına_ucret, 2))))
