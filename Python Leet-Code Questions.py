#PYTHON  LEET-CODE  QUESTIONS.......

#1.)vaild anagram
#2.)isomorphic or not 
#3.)vaild parantheses..
#4.)time-to-buy-and-sell-stock
#5.)two sum
#6.)three sum

#1.) Vaild anagram or not....
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
    print("not anagram") '''


#2.)isomorphic or not....
'''s="pep"
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
    print("not isomorphic")'''
 
# Second method to check ismorphic or not with using zip function...
'''s="zac"
y="hey"
dict1={}
for i in zip(s,y):
    s1,s2=i
    if(s1 in dict1 and dict1[s1]!=s2):
       print(" Not isomorphic")
       dict1[s1]=s2
print("isomorphic")'''


#3.) Question name => Vaild Parenthesis..
'''data="{[]}"
mylist=[]
x=0
for char in data:
  if char in "[({":
    mylist.append(char)
  elif(mylist):
    if(char=="}" and mylist.pop()!="{"):
      x=1
      break
    elif(char=="]" and mylist.pop()!="["):
     x=1
     break
  else:
    x=1
    break
if(x==0 and len(mylist)==0):
  print("vaild")
else:
  print("invaild")'''


#4.)#time-to-buy-and-sell-stock question with using min and max function....
'''mylist=[7,1,5,3,6,4]
profit=0
min_price=mylist[0]
for i in range(len(mylist)):
    profit_margin=mylist[i]-min_price

    profit=max(profit,profit_margin)
    #print(min_price,mylist[i])
    min_price=min(min_price,mylist[i])

print(profit)'''

# Input: List of stock prices
'''prices = [7, 1, 5, 3, 6, 4]
max_profit = 0
min_price = prices[0]
i = 1
while i < len(prices):
    if(prices[i] < min_price):
        min_price = prices[i]
    else:
        profit = prices[i] - min_price
        if(profit > max_profit):
            max_profit = profit
    i += 1
print("The maximum profit is:", max_profit)'''


#two sum ..
'''nums=[1,2,3,7,11,15]
target=9
for x in range(0,len(nums)):
    print(x,nums[x])
    for y in range(x+1,len(nums)):
     if(nums[x]+nums[y]==target):
        print(x,y)
        break'''


#three sum..
'''nums = [-1, 0, 1, 2, -1, -4]
nums.sort()
for i in range(0,len(nums)):
   j=i+1
   k=len(nums)-1
   while(j<k):
      if(nums[i]+nums[j]+nums[k]==0):
         print(i,j,k)
         j+=1
      elif((nums[i]+nums[j]+nums[k]>0)):
        k+-1
      else:
        j+=1'''


'''nums = [-1, 0, 1, 2, -1, -4]
nums.sort()
for i in range(0,len(nums)):
    j=i+1
    k=len(nums)-1
    while(j<k):
        if(nums[i]+nums[j]+nums [k]==0):
            print(i,j,k)
            j+=1
        elif(nums[i]+nums[j]+nums[k]>0):
            k+-1
        else:
            j+=1'''

       

#Three sum leetcode..
'''nums = [-1, 0, 1, 2, -1, -4]
nums.sort()
for i in range(len(nums)):
    if i > 0 and nums[i] == nums[i - 1]:
        continue
    j, k = i + 1, len(nums) - 1
    while j < k:
        total = nums[i] + nums[j] + nums[k]
        if total == 0:
            print(nums[i], nums[j], nums[k],end='')
            j += 1
            k -= 1
            while j < k and nums[j] == nums[j - 1]:
                j += 1
            while j < k and nums[k] == nums[k + 1]:
                k -= 1
        elif total > 0:
            k -= 1
        else:
            j += 1'''


#Three sum close code leetcode..
nums=[-1,2,1,-4]
nums.sort()
target=1
diff=float('inf')
for i in range(0,len(nums)-2):
  start=i+1
  end=len(nums)-1
  while start<end:
    t_sum=nums[i]+nums[start]+nums[end]
    if abs(t_sum-target) < abs(target-diff):
      dif=t_sum
    if(t_sum<target):
      start+=1
    elif(t_sum>target):
      end-=1
print(t_sum)


