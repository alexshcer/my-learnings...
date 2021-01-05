# sets use {}
#you cant have duplicate in sets -_- cool
#unorderd

s1 = {'python','c++','Java','javascript'}
print(s1) #prints in random order
print()

s1.add('ReactJS')  #add 
print(s1)
print()
s2 = {"python" , "python"}
print(s2)
print()
l = [1,1,23,4,24,64,2,1,212,34,1,6,'abc','abc'] 
no_duplicate_lists = set(l) #######
print(no_duplicate_lists)

#functions in sets

s3 = ('Java','c#', "NodeJS",'c','C++' )

print()
print(s1.union(s3))
print(s1.intersection(s3))
print(s1.difference(s3))
print(s1.clear)

