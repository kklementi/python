#Karel Klementi 06.11.2025

#Iseseisev töö 1.B

#1.1

print('Albert Einstein ütles: "Kujutusvõime on tähtsam kui teadmine."')


#1.2

aasta = 1885
auto = "Benz Patent-Motorwagen"
lause_keskosa = ". aastal valmis esimene sisepõlemismootoriga auto nimega"
lause = print(aasta, lause_keskosa, auto)

#1.3

tulemus = float(input("Esamitulemus protsendina: "))
if tulemus <= 50:
    print("hinne 2")
elif tulemus >= 50 and tulemus < 75:
    print("hinne 3")
elif tulemus >= 75 and tulemus < 90:
    print("hinne 4")
elif tulemus >= 90 and tulemus <= 100:
    print("hinne 5")
else:
    print("Vale sisestus")

#1.4
    
opilasi = int(input("Palju õpilasi on?: "))
kohad = 2
laudu = opilasi // kohad
partnerita = opilasi % kohad
print(f"Täislaudu on {laudu}, ning ilma partnerita jääb {partnerita} õpilast")

