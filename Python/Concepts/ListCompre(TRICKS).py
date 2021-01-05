#List Comprehension (Tricks and Tips)
names =['breach' , 'sova' , 'omen', 'killjoy' , 'cypher'] 
l = []
for agent in names : #long method
    l.append(agent)
print(l)

print([agent for agent in names]) #cool litle trick
print()
l = []
for agent in names : #long method
    l.append(agent + ' Selected')
print(l)

print([agent + ' Picked' for agent in names])
##########

gunsANDratings = {"operator": 5, 'vandal' : 4.5, 'phantom': 4.6 , 'spector' : 3}
l = []
for guns in gunsANDratings: #long
    if gunsANDratings[guns] > 3:
        l.append(guns)
print(l)

print([guns for guns in gunsANDratings if gunsANDratings[guns]>3])


