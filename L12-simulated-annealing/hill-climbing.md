# Hill Climbing
General optimazation strategy for **local search**. 

* Starts with an *arbitrary* solution to a problem
* **Incrementally** changes a single element of the solution to improve solution:
    * If the change produces a better solution -> repeat incremental change on new solution
    * If no improvement found -> return answer

## Example
* One-dimensional state-space 
* **Elevation** = objective function
    * Higher = better

* From current state:
    * Calculate gradient 1 unit on either side
    * Move 1 unit in the direction of the **most positive** gradient
    * If neither gradient improves solution:
        * Return current state

![](../images/2017-11-05-11-35-57.png)

## Pseudocode
```
function Hill-Climbing(problem) -> returns a solution state
    inputs: problem = a problem
    static: current = a node
            next = a node
    
    current = Make-Node(Initial-State[problem])
    loop do
        next = highest valued successor of current
        if Value[next] < Value[current] -> return current
        current = next
    end
```

## Problems
* May **converge on local optima**
    * Not guaranteed to find **global optima**
* Plateaus can cause algorithm to terminate early or to 'wander' in incorrect direction