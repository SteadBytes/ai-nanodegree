# n-Queens Problem
Problem of placing *n* queens on an *n x n* board, such that no queens can attack each other.

The most typical form of the problem is **8-queens**.

* Queens can attack each other if they share a row, column or diagonal
* Two queens that are able to attack are called an **attacking pair**
* **Goal** is to have **0 attacking pairs**

Total possible attacking pairs of queens = *n 'choose' 2*:
* *n!/ 2!(n-2)!*
    * Binomial coefficient
* For 8-queens problem:
    * *8!/2!(8-2)! = 28*

Fitness value:
* Total possible attacking pairs - number of attacking pairs
* The higher the value, the **fewer** attacking pairs there are on the board
* For 8-queens the optimal fitness value is **28**


## Finding Attacking Pairs
Attacking pairs = any two queens which can attak one another

Given two queens at coords *(x1,y1), (x2, y2)*, they are attacking pairs if:
* *y1 = y2*
    * Horizontally
* *x1=x2*
    * Vertically
* *|x1-x2| = |y1-y2|*
    * Diagonally

* **Input** = String of y-values in x-value order:
    * '32752411'
    * = (1,3), (2,2), (3,7), (4,5), (5,2), (6,4), (7,1), (8,1)
* **Output** = Number of attacking pairs

### Method:
* Store pairs in a set of sets:
    * Avoid duplicate pairs
* Loop over input:
    * For each other coord in input not yet search:
        * Test the two sets of coords for 'attackability':
        * If any conditions pass, create a set of the two coords, then add to pairs set
* Length of pairs set = number of attacking pairs
```Python
pos_str = '32543213'

pairs = set()

for i in range(len(pos_str)):
  q1 = (i+1,int(pos_str[i]))
  for j in range(i+1, len(pos_str)):
    pair = False
    q2 = (j+1,int(pos_str[j]))
    if q1[0] == q2[0]:
      pair = True
    elif q1[1] == q2[1]:
      pair = True
    elif abs(q1[0]-q2[0])==abs(q1[1]-q2[1]):
      pair = True
    if pair:
      pairs.add(frozenset((q1,q2)))

print(len(pairs))
```