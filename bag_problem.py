from functools import reduce

#---------------------经典背包问题，给定元素的w和v以及最大容量W，求最大价值---------------------------------------

def bagpro_classic1(W, w, v):
    sheet = [[0 for col in range(W+1)] for row in range(len(w)+1)]  #建二维数组并初始化0

    for i in range(1, len(w)+1):
        for j in range(1, W+1):
            if w[i-1] <= j:     #容量如果装得下
                sheet[i][j] = max(sheet[i-1][j], sheet[i-1][j-w[i-1]]+v[i-1])  #比较放和不放哪个更大，并记录
            else:
                sheet[i][j] = sheet[i-1][j]  #装不下就延续之前的最佳数值

    for i in range(len(w)+1): 
        print(sheet[i])

def bagpro_classic2(W, w, v):         #优化空间可用一维数组替代
    sheet = [0 for col in range(W+1)]

    for i in range(1, len(w)+1):
        for j in range(W,-1,-1):      #因每一元素只需和前一组之前的元素比较，因此内循环采用逆序，可重复利用空间且不影响功能
            if w[i-1] <= j:     
                sheet[j] = max(sheet[j], sheet[j-w[i-1]]+v[i-1])  #同一数组间前后比较即可

    print(sheet)

bagpro_classic1(20, [5,4,3,6,5,6,2], [7,5,5,3,5,1,9])
bagpro_classic2(20, [5,4,3,6,5,6,2], [7,5,5,3,5,1,9])

#--------------------完全背包问题,一维数组即可完成记录---------------------------------------------------------------


def bagpro_complete(W, w, v):
    sheet = [0 for col in range(W+1)]  #建一维数组并初始化0
    
    for i in range(1, W+1):  #遍历所有容量可能
        L = [0 for col in range(len(w))]
        for j in range(len(w)):  #因为每种都有无限多个，所以每个容量都要考察所有物品，才能判断放哪个最合适
            if w[j] <= i:     #容量如果装得下
                L[j] = max(sheet[i-1], sheet[i-w[j]]+v[j])  #每种物品都要比较放和不放哪个更大，并记录
            else:
                L[j] = sheet[i-1]  #装不下就延续之前的最佳数值

        sheet[i] = max(L)  #最后将汇总的list再取最大值放入sheet，完成本次容量的判断

    print(sheet)

#bagpro_complete(10, [3,2,3], [6,4,1])


#--------------------多重背包问题,一维数组即可完成记录---------------------------------------------------------------


def bagpro_multi(W, w, v, c):
    sheet = [0 for col in range(W+1)]  #建一维数组并初始化0
    
    for i in range(1, W+1):  #遍历所有容量可能
        L = [0 for col in range(len(w))]
        for j in range(len(w)):  #因为每种都有无限多个，所以每个容量都要考察所有物品，才能判断放哪个最合适
            if w[j] <= i:     #容量如果装得下
                L[j] = max(sheet[i-1], sheet[i-w[j]]+v[j])  #每种物品都要比较放和不放哪个更大，并记录
            else:
                L[j] = sheet[i-1]  #装不下就延续之前的最佳数值

        sheet[i] = max(L)  #最后将汇总的list再取最大值放入sheet，完成本次容量的判断

    print(sheet)