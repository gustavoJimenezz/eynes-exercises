def transpose(matrix):
    filas = len(matrix)
    columnas = len(matrix[0])
    matrix_trans = []

    for i in range(columnas):
        aux_1 = []
        for j in range(filas):
            aux_1.append(matrix[j][i])
        matrix_trans.append(aux_1)
    return matrix_trans
