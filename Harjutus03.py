#Karel Klementi 09.10.2025
#Harjutus03.1

import turtle

nimi = "Karel"
vanus = 21
pikkus = 1.82



print(nimi,",", vanus, "aastat vana ja pikkus on", pikkus, "m")

#Harjutus03.2

print(nimi+", "+str(vanus)+ " aastat vana ja pikkus on "+str(pikkus)+ "m")

#Harjutus03.3

#Trüki välja lause, mis ühendab need andmed, nt: “Soome reis kestab 5 päeva ja üks öö maksab 30.50 eurot.”
#Kasuta väljatrükkimisel ainult komasid (,)

sihtkoht = "Haapsalu"
paevade_arv = 5
oobimise_hind = 100.50
kokku = paevade_arv * oobimise_hind

print(sihtkoht," reis kestab ", paevade_arv, " päeva ja maksab kokku ", kokku, "€")

#Harjutus03.6

kylje_pikkus = 100
nurk = 90
kujundi_varv = "blue"
x = 110
#kordaja = x * 1,5

turtle.pencolor(kujundi_varv)
for j in range(3):
    for i in range(4):
        turtle.fd(kylje_pikkus)
        turtle.lt(nurk)
    turtle.penup()
    turtle.goto(x, 0)
    turtle.pendown()
    x = x * 2
    
    
turtle.done()