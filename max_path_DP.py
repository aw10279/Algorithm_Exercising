#现有一个 m × n (m,n 都小于 100)的网格，位于左上角的 A 要去寻找右下角的 B，A 只能向下或者向右行走，现在问题来了，按照刚才的
#规则，A 到达 B 一共有多少种不重复的路径？

def max_path(m, n):
      
    matrix = [[1 for x in range(m)] for y in range(n)] #只能向下向右的，都可以动规解决。此题需同时用到本行和上一行，必须2维数组
    for i in range(1, n):
        for j in range(1, m):  
            matrix[i][j] = matrix[i][j-1]+matrix[i-1][j]#最优子结构为：每个位置的最大值，都是左边+上边的总和
 
    print(matrix[n-1][m-1])

max_path(10,20)