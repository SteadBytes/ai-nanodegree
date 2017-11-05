# Alpha Beta Pruning
Decreases the number of nodes evaluated by Minimax

Cuts off (prunes) branches in the game tree which need not be searched as a better move has already been found.

## Basic Premise
Given any node *n* in the tree that Player has a choice of moving to:
* If Player has a better choice *m* either:
    * At the parent node of *n*
    * At any point further up in the tree
* *n* will **never be reached** in actual play
    * When playing optimally, the worse move will never be chosen

## Algorithm
Alpha Beta tracks the **bounds** on the backed-up values in order to prune the tree:
* &alpha; = value of best choice found so far at any point along search path for **MAX**
    * i.e. highest value
* &beta; = value of best choice found so far at any point along search path for **MIN**
    * i.e. lowest value

The values of alpha and beta are updated as the search progresses

If values of current node is known to be worse than current alpha/beta values for MAX/MIN the branches from the node can be pruned.


## Pseudocode
Alpha-Beta Search is a **modification of minimax** algorithm:
```
function ALPHA-BETA-SEARCH(state) returns an action
v = MAX-VALUE(state, -infinity, +infinity)
return the action in Actions(state) with value v

function MAX-VALUE(state, alpha, beta) return a utility value
if TERMINAL-TEST(state) then return UTILITY(state)
v = -infinity
for each a in Actions(state):
    v = Max(v, MIN-VALUE(Result(s,a), alpha, beta))
    if v >= beta then return v
    alpha = Max(alpha, v)
return v

function MIN-VALUE(state, alpha, beta) return a utility value
if TERMINAL-TEST(state) then return UTILITY(state)
v = +infinity
for each a in Actions(state):
    v = Min(v, MAX-VALUE(Result(s,a), alpha, beta))
    if v <= alpha then return v
    beta = Min(beta, v)
return v
```