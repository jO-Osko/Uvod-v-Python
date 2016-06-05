niz = "To je moj stavek 12356 . !? ...;"

# Nizi so skupki posamezni znakov (crk), zato lahko ugotovimo njihovo dolzino
print(len(niz))

# Nize lahko med samo sestevamo
print(niz + ", se dodaten del stavka")

# Python pa javi napako, ce hocemo sesti niz in stevilo "12" + 3 <- to je napaka 

# Nizi s seboj prinesejo veliko uporabnih metod
print(niz.upper())
print(niz.lower())

print(niz.capitalize())

print(niz.title())

# Te metode niza ne spreminjajo, ampak nam vrnejo nov niz

# Ce se katere ne spomnimo si pomagamo s funkcijo dir
# dir(str) nam tako vrne metode na tipu str

naslov = niz.title()

print(naslov * 2)

print(niz)

stran = "ime mi je filip, ime mi je je je rad python, jem hrano, 123, python, sedenje"

# Pomembna lastnost nizov je to, da 'vsebujejo' podnize 
if "python" not in stran: # in preveri, ali se v strani skriva podniz, not in preveri, ali ga ni
    print("prepisoval si")
print("python," in stran) 

# count presteje ponovitvne celega v nizu
print(stran.count(" "))

# metoda find prvo mesto, kjer se nahaja podniz ali pa -1 ce ga ni v iskanem nizu
print(stran.find("asdf"))

print(stran.count("je"))

print(stran.find("je"))

#Uporabna je tudi metoda replace, s katero hitro zamenjamo dele v nizu
print(stran.replace(" je ", " ni "))






