def transpose(matrix):
    columns = len(matrix[0])
    rows = len(matrix)
    transposed_matrix = []

    for row in range(columns):
        aux_list = []
        for column in range(rows):
            aux_list.append(matrix[column][row])
        transposed_matrix.append(aux_list)

    return transposed_matrix
