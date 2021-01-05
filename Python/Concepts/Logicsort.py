def ss(a):
    
    n = len(a)


    print()
    print(a)
    for i in range(0,n-1):
        j=i
        while a[j+
        1] < a[j] :
          temp = a[j]
          a[j] = a[j+1]
          a[j+1] = temp
          if j>0:
             j -= 1
          else:
             break


    
