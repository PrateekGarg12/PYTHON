(1)..
a=int(input("enter the even number"))

while(a<=100):
 print(a)
 a=a+2

output=enter the even number2
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
52
54
56
58
60
62
64
66
68
70
72
74
76
78
80
82
84
86
88
90
92
94
96
98
100
----------------------------------------------------------
(2)..
n = int(input("Enter a number: "))
sum= 0
i = 1
while i <= n:
    sum =sum+i
    i =i+2
print("The sum of all odd numbers 1 to n:", sum)

output==Enter a number: 10
The sum of all odd numbers 1 to n: 25
-------------------------------------------------------------
(3)..
n=int(input("enter the number"))
i=1
while i<n:
  print(i)
  i=i+1
output==enter the number10
1
2
3
4
5
6
7
8
9
---------------------------------------------------------------
(4)..
a=int(input("enter the number"))
while a>0:
  print(a)
  a=a-1
output==enter the number10
10
9
8
7
6
5
4
3
2
1
(5)..
n=int(input("enter the number"))
count=0
while n>0:
  count=count+1
  n=n//10
print(count)
output==enter the number1547
4
---------------------------------------------------------------------
(6)..
n=int(input("enter the number"))
sum=0
while(n>0):
  sum=sum+n
  n=n-1
print(sum)
output==enter the number5
15
---------------------------------------------------------------------
(7)..
n=int(input("enter the number"))
sum=0
first=n
last=n%10
while first>9:
  sum=sum+first%10
  first=first // 10
  sum=last+first%10
print("the first of digit",first)
print("the last of digit",last)
print("the sum of first and last digit number ",sum)

output==enter the number10887
the first of digit 1
the last of digit 7
the sum of first and last digit number  8
-------------------------------------------------------------------------
(8)..
n=int(input("enter the number"))
i=n
sum=0
while n>0:
  sum=sum*10+n%10
  n=n//10
print(sum)

output==enter the number1045
5401
(9)..
n=int(input("enter the number"))
first=n
last=n%10
while first>9:
  first=first // 10
  sum=last+first%10
print("the first of digit",first)
print("the last of digit",last)

output==enter the number1547
the first of digit 1
the last of digit 7
--------------------------------------------------------------------------
(10)..
a=int(input("enter the number"))
b=int(input("enter the number"))
c=1
for i in range(1,b+1):
  c=c*a
print(c)
output==enter the number3
enter the number4
81
---------------------------------------------------------------------------
(11)..
a=int(input("enter the number"))
for i in range(1,a+1):
  if(a%i==0):
    print(i)
output==enter the number10
1
2
5
10
---------------------------------------------------------------------------
(12)..
a=int(input("enter the number"))
fact=1
while a>0:
  fact=fact*a
  a=a-1
print(fact)

output==enter the number5
120
---------------------------------------------------------------------------
(13)..
a=int(input("enter the number"))
b=int(input("enter the number"))
if a>b:
   c=a
else:
   c=b
while True:
   if c%a==0 and c%b==0:
     lcm=c
     break
     c=c+1
print(lcm)

output== enter the number:54
enter the number:24
216


--------------------------------------------------------------------
(14)..n=int(input("enter the number"))
for i in range(2,n):
  if(n%i==0):
    print("not prime")
    break
else:
  print("prime")

output==enter the number11
prime
-----------------------------------------------------------------
(15)..

a=int(input("enter the number"))
for i in range(2,a+1):
    j=2
    for j in range(2,i):
        if(i%j==0):
           j=i
           break;
    if(j!=i):

     print(i)
output== enter the number:6
3
5
-----------------------------------------------------------------------
(16)..
a=int(input("enter the number"))
factor=2
while(a>1):
 if a%factor==0:
  print(factor)
  a=a//factor
 else:
  factor-=factor+1

output==enter the number10
2
5
--------------------------------------------------------------------------
(17)..
n=int(input("enter the number:"))
tem=n
sum=0
while(n>0):
  ren=n%10
  sum=sum+ren*ren*ren
  n=n//10

if(tem==sum):
    print("armstrong number")
else:
    print("not armstrong number")

output==enter the number:371
armstrong number
--------------------------------------------------------------------------
(18)..
num = int(input("Enter a number: "))
b= num
sum = 0

while num > 0:
    digit = num % 10 
    fact = 1
    i = 1
    while i <= digit:
        fact *= i
        i += 1
    sum += fact 
    num //= 10 

if sum== b:
    print(f"{b} is a Strong number.")
else:
    print(f"{b} is not a Strong number.")

output==Enter the number:145
145 is a strong number.
--------------------------------------------------------------------------
(19)..num = int(input("Enter a number: "))
sum = 0
d = 1

while d < num:
    if num % d == 0: 
        sum += d
    d += 1

if sum == num:
    print(f"{num} is a Perfect number.")
else:
    print(f"{num} is not a Perfect number.")

output==Enter the number:6
6 is a perfect number.
--------------------------------------------------------------------------
(20)..
n = int(input("Enter the number of terms: "))

a, b = 0, 1
count = 0

while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1

output==Enter the number:8
0 1 1 2 3 5 8 13
--------------------------------------------------------------------------