#regex is re 

import re
text = " raND0m string. swasthik.shetty10902@gmail.com x349-2_1x@xxx.net"
pattren1 = re.compile("[zrAdmC]") #u can use [A-Z] to cover entier alphabate
pattren2 = re.compile("random") 

result1 = pattren1.search(text) #search() searches for only first letter
print(result1)

result2 = pattren2.search(text)
print(result2)

pattren3 = re.compile("[a-zA-Z0-9]+") 
result3 = pattren3.search(text)
print(result3)

pattren4 = re.compile("[a-zA-Z0-9\.\-\_]+\@[a-zA-Z0-9]+\.[a-zA-Z]+")#search ofr email
result4 = pattren4.findall(text) #find all will search for more

print(result4)

