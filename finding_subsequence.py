# -*- coding: utf-8 -*-

#给定一个长度为N的数组，找出一个最长的单调自增子序列（不一定连续，但是顺序不能乱） 例如：数组A{1，3，5，2，4，6，7，8}，则其最长
#的单调递增子序列为{1，2，4，6，7，8}，长度为6。


#----------------将数组排序，并和原数组求最长公共子序列，即转化为LCS问题--------------------------
def increase1(L):
    matrix = [[0 for col in range(len(L)+1)] for row in range(len(L)+1)]
    P = sorted(L)
    for i in range(1, len(L)+1):
        for j in range(1, len(L)+1):
            if L[i-1] == P[j-1]:    #若相等，将左上角数值+1并赋值给当前
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:                   #否则，即赋值左侧和上侧的最大值
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

    for i in range(len(L)+1):
        print(matrix[i])

#-------------------------------------------------------------------------

def increase2(L):  #贪心算法：每步只管当前情况不管后面的可能性，导致下面的参数没有得到最优解
    maxsum = 0
    for i in range(len(L)-1):  #以每个元素为起点
        sum = 1                #有起点为初始条件，故sum初始化1
        temp = L[i]            #为比较大小临时存储使用
        for j in range(i+1, len(L)):#每次都遍历所有后面的元素
            if L[j] > temp:         #只按当前和相邻数字的大小判断
                sum += 1
                temp = L[j]
        maxsum = max(maxsum, sum)#找出最大值


    print(maxsum)



increase1([1,3,11,6,9,7,12,8])
increase2([1,3,11,6,9,7,12,8])