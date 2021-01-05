from collections import OrderedDict #for dictionary to be in order

#dictionary = {'zzz': "key"}
Language = {'c#':3 ,'C++' :5,'Python1':4 , 'Python2.7' :2,'java':1 ,'ReactJS':6} # :@ = keys
print(Language['Python1']) 
print(Language.get('Python1'))
print(Language.get('Python')) #get

##################

contacts = {
    'satu' : [43413214, 'satu@sgsfs.com'],
    'adu ' : [31312153, 'adu@dsad\.com']
}
print(contacts['satu'])
nestedcontacts = {
    'satu' : { 'phone' :43413214, 'email' : 'satu@sgsfs.com'},
    'adu ' : { 'phone' :31312153, 'email' :'adu@dsad\.com'}
}
print(nestedcontacts['satu'])

####################
dic ={}

sentence = "i like your if   sketchers you you if like my gucci shoes i buy u the purso if you show me your if boobs "
senlist = sentence.split()
senlist.sort()
for i in range(len(senlist)-2):
     if senlist[i] == senlist[i+1]:
        dic[senlist[i]] = senlist.count(senlist[i])
        
        
        
print()     
print(dic)
print(senlist)

########################
  
#print()
#print(Language.items()) #.items() returns tuple
#print(Language.keys()) #.keys()  returns keys 
#print(Language.values())# returns content

#dict.pop(key)
#dict.popitem() pops last item
#dict.clear() wipe out everything

Language.popitem()
print(Language)
print(sorted(list(Language.values())))
