print("Python Pizza'ya hoşgeldiniz!")
pizza_boyut = input("Lütfen pizzanızın boyutunu seçin. k/o/b ")
sucuk_olsunmu = input("Pizzanızda sucuk ister misiniz? e/h ")
extra_peynir = input("Pizzanızda extra peynir olsun mu? e/h ")
pizza_fiyat = 0

if pizza_boyut == "k":
        pizza_fiyat = 50
elif pizza_boyut == "o":
        pizza_fiyat = 100
elif pizza_boyut == "b":
        pizza_fiyat = 150
else:
    print("Lütfen geçerli bir boyut girişi yapın!")
if extra_peynir == "e":
    pizza_fiyat += 10

if sucuk_olsunmu == "e":
    if pizza_boyut == "k":
        pizza_fiyat += 20
    else:
        pizza_fiyat += 30

print(f"Pizza toplam tutarı {pizza_fiyat}TL")