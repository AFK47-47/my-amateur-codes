
print("Aylık maaş hesaplayıcısına hoşgeldiniz!")

gunluk_al_maas = int(input("Lütfen günlük aldığınız maaşı yazınız. "))

sendika_kesim = gunluk_al_maas

gunluk_arabasurme_ucret = int(input("Günlük alınan araba sürme ücreti yazınız. "))

aylik_alinan_yol_parasi = int(input("Aylık aldığınız yol parasını yazınız. "))

aylik_alinan_ikramiye = int(input("Aylık alınan ikramiyeyi yazınız. "))

aylik_alinan_cocuk_yardimi = int(input("Aylık alınan çocuk yardımı tutarını yazınız. "))

gunluk_al_yemek_parasi = int(input("Günlük aldığınız yemek parası tutarını yazınız. "))

hi_calisilan_gs = int(input("Hafta boyunca haftaiçi kaç gün çalıştığınızı yazınız. (Tam bir hafta boyunca) "))

if hi_calisilan_gs > 5 or hi_calisilan_gs < 1:
    print("LÜTFEN EN BAŞA DÖNÜP GEÇERLİ BİR SAYI YAZINIZ!!\n AKSİ TAKDİRDE HESAPLAYICI ÇALIŞMAYACAKTIR!")

hs_calisilan_gs = int(input("Lütfen ay boyunca cumartesi çalıştığınız gün toplamını yazınız. "))
if hs_calisilan_gs > 4:
    print("LÜTFEN EN BAŞA DÖNÜP GEÇERLİ BİR SAYI YAZINIZ!!\n AKSİ TAKDİRDE HESAPLAYICI ÇALIŞMAYACAKTIR!")

ay = input("Hangi ayda olduğunuzu yazınız.\n O/Ş/Mar/May/H/T/Aus/Eyl/Ek/K/Ar\n")


ay_hafta_sayisi = 0
ay_gun_sayisi = 0

if ay == "O" or ay == "Mar" or ay == "H" or ay == "Aus" or ay == "Ek" or ay == "Ar":
    ay_gun_sayisi = 31
if ay == "May" or ay == "T" or ay == "Eyl" or ay == "K":
    ay_gun_sayisi = 30
if ay == "Ş":
    ay_gun_sayisi = 28

if ay == "O" or ay == "Mar" or ay == "H" or ay == "Aus" or ay == "Ek" or ay == "Ar":
    ay_hafta_sayisi = 31 / 7
if ay == "May" or ay == "T" or ay == "Eyl" or ay == "K":
    ay_hafta_sayisi = 30 / 7
if ay == "Ş":
    ay_hafta_sayisi = 28 / 7
hi_ayda_calisilan_gs = round(ay_hafta_sayisi * hi_calisilan_gs)

aylıkarabasurme_ücret = (hs_calisilan_gs + hi_ayda_calisilan_gs) * gunluk_arabasurme_ucret

hs_toplam_para = hs_calisilan_gs * (1.5 * gunluk_al_maas) + hs_calisilan_gs * gunluk_al_yemek_parasi
hi_toplam_para = gunluk_al_maas * hi_ayda_calisilan_gs + hi_ayda_calisilan_gs * gunluk_al_yemek_parasi
aylık_alınan_toplam_maas = hs_toplam_para + hi_toplam_para + aylik_alinan_cocuk_yardimi + aylik_alinan_ikramiye - sendika_kesim + aylıkarabasurme_ücret + aylik_alinan_yol_parasi

print(ay +" ayı sonu alınacak toplam ücret tutarı: " + str(aylık_alınan_toplam_maas))
