def palindrom(n):
    n = str(n)
    lungime = len(n) - 1
    i = 0
    k = 1
    while i < lungime:
        if n[i] != n[lungime]:
            k = 0
        i += 1
        lungime -= 1
    if k == 1:
        return True
    else:
        return False


def prim(n):
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def sir_prim(y):
    lista = []
    for i in range(0, y, 1):
        if prim(i):
            lista.append(i)
    c = len(lista)
    return lista[c - 1]


optiune = '''
'palindrom' - Pentru aflarea unui palindrom
'numar_prim' - Găsiți cel mai mare număr prim mai mic decât un număr dat
'stop' - oprire program
'''


def main():
    while True:
        optiuni = input(optiune)
        if optiuni.lower() == 'palindrom':
            numar = int(input("Scrieti valoarea:"))
            if palindrom(numar):
                print("Este palindrom")
            else:
                print("Nu este palindrom")
        elif optiuni.lower() == 'numar_prim':
            numar = int(input("Scrieti valoarea:"))
            c = sir_prim(numar)
            print(f'Numarul cel mai mare prim este {c}')
        elif optiuni.lower() == 'stop':
            break
        else:
            print("Nu exista comanda!")


if __name__ == main():
    main()
