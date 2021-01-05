import math
x = int(input())
y = int(input())
angle = math.atan(x / y)
pi=22/7
angle = angle*(180/pi)
angle = round(angle)
print(str(angle) + u"\N{DEGREE SIGN}")