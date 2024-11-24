(1)..

****
 ****
  ****
   ****

n = 4

for i in range(0,n,+1):
    for j in range(i):
        print(" ", end="")
    
    for star in range(n):
        print("*", end="")
    
    print()
--------------------------------------------------------------------
(2)..

******
*    * 
     
*    *
******

rows = 4
cols = 6
for i in range(rows):
    if i == 0 or i == rows -1:
        print('*' * cols)
    else:
        print('*' + ' ' * (cols - 2) + '*')s
---------------------------------------------------------------------
(3)..
A
AB
ABC
ABCD
ABCDE

n = 5

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(chr(64 + j), end="")
    print()

----------------------------------------------------------------------------
(4)..
A
BB
CCC
DDDD
EEEEE

n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(chr(64 + i), end="")
    print()
-----------------------------------------------------------------------------

(6)..
        * 
      * *
    * * *
  * * * *
* * * * *

for i in range(5,0,-1):
    for j in range(1,i):
        print(" ",end=" ")
    for star in range(i,6):
        print("*",end=" ")
    print()
---------------------------------------------------------------------------
(7)
     1
    12
   123
  1234
 12345

for i in range(1,5+1):
    print(" " * (5 - i), end=" ")
    
    for j in range(1, i + 1):
        print(j, end="")
    
    print()
------------------------------------------------------------------------------
(8)
 
12345
  1234
   123
    12
     1

for i in range(5,0,-1):
    for k in range(5-i):
        print(" ", end="")
    
    for j in range(1, i + 1):
        print(j, end="")
    
    print()
-----------------------------------------------------------------------------
(9)

ABCDE
  ABCD
   ABC
    AB
     A

for i in range(5,0,-1):
    for k in range(5-i):
        print(" ", end="")
    
    for j in range(1, i + 1):
        print(chr(64+j), end="")
    
    print()
-----------------------------------------------------------------------------
(10)

     *****
    *****
   *****
  *****
 *****
for i in range(1,6):
    for k in range(5-i):
        print(" ", end="")
    
    for j in range(1, 5 + 1):
        print("*", end=" ")
    
    print()

--------------------------------------------------------------------------
(11)..

     1 2 3 4 5 
    1 2 3 4 5
   1 2 3 4 5
  1 2 3 4 5
 1 2 3 4 5

for i in range(1,6):
    for k in range(5-i):
        print(" ", end="")
    
    for j in range(1, 5 + 1):
        print(j, end=" ")
    
    print()
----------------------------------------------------------------------------
(12)..
     A B C D E 
    A B C D E
   A B C D E
  A B C D E
 A B C D E

for i in range(1,6):
    for k in range(5-i):
        print(" ", end="")
    
    for j in range(1, 5 + 1):
        print(chr(64+j), end=" ")
    
    print()

------------------------------------------------------------------------------
(13)..

*
**
***
****
***
**
*

for i in range(1,6):
 for j in range(1,i-1):
    print("*",end="")
 print()
for i in range(1,6):
  for j in range(5,i,-1):
    print("*",end="")
  print()
---------------------------------------------------------------------------
(14)..

   *
  **
 ***
****
 ***
  **
   *

for i in range(3,0,-1):
 for j in range(0,i):
    print(" ",end="")
 for star in range(i,4):
    print("*",end="")
 print()
for i in range(1,6):
 for k in range(1,i):
    print(" ",end="")
 for j in range(5,i,-1):
    print("*",end="")
 print()

------------------------------------------------------------------------------

(15)..

1 
1 2
1 2 3
1 2 3 4
1 2 3 4 5

for i in range(1,5+1):
 for j in range(1,i+1):
    print(j,end=" ")
 print()
------------------------------------------------------------------------------
(16)
    1 
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5

for i in range(1,6):
  for space in range(5,i,-1):
      print(" ",end="")
  for j in range(1,i+1):
      print(j,end=" ")
  print()
----------------------------------------------------------------------------
(17)..

1 
1 2
1  3
1   4
1 2 3 4 5

for i in range(1,5+1):
 for j in range(1,i+1):
     if j==1 or j==i or i==5:
        print(j,end=" ")
     else:
        print(" ",end="")
 print()
----------------------------------------------------------------------------
(18)

    1 2 3 4 5 
    1 2 3 4
    1 2 3
    1 2
    1
for i in range(7,1,-1):
  for space in range(1,5):
      print(" ",end="")
  for j in range(1,i-1):
      print(j,end=" ")
  print()
-----------------------------------------------------------------------------
(18)..
   * 
  * *
 * * *
* * * *

for i in range(1,5):
 for k in range(i,4):
     print(" ",end="")
 for j in range(1,i+1):
     print("*",end=" ")
 print()
------------------------------------------------------------------------------
(19)..

1 2 3 4 5 
2     5 
3   5 
4 5 
5 
for i in range (1,5+1):
    for j in range(i,5+1):
        if i==1 or j==i or j== 5:
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()

-----------------------------------------------------------------------------
(20)..
   * 
  * *
 * * *
* * * *
* * * *
 * * *
  * *
   *
for i in range(1,5):
 for k in range(i,4):
     print(" ",end="")
 for j in range(1,i+1):
     print("*",end=" ")
 print()
for i in range(6,0,-1):
 for k in range(i,5+1):
     print(" ",end="")
 for j in range(1,i-1):
     print("*",end=" ")
 print()
------------------------------------------------------------------------------
(21)..
        1 
      1 2 3
    1 2 3 4 5
  1 2 3 4 5 6 7
1 2 3 4 5 6 7 8 9
  1 2 3 4 5 6 7
    1 2 3 4 5
      1 2 3
        1

for i in range(1,5):
 for k in range(5-i):
     print(" ",end=" ")
 for j in range(2*i-1):
     print(j+1,end=" ")
 print()
for i in range(5,0,-1):
 for k in range(5-i):
     print(" ",end=" ")
 for j in range(2*i-1):
     print(j+1,end=" ")
 print()
------------------------------------------------------------------------------
(22)..

1 2 3 4 5 6 7 8 9 
  1 2 3 4 5 6 7
    1 2 3 4 5
      1 2 3
        1
      1 2 3
    1 2 3 4 5
  1 2 3 4 5 6 7
1 2 3 4 5 6 7 8 9

for i in range(5,1,-1):
 for k in range(5-i):
     print(" ",end=" ")
 for j in range(2*i-1):
     print(j+1,end=" ")
 print()
for i in range(1,6):
 for k in range(5-i):
     print(" ",end=" ")
 for j in range(2*i-1):
     print(j+1,end=" ")
 print()
--------------------------------------------------------------------------
(23)..

A B C D E F G H I 
  A B C D E F G
    A B C D E
      A B C
        A
      A B C
    A B C D E
  A B C D E F G
A B C D E F G H I

for i in range(5,1,-1):
 for k in range(5-i):
     print(" ",end=" ")
 for j in range(2*i-1):
     print(chr(64+j+1),end=" ")
 print()
for i in range(1,6):
 for k in range(5-i):
     print(" ",end=" ")
 for j in range(2*i-1):
     print( chr(64+j+1),end=" ")
 print()
-----------------------------------------------------------------------------
(24)..
* * * * *
*       *
*       *
*       *
* * * * *
for i in range(1,6):
    for j in range(1,6):
        if i == 0 or i == 1 or i==5 or j == 0 or j == 1 or j==5:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
--------------------------------------------------------------------------------
(25)..
A B C D E 
A       E
A       E
A       E
A B C D E

for i in range(1,6):
    for j in range(1,6):
        if i == 0 or i == 1 or i==5 or j == 0 or j == 1 or j==5:
            print(chr(64+j), end=' ')
        else:
            print(' ', end=' ')
    print()
---------------------------------------------------------------------------------
(26)..
1 2 3 4 5 
1       5
1       5
1       5
1 2 3 4 5

for i in range(1,6):
    for j in range(1,6):
        if i == 0 or i == 1 or i==5 or j == 0 or j == 1 or j==5:
            print(j, end=' ')
        else:
            print(' ', end=' ')
    print()
--------------------------------------------------------------------------------------
(27).. 

        * 
      *   *
    *       *
  *           *
*               *
  *           *
    *       *
      *   *
        *


n = 5

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    
    print("*", end=" ")
    
    if i > 0:
        for j in range(2 * i - 1):
            print(" ", end=" ")
        print("*", end=" ")
    
    print()

for i in range(n - 2, -1, -1): 
    for j in range(n - i - 1):
        print(" ", end=" ")
    
    print("*", end=" ")
    
    if i > 0:
        for j in range(2 * i - 1):
            print(" ", end=" ")
        print("*", end=" ")
    
    print()
-----------------------------------------------------------------------------
