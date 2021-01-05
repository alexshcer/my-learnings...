#def rangoli(n):
#    test_list = [] 
#    dash = []
#    alpha = 'a'
#    for i in range(0, 26): 
#        test_list.append(alpha) 
#        alpha = chr(ord(alpha) + 1) 
#    #for i in range(0, 26): 
#    #    dash.append('-') 
#    #
#    #for i in range(2*n-1):
#    #    dash[13]= test_list[n-1]
#    #    print()
#    #    for k in range(26) :
#    #        print(dash[k] ,  end= "")
#    s=n
#    #while dash[-2] == 'a':
#    while (s-1)!=-1 :
#        dash.append(test_list[s-1]) 
#        dash.append('-')
#        s -= 1 
#    for i in range(len(dash)):
#        dash.append(dash[len(dash-i)])
#    print(dash)
#
#
#    return
#
#n = int(input())
#rangoli(n)
import string
def print_rangoli(size):
    alpha = string.ascii_lowercase

    n = size
    L = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    print('\n'.join(L[:0:-1]+L))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)