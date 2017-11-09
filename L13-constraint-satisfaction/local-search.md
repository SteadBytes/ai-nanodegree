# Local Search for CSP's
* Use **complete state formulation**:
    * Initial state assigns a value to every variable
    * Search changes the value of one variable at a time
* Initial state will typically violate constraints
    * Local search is designed to eliminate the violated constraints
* New values for variables are chosen using a heuristic evaluation
    * **Min-conflicts** = choose value that results in the minimum number of conflicts with other variables

## Min-Conflicts CSP Local Search
* Conflicts() function counts the number of constraints violated by a particular value, given the rest of the current assignment
```
function Min-Conflicts(csp, max_steps) returns a solution or failure
    inputs: csp, a constraint satisfaction problem
            max_steps, number of steps allowed before giving up on search
    
    current = an initial complete assignment for csp

    for i =1 to max_steps:
        if current is a solution for csp:
            return current
        var = randomly chosen conflicted variable from csp.Variables
        value = the value v for var that minimizes Conflicts(var, v, current, csp)
        set var = value in current
    return failure
```
