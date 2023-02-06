# hra šibenice
# slovník slova.txt (vytvořen ze souboru index.dic, seznam slov vytvořil Petr Kolář a další a je poskytován pod licencí GNU GPL 2)

from random import choice
from obrazek_sibenice import obrazek

## Uhodni slovo
def uhodni ():
    """Funkce, která vyhodnotí, zda se písmeno v hádaném slově nachází nebo ne a vratí zapsané písmeno, případně počet neúspěšných pokusů."""
    with open("slova.txt", encoding="utf-8") as soubor:
        slovo = choice(soubor.readlines())
        slovo = slovo.rstrip()
        #print(f"vybrane slovo je {slovo}")

    delka_slova = len(slovo)
    hadane_slovo = ["_"] * delka_slova
    neuspesny_pokus = 0
    nepatrici_pismena = " "

    vypis_podtrzitek = "".join(hadane_slovo)    # Vypíše tolik podtržítek, kolik má hledané slovo znaků
    print(vypis_podtrzitek)

    while "_" in hadane_slovo:    # Dokud budou v hadanem slově neuhádnuté znaky "_" -> ptej se na "Řekni písmeno"
        pismeno = input("Řekni písmeno: ")
        pismeno = pismeno.lower()
        if len(pismeno) == 1:
            if pismeno in hadane_slovo:   # Pokud už je písmeno v hadaném slově doplněno a člověk se na něj znovu zeptá
                neuspesny_pokus = neuspesny_pokus + 1
                print(f"Na tohle písmeno jsi se už ptal/a. Tvůj počet neúspěšných pokusů je {neuspesny_pokus}. Zkus to znovu.")

            elif pismeno in slovo:
                for pos, char in enumerate(slovo):
                    if(char == pismeno):
                        hadane_slovo[pos]=char
                        print("".join(hadane_slovo))
            else:
                neuspesny_pokus = neuspesny_pokus + 1 
                print(obrazek(neuspesny_pokus))
                if neuspesny_pokus == 9:
                    return f"Tvůj počet neúspěšných pokusů je {neuspesny_pokus}. Prohrál/a jsi! Visíš!\nHádané slovo bylo '{slovo}'"
                    
                elif pismeno in nepatrici_pismena:
                    print(f"Na písmeno \"{pismeno}\" jsi se už ptal/a. Počet neúspěšných pokusů je {neuspesny_pokus}")
                else:
                    nepatrici_pismena = nepatrici_pismena + pismeno + ", "
                    print(f"\"{pismeno}\" ve slově není. Tvé neuhodnuté znaky jsou: {nepatrici_pismena}")
                    print(f"Počet neúspěšných pokusů je: {neuspesny_pokus}. Zkus to znovu.")

        elif pismeno == "f1":   # po zadani f1 se zobrazí slovo :)
            print(slovo)
        else:
            print("Zadej prosím pouze jedno písmeno. ")

        vysledek = "".join(hadane_slovo)
        #print(vysledek)

    return f"Uhodl/a jsi, hledané slovo bylo \"{vysledek}\". Děkuji za hru. Počet neúspěšných pokusů byl {neuspesny_pokus}."

print(uhodni()) # spustí hru

#dotaz na uživatele, zda chce hrát znovu
while True:
    otazka = input("Chceš hrát znovu? ano/ne: ")
    if otazka == "ano" or otazka == "Ano" or otazka == "a":
        print(uhodni())

    else:
        print("Dobře. Měj se, ahoj!")
        break
