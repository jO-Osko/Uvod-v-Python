# Pomemben pristop inzinirske metode je tudi pravajanje novih problemov na 
# probleme, ki jih ze poznamo, tako pri delu z datotekami le to preberemo kot niz
# in smo ze na podrocju, ki nam je domace

# Z open odpremo datoteko, bodimo pozorni, da dodamo tudi koncnico za piko,
# ki jo racunalniki pogosto skrijejo
datoteka = open("besedilo.txt")

# preberemo celoto datoteko v niz
besedilo = datoteka.read()

# z nizi pa se ze poznamo
print(len(besedilo))

print(besedilo.count("lorem"))
