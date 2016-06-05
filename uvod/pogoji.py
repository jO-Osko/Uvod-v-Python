geslo_miha ="password"
geslo_luka = "password"
geslo_anze = "password anze"

geslo_uporabnik = raw_input("Vnesi svoje geslo") # uporabnik vnese geslo

if geslo_uporabnik == geslo_miha: # preverimo, ce je to geslo enako, pazimo, da uporabljamo == in ne =
    print("geslo je pravilno")
    print("zivjo miha")
elif geslo_uporabnik == geslo_luka: # ce geslo ni enako geslo_miha in je enako geslo_luka, izvedemo zamaknjeno kodo
    print("geslo je pravilno")
    print("zivjo luka")
elif geslo_uporabnik == geslo_anze: # ce ni bil izpolnjen noben izmed zgornjih pogojev in je geslo enako geslo_anze izvedemo kodo
    print("geslo je pravilno")
    print("zivjo luka")
else: # ce ni bil izpolnjen noben pogoj od prej potem izpisemo "poskusi ponovno" 
    print("poskusi ponovno")


