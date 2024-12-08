#first question..
mydictionary={"amount":0}
for i in range(1,11):
  mydictionary["amount"]= mydictionary["amount"]+1
print(mydictionary)

#second question..
mydictionary={"hello":0}
for i in mydictionary:
  mydictionary[i]=mydictionary[i]+1
print(mydictionary)

#third question..
mydictionary={"amount":0}
for i in "hello":
  mydictionary["amount"]= mydictionary["amount"]+1
  print(i)

#fourth question..
mydictionary={"amount":0}
for i in "hello":
  if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
    print(i)

#fifth question..
a={}
for char in "hey":
  a[char]=1
print(a)

#sixth question..
mydictionary={}
for char in "heeehyy":
  if chr not in mydictionary:
    mydictionary[char]=1

print(mydictionary)

#seventh question..
mydictionary={}
data="heeehyy"
for i in data :
  if i not in mydictionary:
    mydictionary[i]=1
  elif(i in mydictionary):
    mydictionary[i]=mydictionary[i]+1
print(mydictionary)

#eight program...




