# -*- coding: utf-8 -*-
#------------------------------寻找最长公共子序列（LCS）-----------------------------
def LCS(x, y):

    matri_n = [[0 for col in range(len(y)+1)] for row in range(len(x)+1)]  #计数矩阵
    matri_d = [[0 for col in range(len(y)+1)] for row in range(len(x)+1)]  #方向矩阵，用来回溯所有选定元素

    for i in range(1, len(x)+1):        #动规解决：以2个字符串为行和列，建立矩阵，记录每种状态下的公共子序列最大值
        for j in range(1, len(y)+1):

            if x[i-1] == y[j-1]:
                matri_n[i][j] = matri_n[i-1][j-1]+1   #相同，将左上角（必须去掉当前的2个元素，故都要-1）的数值+1并赋值
                matri_d[i][j] = 'same'

            elif matri_n[i][j-1] > matri_n[i-1][j]:   #不同，比较左侧和上侧的数值，将较大的赋值，并在方向矩阵中记录下位置
                matri_n[i][j] = matri_n[i][j-1]
                matri_d[i][j] = 'left'

            elif matri_n[i][j-1] <= matri_n[i-1][j]:
                matri_n[i][j] = matri_n[i-1][j]
                matri_d[i][j] = 'up'

    return matri_n, matri_d

def getLCS(x, y):

    matri_n, matri_d = LCS(x, y)   #调用LCS，完成2组矩阵
    i, j = len(x), len(y)
    res = ''

    while i>0 and j>0:
        if matri_d[i][j] == 'same':     #从右下角开始回溯，如果相同将元素加到前面，如果不同左移或上移
            res = x[i-1] + res
            i -= 1
            j -= 1
        if matri_d[i][j] == 'left':     #若左和上的数值相等，且最长序列不止一个，选择向左或向上将会出现不同的结果
            j -= 1                      #若最长只有一个，不论选择哪个方向都是一样的
        if matri_d[i][j] == 'up':
            i -= 1

    for i in range(1, len(x)+1):
        print(matri_n[i])

    for i in range(1, len(x)+1):
        print(matri_d[i])

    print(res)

getLCS('ABCBDAB', 'CBDCABA')