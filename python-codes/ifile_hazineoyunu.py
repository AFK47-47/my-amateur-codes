print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /________________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************''')
print("Hazine bulma oyununa hoş geldiniz!")
sağsol = input("Adada bir yol ayrımı var sağmı sol mu?")
if sağsol == "sol":
    print("bir çukura düştün kaybettin")
elif sağsol == "sağ":
    altüst = input("geçtin ve karşında bir kulube var üst kat mı alt kat mı?")
    if altüst == "alt":
        print("alt kattaki çukuru karanlıktan göremedin ve düştün kaybettin.")
    elif altüst == "üst":
        bölüm = input("sonunda sandığı buldun fakat sandık üç farklı bölüme ayrılmış ve yanlış \nbölümün secilmesinde hazine kendini imha ediyor sağ mı sol mu yoksa ortadaki bölümü mü sececeksin? sağ/sol/orta")
        if bölüm == "sağ":
            print("hazineyle birlikte patladın.")
        elif bölüm == "sol":
            print("hazineyle birlikte patladın.")
        elif bölüm == "orta":
            print("hazineyi kazandın!!")
        else:
            print("Lütfen geçerli bir giriş yapın!")
    else:
        print("Lütfen geçerli bir giriş yapın!")
else:
    print("Lütfen geçerli bir giriş yapın!")