datoteka = open("dna.txt")

dnk = datoteka.read()


# Vemo, da so vsi beli moski

if "TGCAGGAACTTC" in dnk and "AAAACCTCA" in dnk:
    print("Seznam osumljencev se zdi smiselen")
else: # Ce storilec ni bel moski, potem je nas seznam osumljencev napacen
    print("S seznamov osumljencev je nekaj narobe")

# Preverimo kdo je to storil
if "TTAGCTATCGC" in dnk and "AAGTAGTGAC" in dnk and "ACCACAA" in dnk:
    print("Ziga je bil")
elif "CCAGCAATCGC" in dnk and "TTGTGGTGGC" in dnk and "AGGCCTCA" in dnk:
    print("Matej je bil")
elif "GCCAGTGCCG" in dnk and "GGGAGGTGGC" in dnk and "GCCACGG" in dnk:
    print("Miha je bil")
else:
    print("Nihce izmed osumljenih ne ustreza")

    
