# mutable = change ability(Changeable) eg: lists , dictionaries(keys are immutable)
# immutabe = cantchange ability(inChangeable) eg: tuple , int ,floats , booleans

t = (1 ,2 , [1 ,2 ,3 ])
t[2][1] = 4 #changing content of list 
print(t)
t[2][2] = 5
t[2][0] = 3
print(t)
