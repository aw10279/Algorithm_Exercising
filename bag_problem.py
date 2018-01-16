from functools import reduce

#---------------------01背包问题，给定元素的w和v以及最大容量W，求最大价值---------------------------------------


def bagpro_classic1(W, w, v):          #方法1：经典二维数组动规解决
    sheet = [[0 for col in range(W+1)] for row in range(len(w)+1)]  #建二维数组并初始化0

    for i in range(1, len(w)+1):
        for j in range(1, W+1):
            if w[i-1] <= j:            #容量如果装得下
                sheet[i][j] = max(sheet[i-1][j], sheet[i-1][j-w[i-1]]+v[i-1])  #比较放和不放哪个更大，并记录
            else:
                sheet[i][j] = sheet[i-1][j]  #装不下就延续之前的最佳数值

    for i in range(len(w)+1): 
        print(sheet[i])

#---------------------------------------------------------------------------

def bagpro_classic2(W, w, v):         #方法2：用一维数组替代二维，优化空间复杂度
    sheet = [0 for col in range(W+1)]

    for i in range(1, len(w)+1):
        for j in range(W,-1,-1):      #因每一元素只需和前一组之前的元素比较，因此内循环采用逆序，可重复利用空间且不影响功能
            if w[i-1] <= j:     
                sheet[j] = max(sheet[j], sheet[j-w[i-1]]+v[i-1])  #同一维之间前后比较即可

    print(sheet)

#bagpro_classic1(20, [5,4,3,6,5,6,2], [7,5,5,3,5,1,9])
#bagpro_classic2(20, [5,4,3,6,5,6,2], [7,5,5,3,5,1,9])







#--------------------完全背包问题（每种物品有无限多个）,一维数组即可完成记录--------------------------------------------------


def bagpro_complete1(W, w, v):       #方法1，自创，每个容量都考察所有物品，最后取最大值判断哪个最合适，需额外数组L
    sheet = [0 for col in range(W+1)]#sheet存储按照容量值排序的各容量下的最大值
    
    for i in range(1, W+1):          #遍历所有容量可能
        L = [0 for col in range(len(w))]
        for j in range(len(w)):      #考察所有物品(W和w都为整数，故W每加1，最多可多放1个物品，而不能反复放，故可以这样遍历)
            if w[j] <= i:            #如果装得下
                L[j] = max(sheet[i-1], sheet[i-w[j]]+v[j])  #每种物品都比较放和不放哪个更大，并记录进L
            else:
                L[j] = sheet[i-1]  #装不下就延续之前的最佳数值

        sheet[i] = max(L)  #最后取最大值放入sheet，完成本次判断(因每次循环最多就多放1个，故该值即为该容量下的最大值)

    print(sheet)           #

#------------------------------------------------------------------------

def bagpro_complete2(W, w, v):      #方法2，只用1个一维数组完成计算，比方法1又节省一半空间
    sheet = [0 for col in range(W+1)]

    for i in range(1, len(w)+1):    #外循环，依次考虑所有物品
        for j in range(1, W+1):     #内循环，顺序遍历所有容量（因要参考的最大值必须是考虑进j之后的值，故必须顺序）
            if w[i-1] <= j:
                sheet[j] = max(sheet[j], sheet[j-w[i-1]]+v[i-1])

    print(sheet)

#bagpro_complete1(20, [5,2,3,5,7], [6,4,1,5,3])
#bagpro_complete2(20, [5,2,3,5,7], [6,4,1,5,3])








#--------------------多重背包问题（每种物品有有限多个）,类似01背包的思路-----------------------------------------------------


def bagpro_multi1(W, w, v, c):      #方法1，01背包基础上增加一组循环
    sheet = [0 for col in range(W+1)]

    for i in range(1, len(w)+1):
        for j in range(W,-1,-1):        #下一层循环专门遍历个数的可能性，故判断基础必须不包含当前物品，故此循环需为逆序
            for k in range(c[i-1]+1):   #针对每种物品、每个重量(前两层循环)，遍历所有当前物品个数的可能性，找出最大值
                if w[i-1]*k <= j:
                    sheet[j] = max(sheet[j], sheet[j-k*w[i-1]]+k*v[i-1])  #sheet用j的顺序填写，k只是在单个单元格内循环比较
                

    print(sheet)

#------------------------------------------------------------------------

def bagpro_multi2(W, w, v, c):      #方法2，二进制思维分解物品个数，将时间复杂度从N降为logN
    sheet = [0 for col in range(W+1)]
    weight = []                     #存储分解后的重量和价值
    value = []

    for i in range(len(w)):        #此循环将所有物品个数以2^n的形式分解，并组成新list
        m = c[i]
        k = 1
        while m >= k:
            weight.append(k*w[i])
            value.append(k*v[i])
            m -= k
            k *= 2
        if m >0:
            weight.append(m*w[i])
            value.append(m*v[i])

    for i in range(1, len(weight)+1):  #将01背包方法用于新组成的list，完成
        for j in range(W,-1,-1):
            if weight[i-1] <= j:     
                sheet[j] = max(sheet[j], sheet[j-weight[i-1]]+value[i-1])


    print(sheet)


bagpro_multi1(20, [9,9,4,1], [3,5,9,8], [2,1,2,3])
bagpro_multi2(20, [9,9,4,1], [3,5,9,8], [2,1,2,3])