list1 = [1,2,3,4,5,6]
list2 = ['one','two','three','four','five']
zipped =  list(zip(list1,list2))  #ziping list1 and list2 .. up til n valves
print(zipped)
unzipped = list(zip(*zipped)) # * will un-zip
print(unzipped)

for (l1,l2) in  zip(list1,list2): #can be itterated 
    print(l1)
    print(l2)

items = ['appele', 'banana', 'chiku']
counts = [4,8,12]
prices = [60,20,50]
sentences  = []
for (item,count,price) in zip(items,counts,prices):
    sentences.append('i brought '+str(count)+' '+ str(item)+'at rs '+str(price))
print(sentences)
