# Planning Graphs
* Polynomial size approximation of the full state->action->successor state tree
    * Planning problem with *l* literals and *a* actions:
        * Each *S<sub>i</sub>* has no more than *l* nodes and *l<sup>2</sup>* mutex links
        * Each *A<sub>i</sub>* has no more than *a+l* nodes, *(a+l)<sup>2</sup>* mutex links and *2(al+l)* precondition and effect links
        * Entire graph with *n* levels = ***O(n(a+l)<sup>2</sup>)*** size and time to build complexity
* Use to *estimate* number of steps required to reach goal *G* from initial state *S<sub>0</sub>*
    * Always **correct** when reports the goal is **not reachable**
    * **Never overestimates** number of steps
        * **Admissable heuristic**
* Directed graph organized into **levels**
    * Alternating State , *S<sub>i</sub>* and Action , *A<sub>i</sub>* levels
    * Every *S<sub>i</sub>* contains:
        * All the literals that could result from any possible choice of actions in *A<sub>i-1</sub>*
        * Constraints saying which pairs of literals are **not possible**
    * Every *A<sub>i</sub>* contains:
        * All the actions that are applicable in *S<sub>i</sub>*
        * Constraints saying that two actions cannot both be executed at the same level
    * Level *S<sub>0</sub>* consists of nodes representing **each fluent** that holds in *S<sub>0</sub>*
    * Level *A<sub>0</sub>* consists of nodes for each ground actions that might be applicable in *S<sub>0</sub>*
    * Continue alternating *S<sub>i</sub>*, *A<sub>i</sub>* until termination condidtion is met
* Graph **levels off** when two consecutive levels are identical

![](../images/2017-11-19-14-09-03.png)

* **Persistence Action**
    * A literal can persist of if no action negates it
    * For every literal *C*, a persistence action is added with precondition *C* and effect *C*
* **Mutual Exclusion/Mutex Links**
    * Indicate literals that cannot appear together, regardless of the choice of actions
    * Mutex relation holds between two *actions* if any of conditions hold:
        * Inconsistent effects
            * One action negates an effect of the other
        * Interference
            * One of the effects of an action is the negation of a precondition of the other
        * Competing needs
            * One of the preconditions of an action is mutually exclusive with a precondition of the other
    * Mutex relation holds between two *literals* at the same level if:
        * Inconsistent Support
            * One is the negation of the other
            * Or if each possible pair of actions that could achieve the tow literals is mutually exclusive

## Heuristic Estimation
* If any goal literal does not appear in the final level of the graph -> problem is **unsolvable**
* **Level cost** of goal literal*g<sub>i</sub>*
    * Estimate total cost of achieving any *g<sub>i</sub>* from state *s*
    * The level at which *g<sub>i</sub>* first appears in the planning graph constructed from inital state *s*
* **Serial planning graph**
    * Insists that only one action can actually occur at any given time step
        * Add mutex links between every pair of *nonpersistence* actions
    * More accurate **level cost** as the number of actions is implicitly taken into account (one per level), whereas with a normal planning graph only the number of levels is taken into account (multiple actions per level)
### Conjunctive Goals
* **Max level heuristic** 
    * Takes maximum level cost of any of the goals
    * Admissable
    * **Not necessarily accurate**
* **Level sum heuristic**
    * Sum of level costs of the goals
    * Can be inadmissable
        * Works well with problems that are largely decomposable
* **Set Level heuristic**
    * Finds the level at which all literals in the conjunctive goal appear in the planning graph **without anypair being mutex**
    * Admissable
    * More accurate than max-level
    
