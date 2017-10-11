from functools import reduce

#--------------------背包问题变形，将给定的一组数字平分成2组，实现各组和的差值最小-----------------------------------
#--------------------要求2组平均，即选择固定数量的数字使其总和在不超过sum/2的前提下最大化，即转化为经典背包问题------

def bagpro_trans1(L): #方法1，三维数组记录所有状态（可选范围、可选数量、最大值）
    sum = reduce(lambda x, y: x+y, L)  #计算总量
    matrix = [[[0 for x in range(sum//2+1)] for y in range(len(L)//2+1)] for z in range(len(L)+1)]  #创建三维数组并初始化
    for i in range(1, len(L)+1):
        for j in range(1, min(i+1, len(L)//2+1)):      #此处从0开始遍历才能得出正确结果，原因不明
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

#-----------------------------------------------------------------------------------

def bagpro_trans2(L):  #方法2：用二维数组替代，降低空间复杂度（原理同01背包）
    sum = reduce(lambda x, y: x+y, L)       
    matrix = [[0 for x in range(sum//2+1)] for y in range(len(L)//2+1)]
    for i in range(1, len(L)+1):
        for j in range(min(i, len(L)//2),0,-1):  #因j行要参考j-1行的值，此处需逆序遍历（同01背包）
            for k in range(1, sum//2+1):         #此结构已是分行存储，当前计算不影响上一行数据，无需逆序
                if L[i-1] <= k:  
                    matrix[j][k] = max(matrix[j][k], matrix[j-1][k-L[i-1]]+L[i-1]) 
                #else:
                    #matrix[j][k] = matrix[j][k]  

    for i in range(len(L)//2+1):
        print(matrix[i])
    print('sum = ', sum)
    print('minimum difference = ', abs(sum-2*matrix[len(L)//2][sum//2]))

bagpro_trans1([31,29,42,35,29,33,66,47])
bagpro_trans2([31,29,42,35,29,33,66,47])