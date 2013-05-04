

def read_matrixes(filename):
    file = open(filename, "r")

    matrix = ""
    matrixes = []
    for line in file:
        if line.strip():
            matrix += line
        else:
            if matrix:
                matrixes.append(matrix)
            matrix = ""
    if matrix:
        matrixes.append(matrix)

    # print matrixes
    return matrixes


