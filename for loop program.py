(1)..
n= int(input("Enter a number: "))

print(f"Factors of {n} are:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i)

output==Factors of 8:
1
2
4
8
---------------------------------------------------------------------------
(2)..
# Given values
current_population = 10000
growth_rate = 1.10 

for year in range(10, 0, -1):
    population = current_population / (growth_rate ** (10 - year))
    print(f"{year}th year => {int(population)}")

output==10th year => 10000
9th year => 9090
8th year => 8264
7th year => 7513
6th year => 6830
5th year => 6209
4th year => 5644
3th year => 5131
2th year => 4665
1th year => 4240
----------------------------------------------------------------------------
(3)...

n=int(input("enter the prime number"))
for i in range(2,n):
    if n%i==0:
        print("not a prime number")
        break
else:
    print("prime number")

output==enter the number:7
prime number
------------------------------------------------------------------------------
(4)..
num1 = int(input("enter the first number"))
num2 =int(input("enter the second number"))
for i in range(max(num1, num2), 1 + (num1 * num2)):
    if i % num1 == i % num2 == 0:
        lcm = i
        break
print("LCM of", num1, "and", num2, "is", lcm)

output== enter the first number:12
         enter the second number:14
         LCM of 12 and 14 is 84
---------------------------------------------------------------------------
(5)..
num1 = int(input("enter the first number"))
num2 = int(input("enter the second number"))
hcf = 1

for i in range(1, min(num1, num2)):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i
print("Hcf of", num1, "and", num2, "is", hcf)

output==enter the first number36
enter the second number60
Hcf of 36 and 60 is 12
------------------------------------------------------------------------
(6)..
n = int(input("Enter a number n: "))

sum= 0

for i in range(1, n + 1):
    sum =sum + i

print(f"The sum of the first {n} numbers is: {sum}")

output==Enter a number n: 10
The sum of the first 10 numbers is: 55
-----------------------------------------------------------------------
(7)..
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

c = 0

for i in range(b):
    c = c + a

print(f"The multiple of  is two number {a} and {b} is: {c}")

output==Enter first number: 3
Enter second number: 5
The multiple of  is two number 3 and 5 is: 15
----------------------------------------------------------------------
(8)..
num = int(input("Enter a number: "))

fact = 1

for i in range(1, num + 1):
    fact = fact * i  
print(f"The factorial of {num} is: {fact}")

output==Enter a number: 5
The factorial of 5 is: 120
---------------------------------------------------------------------------
(9)..
num = int(input("Enter a number: "))

count = 0

while num > 0:
    num //= 10
    count= count+ 1  

print( count)

output==
enter the number:75869
5
------------------------------------------------------------------------------
(10)..
total= 0
count = 0

while True:
    num = int(input("Enter a number (enter 0 to stop): "))
    
    if num == 0:
        break
    
    total= total+num
    count= count+1

if count > 0:
    average = total/ count
    print(f"Sum of the numbers: {total}")
    print(f"Average of the numbers: {average}")
else:
    print("No numbers were entered.")

output==Enter a number (enter 0 to stop): 5
Enter a number (enter 0 to stop): 10
Enter a number (enter 0 to stop): 15
Enter a number (enter 0 to stop): 0
Sum of the numbers: 30
Average of the numbers: 10.0
----------------------------------------------------------------------------
(11)..
num = int(input("Enter a table: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

output==Enter a table: 2
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20
------------------------------------------------------------------------------
(12)..
a = 0
b = 1

for i in range(10):
    print(a, end=" ") 
    a, b = b, a + b 

output==0 1 1 2 3 5 8 13 21 34 
------------------------------------------------------------------------------
(13)..
for i in range(1, 5):
    for j in range(i + 1, 5):
        print(f"({i},{j})")

output==(1,2)
(1,3)
(1,4)
(2,3)
(2,4)
(3,4)
------------------------------------------------------------------------------
(14)..
for i in range(1, 6):
    print(i)

else:
    print("Done")

output==
1
2
3
4
5
Done
------------------------------------------------------------------------------
