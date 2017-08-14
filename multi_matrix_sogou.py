# -*- coding: utf-8 -*-
#A[n,m]是一个 n 行 m 列的矩阵，a[i,j] 表示 A 的第 i 行 j 列的元素，定义 x[i,j] 为 A 的第 i 行和第 j 列除了 a[i,j] 之外所有元素
#(共n+m-2个)的乘积，即x[i,j]=a[i,1]*a[i,2]*...*a[i,j-1]*...*a[i,m]*a[1,j]*a[2,j]...*a[i-1,j]*a[i+1,j]...*a[n,j],现输入非负整形
#的矩阵 A[n,m]，求 MAX(x[i,j])，即所有的 x[i,j] 中的最大值。

from functools import reduce

def mul_matrix(m, n, l):
    L = []
    mul1 = [reduce(lambda x, y: x*y, l[i]) for i in range(m)] #各行乘积
    mul2 = [reduce(lambda x, y: x*y, [l[i][j] for i in range(m)]) for j in range(n)] #各列乘积

    for i in range(m):
    	for j in range(n):
    		L.append(mul1[i]*mul2[j]//l[i][j]**2) #去掉指定元素

    print(max(L))

mul_matrix(3,5,[[5,1,8,5,2],[1,3,10,3,3],[7,8,5,5,16]])