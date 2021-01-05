#lists use[]

numbers = [6 , 4 , 2 , 9 , 5 , 3 , 2 , 52 , 63, 7 , 57 ]
numbers.insert(3 , 4)
print(numbers)

numbers.append(4)
print(numbers)

numbers.reverse() 
print(numbers)

numbers.sort(reverse  = True)
print(numbers)

for i in numbers:
    print(i,end='')

print()
print(numbers[:4])
print(numbers[-len(numbers)])
print(numbers[1:])
print(numbers[:-2])
print(numbers[0:10:3])
print(numbers[::-2])
print(numbers[5:0:-2])

for i in range(len(numbers)):
    print(numbers[0:i]) 
winsize = 5 
for i in range (len(numbers)-winsize-1):
    print(numbers[i:i+winsize] )

