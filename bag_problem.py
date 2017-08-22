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

#---------------------------------------------------------------------------

def bagpro_classic2(W, w, v):         #可用一维数组替代二维，优化空间复杂度
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
    sheet = [0 for col in range(W+1)]  
    
    for i in range(1, W+1):          #遍历所有容量可能
        L = [0 for col in range(len(w))]
        for j in range(len(w)):      #考察所有物品
            if w[j] <= i:            #容量如果装得下
                L[j] = max(sheet[i-1], sheet[i-w[j]]+v[j])  #每种物品都要比较放和不放哪个更大，并记录进L
            else:
                L[j] = sheet[i-1]  #装不下就延续之前的最佳数值

        sheet[i] = max(L)  #最后取最大值放入sheet，完成本次容量的判断

    print(sheet)

#------------------------------------------------------------------------

def bagpro_complete2(W, w, v):      #方法2，只用1个一维数组完成计算，比方法1又节省一半空间
    sheet = [0 for col in range(W+1)]

    for i in range(1, len(w)+1):    #外循环，依次考虑所有物品
        for j in range(1, W+1):     #内循环，顺序遍历所有容量可能（因第j个要参考的最大值，必须是考虑进j之后的值，故必须顺序）
            if w[i-1] <= j:
                sheet[j] = max(sheet[j], sheet[j-w[i-1]]+v[i-1])

    print(sheet)

#bagpro_complete1(10, [1,2,3], [6,4,1])
#bagpro_complete2(10, [1,2,3], [6,4,1])








#--------------------多重背包问题（每种物品有有限多个）,类似完全背包----------------------------------------------------------


def bagpro_multi1(W, w, v, c):      
    sheet = [0 for col in range(W+1)]
    count = [0 for col in range(len(w)+1)] #增加count数组，计算每个最大值对应的物品数量

    for i in range(1, len(w)+1):    #
        for j in range(W,-1,-1):     #
            if w[i-1] <= j:
                if sheet[j] < sheet[j-w[i-1]]+v[i-1]:
                    if count[i] < c[i-1]:
                        sheet[j] = sheet[j-w[i-1]]+v[i-1]
                        if j % w[i-1] == 0:
                            count[i] += 1                 
                        else:
                            sheet[j] = sheet[j-1]
                
    print(sheet)
    
#------------------------------------------------------------------------

def bagpro_multi2(W, w, v, c):      #方法2
    sheet = [0 for col in range(W+1)]

    for i in range(1, len(w)+1):    #
        for j in range(W,-1,-1):
            for k in range(c[i-1]+1):
                if w[i-1]*k <= j:
                    sheet[j] = max(sheet[j], sheet[j-k*w[i-1]]+k*v[i-1])
                

        print(i,j,k,sheet)


bagpro_multi2(20, [9,9,4,1], [3,5,9,8], [3,1,2,3])