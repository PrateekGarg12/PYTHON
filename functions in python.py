#functions in python..

'''def hello():
    print("piyush")
    print("tushar")
hello()'''


'''def addno():
    x=10  #x and y are local variable ..
    y=20
    print(x+y)
addno()'''


'''z=30 #z is global variable..
def addno():
    x=10  #x and y are local variable ..
    y=20
    print(x+y+z)
addno()'''


'''#if we change the global variable value then we use 'global keyword'...
z=50
def addno():
    global z
    x=10  #x and y are local variable ..
    y=20
    print(x+y+z)
addno()
print(z)'''


'''#passing parameter in function..
def addno(x,num): #'x and num' are local variable because these variables are inside of the function
    print("x= ",x,"num= ",num)
addno(40,60)'''


#memory address => memory address are changed when we not stored ane variable into another variable
#but we change one variable into another variable then the address of both variable are change...
#example
'''x=40
y=20
x=y
print(id(x))
print(id(y))'''

'''#second example..
def sum123(x):
    print("old x",x)
    x=20
    print("new x",x)
z=30
sum123(z)'''


#NOTE -:
#lifecycle of the variable...
#mutable local mein changes global mein bhi dhikenge
#immutable mein local ke changes global mein nahi dhikenge..

#Example of note...
'''def func(x):
    print("x: ",x)
    x.append(999)

mylist=[10,20,30,40,50]
func(mylist)
print(mylist)'''


#what is return with example..
#return function ke andar hi chalta hai bahar nahi..
#return gives the final value.. like these example they give 100
#bydefault function give the 'none'

'''def func(x):
    return x+20
out=func(80)
print('out= ',out)'''

'''def check(x):
    if(x%2==0):
        return True
    else:
        return False
out=check(23)
print(out)'''

#------------------------------------------------------------------------------
# Function questions...

#1.) Fibonacci Series in python..
'''def fibo():
    num=int(input("Enter any number: "))
    n1=0
    n2=1
    print("Fibonacci Series: ",n1,n2,end=' ')
    for i in range(2,num):
        n3=n1+n2
        n1=n2
        n2=n3
        print(n3,end=' ')
    print()
fibo()'''

#2.) Check the number is palindrome or not..
'''def palin(num):
    sum=0
    temp=num
    while(num>0):
        rem=num%10
        sum=sum*10+rem
        num=num//10
    if(temp==sum):
        print("Palindrome number")
    else: 
        print("Not Palidrome number")
palin(121)'''

#3.) take input any string from user and convert the first and last word of the string as capital...
'''str="hello world"
print("String before:", str)
string = ""
for i in str:
    string += (i[:-1] + i[-1].upper()) + ' '
print("String after:", string.strip())'''


#4.) print pyramid with create function..
'''def pattern(rows):
    for i in range(1,rows):
        for s in range(1,(rows-i)):
            print(" ",end='')
        for j in range(i):
            print("* ",end='')
        print("")
pattern(6)'''


#pasing parameters in function..
#type of argument 1.) Required argument..  jitne parameter utne argument
'''def fun(id,name,age):
    print("details are: ",id,name,age)
fun(1,"tushar",16)'''


#2.)postion argument=> jis jagah position ho usi jagh dena
'''def fun(id,name,age):
    print("details are: ",id,name,age)
fun(16,"tushar",1)'''

#3.) Keyword argument..
'''def fun(id,name,age):
    print("details are: ",id,name,age)
fun(id=16,name="tushar",age=1)'''# keyword diya hai yaha jaise id= ,name=,age=..

#4.) Default argument=> kuch bhi default argument denge..
'''def fun(id,name,age=100):
    print("details are: ",id,name,age)
fun(16,"tushar",)''' #yaha kuch bhi value nahi di toh yeh automatically default argument lele ga jo hamne function mein di hai...


#Variable length argument...jo bhi parameter pass hoga vo tuple form mrin hoga
def func(*x):
    print("details are: ",x)
func(10,30,'b',5,6) #yaha multiple arguments de sakte hai ek parameter ke through with the help of (*) these operator

#keyword variable length argument...=>  data provide kar rahe the uska 
# isme two * lagte hai aur isme jo argument pass hote hai vo dictionary form mein hote hai..
def func(**x):
    print("details are: ",x,type(x))
func(id=10,name="hey",salary=20000)
func(id=100)

#(*args)=>keywords argument ko args bhi bolte hai
#(**kwargs)=>keyword variable length argument ko kwargs bhi bolte hai..

#learn
#high order function 
#first class function 

#first class function example
'''def square(x):
    return(x*x)
def cube(y,z):
    print(y*z(y)) #z mein square function ka address chala gaya isliye jab bhi square function call hoga yani z call ho raha hai
cube(3,square)'''

#second example of first class funtion
def square(x):
    return(x*x)
def cube(y,z):
    print(y,z(20))
cube(10,square)
