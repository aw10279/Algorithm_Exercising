import random, math

n = 0
for i in range(10000):
    x = random.uniform(0, 2)
    y = random.uniform(0, 2)
    print(x, y)
    if math.sqrt((x-1)**2+(y-1)**2) < 1:
        n += 1

print(n/10000*4)