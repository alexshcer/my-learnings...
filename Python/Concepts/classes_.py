class operation :
    def __init__(self,n1,n2): #constructor (creartes global variable for class)
        self.num1 = n1
        self.num2 = n2
        
    def add(self):
        return self.num1+self.num2
    def sub(s):
        return s.num1-s.num2
    def multi(m):
        return m.num1*m.num2


obj = operation(3,4)
print(obj.add())
print(obj.sub())
print(obj.num1)
print(obj.multi())

