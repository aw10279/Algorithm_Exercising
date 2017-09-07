# -*- coding: utf-8 -*-

def LCS(x, y):

    matri_n = [[0 for col in range(len(y)+1)] for row in range(len(x)+1)]
    matri_d = [[0 for col in range(len(y)+1)] for row in range(len(x)+1)]

    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):

            if x[i-1] == y[j-1]:
                matri_n[i][j] = matri_n[i-1][j-1]+1
                matri_d[i][j] = 'same'

            elif matri_n[i][j-1] > matri_n[i-1][j]:
                matri_n[i][j] = matri_n[i][j-1]
                matri_d[i][j] = 'left'

            elif matri_n[i][j-1] <= matri_n[i-1][j]:
                matri_n[i][j] = matri_n[i-1][j]
                matri_d[i][j] = 'up'

    return matri_n, matri_d

def getLCS(x, y):

    matri_n, matri_d = LCS(x, y)
    i, j = len(x), len(y)
    res = ''

    while i>0 and j>0:
        if matri_d[i][j] == 'same':
            res = x[i-1] + res
            i -= 1
            j -= 1
        if matri_d[i][j] == 'left':
            j -= 1
        if matri_d[i][j] == 'up':
            i -= 1

    for i in range(len(x)+1):
        print(matri_n[i])

    for i in range(len(x)+1):
        print(matri_d[i])

    print(res)

getLCS('ABCBDAB', 'CBDCABA')