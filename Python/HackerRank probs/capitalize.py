#def solve(s):
#    l = s.split(' ')
#    for i in l:
#        l1 = []
#        if i[0].isalpha() :
#            l1.append(i[0].upper())
#        else:
#            l1.append(i[0])
#        for j in range(1,len(i)):
#            if i[j].isalpha:
#                l1.append(i[j].lower())
#            else:
#                l1.append(i[j].lower())
#        l2 ="".join(l1)
#        print(l2,end = ' ')
#s = str(input())
#solve(s)
# |||||||||||||||||||||||||||||||||||||||||| #
def solve(s):
   l = s.split(' ') 
   for i in l:
       print(i.title(), end= ' ')

s = input()
solve(s)