if __name__ == "__main__":
    # Vkupno e globalna promenliva, no ne e definirana so klucniot zbor global
    vkupno = 0

    # Defiranje na funkcija so klucniot zbor def
    def zbir(x, y):
        vkupno = x + y #Vkupno e lokalna promenliva
        print(f'Vo funkcijata, vkupno =', vkupno)
        # return vkupno
    # vkupno_funkcija = zbir(10, 20)
    # print(f'Nadvor od funkcijata, vkupno =', vkupno_funkcija)

    zbir(10, 20)
    print(f'Nadvor od funkcijata, vkupno =', vkupno)
    # Pari e globalna promenliva, no ne e definirana so klucniot zbor global
    pari = 2000

    # Definiranje na funkcija so klucniot zbor def
    def dodadi_pari(x, y):
        # Definiranje na globalna promenliva so klucniot zbor global,
        # za da promenlivata pari se zeme od globalniot prostor na promenlivi,
        # a ne od lokalniot prostor na promenlivi vo samata funkcija
        global pari
        # za pari da se zeme od globalniot, a ne lokalniot prostor na iminja na samata funkcija
        pari = pari + x + y
        print(f'Vo funkcijata, pari = ', pari)
    dodadi_pari(1, 2)
    print(f'Nadvor od funkcijata, pari = ', pari)
