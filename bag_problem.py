from functools import reduce

#---------------------经典背包问题，固定元素的w和v以及最大容量W，求最大价值---------------------------------------

def bagpro(W, w, v):
    sheet = [[0 for col in range(W+1)] for row in range(len(w)+1)]  #建二维数组并初始化0

    for i in range(1, len(w)+1):
        for j in range(1, W+1):
            if w[i-1] <= j:     #容量如果装得下
                sheet[i][j] = max(sheet[i-1][j], sheet[i-1][j-w[i-1]]+v[i-1])  #比较放和不放哪个更大，并记录
            else:
                sheet[i][j] = sheet[i-1][j]  #装不下就延续之前的最佳数值

    for i in range(len(w)+1): 
        print(sheet[i])

#bagpro(20, [5,4,3,6,5,6,2], [7,5,5,3,5,1,9])

#--------------------背包问题变形，将给定的一组数字平分成2组，实现各组和的差值最小-----------------------------------
#--------------------要求2组平均，即选择固定数量的数字使其总和在不超过sum/2的前提下最大化，即转化为经典背包问题------
def bagpro_trans(L):
    sum = reduce(lambda x, y: x+y, L)  #计算总量
    matrix = [[[0 for x in range(sum//2+1)] for y in range(len(L)//2+1)] for z in range(len(L)+1)]  #创建三维数组并初始化
    for i in range(1, len(L)+1):
        for j in range(1, min(i+1, len(L)//2+1)):
            for k in range(1, sum//2+1):            #三重for循环，由外至内分别遍历可选范围、可选数量、最大值。
                if L[i-1] <= k:  #如果不超过最大值
                    matrix[i][j][k] = max(matrix[i-1][j][k], matrix[i-1][j-1][k-L[i-1]]+L[i-1]) #比较放和不放的价值
                else:
                    matrix[i][j][k] = matrix[i-1][j][k]  #超过就延续之前的最佳数值

    for i in range(1, len(L)+1):
        for j in range(1, len(L)//2+1):
            print(matrix[i][j])
    print('sum = ', sum)
    print('minimum difference = ', abs(sum-2*matrix[len(L)][len(L)//2][sum//2]))

bagpro_trans([5,8,3,7,7,9,2])