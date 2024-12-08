#first question..
a=[]
#for i in a:
a.append(1)
a.append(2)
a.insert(1,3)
print(a)

#second question..
a=[]
x=int(input("Enter how many number to input: "))
for i in range(x):
    n=int(input("Enter the number: "))
    a.append(n)
print("maximum number is: ",max(a))
print("minimum number is: ",min(a))

#third program..
list=[]
sum=0
x=int(input("Enter how many number to input: "))
for i in range(x):
  n=int(input("Enter the number: "))
  list.append(n)
print("list is: ",list)
for j in list:
    sum=sum+j
print("sum= ",sum)

#fourth program  first and last character same..
list=[]
ch=0
a=int(input("Enter how many number to input: "))
for i in range(a):
    n=input("Enter elements: ")
    list.append(n)
print("List is: ",list)   
for j in list:
    if len(j)>1 and j[0]==j[-1]:
        ch=ch+1
print(ch)

#fifth program remove duplicate element in list..
list=[]
dup=[]
a=int(input("Enter how many number to input: "))
for i in range(a):
    n=int(input("Enter the number: "))
    list.append(n)
print("Orignal list is: ",list)
for j in list:
    if j not in dup:
        dup.append(j)
print("After remove duplicate element list is: ",dup)

#sixth program find list is empty or not..
list=[1,3,4,5,6,7]
if not list:
    print("list is empty")
else:
    print("not empty")

#seventh program find list have any one common number..
list1=[]
list2=[]
result=False
a=int(input("Enter how many number to input: "))
for i in range(a):
    n=int(input("Enter the number: "))
    list1.append(n)
print("Elements in list1: ",list1)

b=int(input("Enter how many number to input: "))
for j in range(b):
    num=int(input("Enter the number: "))
    list2.append(num)
print("Elements in list2: ",list2)

for x in list1:
    for y in list2:
        if x==y:
            result=True
            print(result)
if result:
    print("List have at lest one common number")
else:
    print("list have no any common number")

#Eight program print specefic list after remove even number..
list1=[]
list2=[]
a=int(input("Enter how many number to input: "))
for i in range(a):
    n=int(input("Enter the number: "))
    list1.append(n)
print("Elements in list1: ",list1)
print("After remove even elements list is -:")
for x in list1:
    if(x%2!=0):
        list2.append(x)
print(list2,end=' ')

#Nineth Program find element's position..
list1=[]
a=int(input("Enter how many number to input: "))
for i in range(a):
    n=int(input("Enter the number: "))
    list1.append(n)
print("list= ",list1)
print("Element found at ",list1.index(5),"Position")

#Tenth program 
list1=['apple','banana','orange','grappes']
list2=[1,2,3,4]
cal=list1+list2
print(cal)

#Elventh program..
num=(input("Enter any number: "))
if(num=='a'):
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    c=a+b
    print(c)
elif(num=='s'):
    x=int(input("Enter first number: "))
    y=int(input("Enter second number: "))
    z=x-y
    print(z)
elif(num=='m'):
    m=int(input("Enter first number: "))
    n=int(input("Enter second number: "))
    t=m*n
    print(t)
else:
    print("select vaild character")



#palindrome program in python
name="saras"
first=0
last=len(name)-1
out=0
while(first<last):
    if(name[first]!=name[last]):
        out=1
        break
    first=first+1
    last=last-1
if(out==1):
    print("not palindrome")
else:
    print("palindrome")


