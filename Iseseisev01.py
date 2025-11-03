#Karel Klementi

#Iseseisev töö 1

#1.1 Tervitus
    #Koostada programm, mis väljastaks ekraanile teksti Tere, maailm! täpselt sellisel kujul - koma ja hüüumärgiga.

print("Tere, maailm!")

#1.2 Aasta liblikas
    #Koostada programm, mille
    #1. real luuakse muutuja nimega aasta ning antakse sellele väärtuseks 2020 (arvuna);
    #2. real luuakse muutuja nimega liblikas ning antakse sellele väärtuseks "teelehe-mosaiikliblikas" (sõnena);
    #3. real luuakse muutuja nimega lause_keskosa ning antakse sellele väärtuseks ". aasta liblikas on " (sõnena);
    #4. real luuakse muutuja nimega lause, mille väärtuse saamiseks ühendatakse üheks sõnaks muutujad aasta,
    #lause_keskosa ja liblikas (vajadusel tuleb kasutada funktsiooni, mis teisendab arvu sõneks);
    #5. real väljastatakse muutuja lause väärtus ekraanile.

aasta = 2020
liblikas = "teelehe-mosaiikliblikas"
lause_keskosa = ". aasta liblikas on "
lause = print(aasta, lause_keskosa, liblikas)
print(lause)

#1.3 Pilved
    #Pilvede alumise pinna (aluse) kõrguse järgi liigitatakse pilvi ülemise, keskmise ja alumise kihi pilvedeks.
    #Ülemiste pilvede alus on kõrgemal kui 6 km, keskmistel pilvedel on 2-6 km kõrgusel,
    #alumistel pilvedel on madalamal kui 2 km. Koostada programm, mis
        #küsib kasutajalt pilvede aluse kõrgust (kilomeetrites),
        #väljastab ekraanile Need on ülemised pilved, kui sisestatu on üle 6,0 km,
        #väljastab Need ei ole ülemised pilved, kui kõrgus on 6,0 km või alla selle.

pilvede_alus = float(input("Pilvede alumise pinna kõrgus kilomeetrites on: "))
if pilvede_alus > 6:
    print("Need on ülemised pilved")
elif pilvede_alus <= 6:
    print("Need ei ole ülemised pilved")
    
#1.4 Bussid
    #Meil on vaja transportida teatud arv inimesi mingi arvu identsete bussidega.
    #Eeldame, et reisijaid on vähemalt üks.Koostada programm, mis küsib transporditavate inimeste arvu ja ühe bussi kohtade arvu
    #(just sellises järjekorras) ning väljastab ekraanile, mitu bussi on vaja ja mitu inimest on viimases bussis
    #(eeldusel, et kõik eelnevad bussid on täis).
try:
    inimesi = int(input("Inimeste arv: "))
    kohti = int(input("Kohti bussis: "))
    busse = inimesi // kohti
    viimane = inimesi % kohti
    print(f"vaja on {busse + 1} bussi ning viimases bussis on {viimane} inimest.")
except:
    print("Kontrolli sisestust ja proovi uuesti!")
    
