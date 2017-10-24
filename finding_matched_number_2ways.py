# -*- coding: utf-8 -*-
#从一组数字中找出包含特殊数字（例59）的所有数字

def way1(n):                    #直接转成字符串，用in判断是否包含即可
	for i in range(1,n+1):
		if str(59) in str(i):
			print(i)

def way2(n):                    #减去59若能被100整除就选中，不能的话去掉末位重复该步骤
	for i in range(1,n+1):
		k = i
		while k >= 59:
			if (k-59)%100 == 0:#能否被整除
				print(i)
				break
			else:
				k //= 10       #去掉末位

way1(1000)
way2(1000)
