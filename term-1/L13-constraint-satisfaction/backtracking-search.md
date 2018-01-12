# Backtracking Search CSP's
* CSP's are **commutative**
    * Assigning values to variables leads to the same partial assignments regardless of order
* Therefore can consider only a **single** variable at each node in search tree
* **Backtracking Search**:
    * Depth-first search
    * Chooses values for one variable at a time
    * Backtracks when a variable has no legal values left to assign
* Repeatedly chooses an unassigned variable:
    * Tries all values in the domain of the variable in turn -> trying to find a solution
    * If an inconsistency is found -> returns failure
        * Causes previous call to try **another value**

## Pseudocode
* Select-Unassigned-Variable() and Order-Domain-Values() functions can be varied to implement **general purpose heuristics**
* Inference() function can optionally be used to impose, arc-,path or k-consistency
```
function Backtracking-Search(csp) returns a solution or failure
    return Backtrack({}, csp)

function Backtrack(assignment, csp) returns a solution or failure
    if assignment is complete:
        return assignment
    var = Select-Unassigned-Variable(csp)
    
    for each value in Order-Domain-Values(var, assignment, csp):
        if value is consistent with assignment:
            add {var=value} to assignment
            inferences = Inference(csp, var, value)
            if inferences != failure:
                add inferences to assignment
                result = Backtrack(assignment, csp)
                if result != failure:
                    return result
        remove {var=value} and inferences from assignment
    return failure
```

### Variable and Value Ordering (Select-Unassigned-Variable())
`var = Select-Unassigned-Variable(csp)`
* Simplest = choose next unassigned variable in order
    * Inefficient
* **Minimum Remaining Values (MRV)**:
    * Choose variable with the fewest legal values
    * Chooses a variable that is most likely to cause a failure soon
        * Prunes the search tree
        * If *X* hase 0 values left, MRV chooses it and failure is detected
* **Degree Heuristic**:
    * Choose variable involved in the largest number of constraints
        * Degree = number of constraints a variable is involved in
    * Reduce **branching factor** on further choices
* **Least Constraining Value**:
    * Choose value that rules out the fewest choices for neighbouring variables in the constraint graph
    * Prefers maximum flexibility for subsequent assignments

* Variable selection should be **fail-first**
    * Minimise number of nodes in the search tree
        * Prunes large parts of tree earlier
* Value selection should **fail-last**
    * Only need one solution -> look at most likely values first
### Inference
* Simple Forward-checking:
    * Whenever a variable *X* is **assigned**, establish arcs consistency for *X*:
        * For each unassigned variable *Y*, connected to *X* by a constraint:
            * Delete from *Y*'s domain any value that is **inconsistent** with the value chosen for *X*
    * No need to do this if arc-constistency is used as a **pre-processing** step before backtracking search begins.
    * Doesnt detect *all* inconsistencies:
        * Makes current variables arc consistent
            * Doesn't look ahead and make all other variables arc consistent
        * Use **MAC** algorithm to overcome this
* Maintaining Arc Consistency (MAC):
    * After variable *X<sub>i</sub>* is assigned a value:
        * **Inference()** procedure calls AC-3: 
            * But with **only the arcs *(X<sub>i</sub>,X<sub>j</sub>)* for all *X<sub>j</sub>* that are unassigned variables that are neighbour of X<sub>i</sub>**
            * Instead of queue of all arcs in the CSP 
        * If any variable has its domain reduced to empty set, AC-3 fails and search can backtrack immediately
    * **Recursively Propagates constraints** when changes are made to the domains of variables

### Intelligent Backtracking
* Simple backtracking = backtrack in chronological order
    * Backtrack to previous point of non-failure
* **Intelligent Backtracking** = backtrack to a variable that is more likely to fix the cause of the failure
    * Variable that was responsible for making an assignment in the failed state impossible
* **Conflict sets** = set of assignments for each variable that are in conflict with a value for the variable
    * Then backtrack to the most recent assignment in the conflict set
    * **Conflict-directed backtracking**

    * Standard conflict set -> **terminal failure** when domain is empty
    * Variable fails, backjump to most recent assignment in its conflict set, new variable then absorbs the conflict set:
        * *X<sub>j</sub>* = current variable
        * *conf(X<sub>j</sub>)* = *X<sub>j</sub>*'s conflict set
        * If every possible value for *X<sub>j</sub>* fails, backjump to the most recent variable *X<sub>i</sub>* in *conf(X<sub>j</sub>)* and set:
            * *conf(X<sub>i</sub) = conf(X<sub>i</sub>)&cup;conf(X<sub>j</sub>) - {X<sub>i</sub>}*