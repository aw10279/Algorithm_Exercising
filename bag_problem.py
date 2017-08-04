from functools import reduce

def bagpro(W, w, v):
    sheet = [[0 for col in range(W+1)] for row in range(len(w)+1)]  #建二维数组并初始化0

    for i in range(1, len(w)+1):
        for j in range(1, W+1):
            if w[i-1] <= j:     #容量如果装得下
    	        sheet[i][j] = max(sheet[i-1][j], sheet[i-1][j-w[i-1]]+v[i-1])  #比较放和不放哪个更大，并记录
            else:
                sheet[i][j] = sheet[i-1][j]  #装不下就赋值不放情况下的数值

    for i in range(len(w)+1): 
        print(sheet[i])

#bagpro(20, [5,4,3,6,5,6,2], [7,5,5,3,5,1,9])



def bagpro_trans(L):
	sum = reduce(lambda x, y: x+y, L)
	matrix = [[[0 for x in range(int(sum/2)+1)] for y in range(int(len(L)/2)+1)] for z in range(len(L)+1)]
	

bagpro_trans([1,2,3,4])