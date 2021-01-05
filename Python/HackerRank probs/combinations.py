from itertools import combinations
x,y = input().split()
l1 = []
for i in range(len(1)):
        l1.append(x[i])
for k in range(int(y)):
    

    c = list(combinations(l1 ,k+1))
    c.sort()

    for i in c:
        print(''.join(i))