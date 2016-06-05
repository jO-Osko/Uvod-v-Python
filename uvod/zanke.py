# -*- coding: utf-8 -*-

# ^ zgornja vrstica pove pythonu, da uporabljamo ne-angleške znake 

pravo_geslo = "password"
stevilo_vpisov = 0  # Nastavimo začetno število ugibanj gesla

while stevilo_vpisov < 3:  # Ponavljamo dokler uporabnik trikrat napačno vpisal gesla
    geslo_uporabnik = raw_input("Vpiši geslo:")

    if geslo_uporabnik == pravo_geslo:  # preverimo če je geslo pravo
        print("pravo geslo")
        break  # Če je geslo pravo potem končamo zanko
    stevilo_vpisov = stevilo_vpisov + 1  # povečamo število napančnih vpisov

if stevilo_vpisov == 3:  # Preverimo ali je uporabnik trikrat narobe vpisal geslo in ga na to opozorimo
    print("Požrlo ti je kartico")

print("Končal sem")
