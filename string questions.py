#Palindrome string program..
a=input("Enter any word: ")
if a==a[::-1]:
    print("yes it is palindrome string")
else:
    print("no it is not palindrome string")

#count number of vowels in a string..
a=input("Enter the string: ")
vowels=0
for i in a:
 if(i=='a'or i=='e'or i=='i'or i=='o'or i=='u'or i=='A'or i=='E'or i=='I'or i=='O'or i=='U'):
    vowels=vowels+1
print("Number of vowels are: ",vowels)

#find the first occurance of a character in a string..
a="apple"
index=a.find('p')
print(index)

#convert a string to uppercase..
a=input("Enter string: ")
b=a.upper()
print(b)

a="hello world"
b=a.replace('l','w')
print(b)

a="python3"
if(a.isdigit()):
    print("true")
else:
    print("false")

a=" hello world "
b=a[1:12]
print(b)

a="banana"
b=a.find('a')
print(b)

a="abc"*3
print(a)

a="banana"
b=a.count('a')
print(b)

a="HELLO"
if(a==a.upper()):
    print("true")
else:
    print("false")

a="banana"
b=a.rfind('a')
print(b)

a="beautiful"
vowels=['a','e','i','o','u','A','E','I','O','U']
text=""
textlen=len(a)
for i in range(textlen):
    if a[i] not in vowels:
        text=text+a[i]
print("\n After removing the vowels string is: ")
a=text
print(a)

a="python programming"
print(a.endswith("ing"))

a="HeLLo"
b=a.swapcase()
print(b)

a="hello world"
b=a.replace('l','p')
print(b)

a="A"
b=a.chr()
print(b)

a=[]
size=int(input("Enter size: "))
for i in range(size):
  val=input("Enter item: ")
  a.append(val)
print(a)


for i in range(5,0,-1):
    for s in range(5-i):
        print(" ",end=' ')
    for j in range(i):
     if(j==0 or j==i-1 or i==5):
        print("*", end=' ')
     else:
        print(" ",end=' ')
    print()