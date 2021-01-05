x = 41
if x%2 == 0 :
    print("even")
else:
    print("odd")
a = 2
b = 4
c = 2 
x = a == c
y = a == b

if  not(x and  y):
    print("arfqrwqqwr")

#for i in range(501):
#    print(i)

#z= 0
#while z<501:
#    print(z)
#    z = z +1

a = int(input())
b = int(input())
notprime = []
numbers = []

for i in range(a,b):
       numbers.append(i)

for num in range(a , b):

    if num > 1:
    
        for i in range(2,num):
            if (num % i) == 0:
                notprime.append(num)

                break
    else :
        notprime.append(num)     
     
prime = list(set(numbers) - set(notprime))
p = prime.sort()
print(prime)     
