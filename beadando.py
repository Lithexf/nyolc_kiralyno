N = 8
def tabla_rajzol(tabla):
    for sor in tabla:
        # A sor elemeit 0 vagy 1
        print(" ".join(str(x) for x in sor))

def biztonsagos_e(tabla, sor, oszlop):
    for i in range(oszlop):
        if tabla[sor][i] == 1:
            return False
    i, j = sor, oszlop
    while i >= 0 and j >= 0:
        if tabla[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i, j = sor, oszlop
    while i < N and j >= 0:
        if tabla[i][j] == 1:
            return False
        i += 1
        j -= 1
    # nincs ütközés = oké
    return True

def megold_kiralynoket_segito(tabla, oszlop):
    if oszlop >= N:
        return True
    
    for probalkozo_sor in range(N):

        if biztonsagos_e(tabla, probalkozo_sor, oszlop):
            
            tabla[probalkozo_sor][oszlop] = 1
            if megold_kiralynoket_segito(tabla, oszlop + 1):
                return True
            tabla[probalkozo_sor][oszlop] = 0


    return False

def megold_kiralynoket():

    # üres tábla
    tabla = [[0 for _ in range(N)] for _ in range(N)]
    if not megold_kiralynoket_segito(tabla, 0):
        print("Nem létezik megoldás.")
        return False

    print("Megoldás:")
    tabla_rajzol(tabla)
    return True

# restart
megold_kiralynoket()