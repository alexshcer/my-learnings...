#tuple cant be modified 
#tuple use()
cc1 = (14124544525423, "EPAX" ,"03/21" , 510)
cc2 = (35424524525423, "XfwAPE" ,"01/24" , 620)
cc3 = (3542624525423, "XwfAPE" ,"01/24" , 290)
cc4 = (35424524525423, "XgfwAPE" ,"01/24" , 420)
cc5 = (354264525423, "XArgewrPE" ,"03/24" , 720)
ccs = [cc1,cc2,cc3,cc4,cc5]

#no , name , expdate , cvv = cc1

#print(no)
#print(name)
#print(cvv) 
#print()
for no, name, expdate, cvv in ccs:
    print(no)
    print(name)
    print(cvv) 
    print()