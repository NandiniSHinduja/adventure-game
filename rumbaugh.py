import re
name=input("Enter the file")
if len(name)<1:name='hundred.txt'
handle=open(name)
x=list()
for line in handle:
    y=re.findall('[0-9]+',line)
    x=x+y
sum=0
for i in x:
    sum=sum+int(i)
print(sum)
