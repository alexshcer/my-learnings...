
s = str(input())

senlist = s.split()
senlist.sort()
dic = {}
print(senlist)
for i in range(len(senlist)-2):
     j = i
     if senlist[j] == senlist[j+1]:
        dic[senlist[i]] = senlist.count(senlist[i]) 
        
        

print(dic)