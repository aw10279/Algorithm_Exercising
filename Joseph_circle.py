# -*- coding: utf-8 -*-

#已知n个人（以编号0，1，2，3...n分别表示）围坐在一张圆桌周围。从第一个人开始报数，数到m的那个人出列；他的下一个人又从1开始报数，
#数到m的那个人又出列；依此规律重复下去，求最后剩下（胜出）人的序号。

#-------------------------------------------------约瑟夫环---------------------------------

def Joseph(n, m):
    j = 0
    for i in range(2, n+1):
        j = (m+j) % i

    print(j)

Joseph(4,5)

#此算法由数学推导得出：当前轮(n-1人）时，序号为a的人在上一轮(n个人)的序号为(m+a)%n。n=1时胜出者序号当然为0，由此可推导出
#n=2,3,4...,n时的序号。
#如从1（而不是0）开始编号，结果为j+1;如报数起始序号为k,则胜出者序号为(k+j)%n