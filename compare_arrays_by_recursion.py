# -*- coding: utf-8 -*-

#给定两颗钻石的编号 g1,g2，编号从1开始，同时给定关系数组vector,其中元素为一些二元组，第一个元素为一次比较中较重的钻石的编号，
#第二个元素为较轻的钻石的编号。最后给定之前的比较次数n。请返回这两颗钻石的关系，若g1更重返回1，g2更重返回-1，无法判断返回0。
#输入数据保证合法，不会有矛盾情况出现。

def bigger1(x, y, L, n):      #遍历所有“第一个元素”，若为x判断第二个是否为y，是就直接返回，不是将该元素作为x进行递归，判断x>y是否成立
    for i in range(n):
        if L[i][0] == x:
            if L[i][1] == y:
                return 1
            else:
                return bigger1(L[i][1], y, L, n)

def compare1(g1, g2, vector, num):      #调用bigger先判断g1>g2是否成立，不成立再调用判断g2>g1，修改tag
    tag = bigger1(g1, g2, vector, num)
    if tag != 1:
        tag = bigger1(g2, g1, vector, num)
        if tag == 1:
            tag = -1
        else:
            tag = 0

    print(tag)

#compare1(3,2,[[1,2],[2,4],[1,3],[4,3]],4)


#-----------------------------------------------以此题练习global的用法-----------------------------------------


tag = 0                                 #模块层变量无需加global，但要在函数内赋值该变量需用global重定义
def bigger2(x, y):  
    global tag                          #用global重定义tag，即可使用和修改该变量
    for i in range(n):
        if L[i][0] == x:                #L和n在其他函数内定义为global，且只调用不赋值，无需定义即可使用
            if L[i][1] == y:
                tag = 1
                break
            else:
                return bigger2(L[i][1], y)

def compare2(g1, g2, vector, num):  
    global tag
    global L                            #在函数内定义的global变量和模块层的变量一样，都可以全局使用
    global n
    L = vector
    n = num
    bigger2(g1, g2)
    if tag != 1:
        bigger2(g2, g1)
        if tag == 1:
            tag = -1

    print(tag)

compare2(4,5,[[1,2],[2,4],[1,3],[4,3],[5,3]],5)

#总结：
#1. 模块层的普通变量和函数层的global变量，都可以作为全局变量使用。
#2. 若在函数内只调用全局变量，无需重定义直接使用；若要对全局变量赋值，必须用global重定义，否则会变为函数的局部变量。
#3. 若不用global重定义，函数内先赋值再调用可以（当局部变量用），先调用再赋值会报错（调用即默认为全局变量，所以不能再赋值）
#4. 用global定义变量不能直接赋值，必须分行。