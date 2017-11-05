# Iterative Deepening Depth-First Search
General strategy to find the best depth limit for a search, where searching the entire tree is infeasible.
* Gradually increases the depth limit from 0..*d* until a goal/cutoff is found/met.

## Pseudocode
Terminates if:
* Solution is found
* depth-limited-search returns *failure* -> no solution exists
```
function ITERATIVE-DEEPENING-SEARCH(problem) returns a solution, or failure
for depth = 0 to infinity:
    result = DEPTH-LIMITED-SEARCH(problem, depth)
    if result != cutoff then return result
```

## Complexity
* *b* = branching factor
* *d* = depth
* Memory complexity = **O(bd)** -> same as DFS
* Time complexity = **O(b<sup>d</sub>)**

Each iteration, the previous levels are **generated again**.
* States are generate multiple times

Not very costly -> the problem is **exponential time**
* Most nodes are at the bottom level of the tree
    * Given a constant/near constant branching factor
* Nodes at the bottom are generated once, one level above twice etc.
    * Time complexity: N(IDS) = (d)b + (d-1)b<sub>2</sup> + ... + (1)b<sup>d</sup>

## For Isolation Game
* Cutoff = time limit for search i.e 2 secs
* Run iterative deepening search and save the best move found so far at each iteration.
* When time limit is reached -> return best move found up to that point

