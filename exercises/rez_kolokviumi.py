def suma_kolokviumi(rezultati):
        return rezultati

if __name__ == "__main__":
    n = int(input())
    rezultati = []
    for i in range(0, n):
        r = {}
        brojIndeks = input()
        brojPoeni1 = float(input())
        brojPoeni2 = float(input())
        r['indeks'] = brojIndeks
        r['Predmet'] = 'Vestacka Inteligencija'
        r['Vkupno od kolokviumi'] = float(brojPoeni1 + brojPoeni2)
        rezultati.append(dict(r))

    print(suma_kolokviumi(rezultati))
