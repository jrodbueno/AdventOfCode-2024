def determine_operator (row,col,row_size,col_size):
    #recibir una columna para saber cuántas veces tiene que haber cierto signo
    #recibir una fila para saber cuántas veces más tiene que ir un signo
    exponent = col_size-2
    repeats = []
    for i in range(exponent,0,-1):
        repeats.append(2**i)
    repeats.append(1)
    print(repeats)
    
    if (row//repeats[col] % 2 == 0):
        return "+"
    else:
        return "*"



if __name__ == "__main__":
    ls = [67,804,531,9,49,3,80]
    col_size = len(ls)
    row_size = 2**(col_size-1)
    print(determine_operator(31,1,row_size,col_size))
    print(96//32%2)
    
