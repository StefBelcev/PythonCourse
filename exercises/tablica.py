import math

if __name__ == "__main__":
    m = int(input())
    n = int(input())
    x = int(input())
    tablica = {}
    if (m > n):
        print('nema podatoci')
    else:
        for broj in range(m,n+1):
            tablica[broj] = (broj*broj,broj*broj*broj,round(math.sqrt(broj),5))
        if x in tablica.keys():
        	print(tablica[x])
        else:
            print('nema podatoci')
    print(sorted(tablica.items()))