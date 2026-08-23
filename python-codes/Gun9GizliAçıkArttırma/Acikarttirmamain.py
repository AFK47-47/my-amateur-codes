import Acikarttirmaart
print(Acikarttirmaart.logo)
print("Körleme açık arttırmaya hoşgeldiniz.")
devam = "evet"
teklifisim = {}
while devam == "evet":
    ad = input("Lütfen teklif yapacak olan kişinin adını yazınız.")
    teklif = input("Lütfen teklifinizi yazınız.")
    teklifisim[ad] = teklif
    devam = input("Teklif yapacak başka bir insan var mı? evet/hayır")
    if devam == "evet":
        print("\n" * 3000)
enyuksekkisi = max(teklifisim)
print(f"Açık arttırmayı kazanan kişi {teklifisim[max(teklifisim)]}TL'lik teklifi ile {enyuksekkisi}")
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


