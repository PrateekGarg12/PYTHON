'''a=[1,3,4,3,2,1,4,3,]
b=[]
for i in range(1,len(a)):
    for j in range(i+1,len(a)):
        if(a[i]==a[j]):
            if a[i] not in b:
             b.append(i)
print(b)'''
#continue use karenge..


'''mysets=set({})
myset={1,2,3,4,51,12,2,10,1}
#add use to add only single element..
myset.add(10101)
print(myset)'''

#update is use to add iterable(iterable means jispe loop chala sakte hain)..

'''myset.update("hey")
myset.update(["hey",999])
print(myset)'''

#remove and discard is use to delete the element but remove give error and discard give not error

#homework..
#1.)difference method kya karta hain..
#2.)intersection update..
#3.)issuperset..
#4.)symmetric difference..


#zip iterable value ko ek sath ikatha karta hai aur vo list bhi ho sakti hai string bhi ho sakti hai aur unhe
#hame tuple ki form mrin deta hai

#zip function and its use with help of program..
'''list1="hii"
list2="hyy"
for i in zip(list1,list2):
    print(i)'''


#check isomorphic or not code
s="pep"
y="ziz"
s_dict={}
y_dict={}
x=0
if(len(s)==len(y)):
    for index in range(0,len(s)):
        if(s[index] in s_dict and s_dict[ s[index] ]!=y[index] ):
         x=1
         break
        s_dict[s[index]]=y[index]
if(x==0):
    print("isomorphic")
else:
    print("not isomorphic")

#check isomorphic or not code using zip function
'''s="zac"
y="hey"
dict1={}
for i in zip(s,y):
    s1,s2=i
    if(s1 in dict1 and dict1[s1]!=s2):
       print(" Not isomorphic")
       dict1[s1]=s2
print("isomorphic")

'''

#anagram question...
'''s="anagram"
t="nagaram"
dict1={}
for char in s:
    if char not in dict1:
        dict1[char]=1
    else:
        dict1[char]=dict1[char]+1
dict2={}     
for char in t:
    if char not in dict2:
        dict2[char]=1
    else:
        dict2[char]=dict2[char]+1
if(dict1==dict2):
    print("anagram")
else:
    print("not anagram")    '''


#python questions..
#vaild anagram
#isomorphic or not 
#vaild parantheses..
#time-to-buy-and-sell-stock

#time-to-buy-and-sell-stock..
'''list=[7,1,5,3,6,4]
buy=list[0]
sell=list[1]
profit=0
for i in list:
    for j in range(i+1,len(list)):
        if(sell<len(list)):'''


'''list=[7,1,5,3,6,4]
buy_price=0
sell_price=1
profit=0
while(sell_price>buy_price):
'''

#
mylist=[7,1,5,3,6,4]
profit=0
min_price=mylist[0]
for i in range(len(mylist)):
    profit_margin=mylist[i]-min_price

    profit=max(profit,profit_margin)
    #print(min_price,mylist[i])
    min_price=min(min_price,mylist[i])

print(profit)

