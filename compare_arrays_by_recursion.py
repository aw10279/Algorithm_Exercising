# -*- coding: utf-8 -*-

#给定两颗钻石的编号 g1,g2，编号从1开始，同时给定关系数组vector,其中元素为一些二元组，第一个元素为一次比较中较重的钻石的编号，
#第二个元素为较轻的钻石的编号。最后给定之前的比较次数n。请返回这两颗钻石的关系，若g1更重返回1，g2更重返回-1，无法判断返回0。
#输入数据保证合法，不会有矛盾情况出现。

def bigger(x, y, L, n):      #遍历所有“第一个元素”，若为x判断第二个是否为y，是就直接返回，不是将该元素作为x进行递归，判断x>y是否成立
    for i in range(n):
        if L[i][0] == x:
            if L[i][1] == y:
                return 1
            else:
                return bigger(L[i][1], y, L, n)

def compare(g1, g2, vector, num):      #调用bigger先判断g1>g2是否成立，不成立再调用判断g2>g1，修改tag
    tag = bigger(g1, g2, vector, num)
    if tag != 1:
        tag = bigger(g2, g1, vector, num)
        if tag == 1:
            tag = -1
        else:
            tag = 0

    print(tag)

compare(3,2,[[1,2],[2,4],[1,3],[4,3]],4)