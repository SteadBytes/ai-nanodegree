# What is a Problem
## Formal Definition
* Initial State -> S<sub>0</sub>
* Actions(s) -> {a<sub>1</sub>, a<sub>2</sub>,...}
    * State as input
    * Returns set of possible actions taht can be taken from the state
* Result(s,a) -> s'
    * State and action as input
    * Applies action to state and returns new state
* GoalTest(s) -> True|False
    * State as input
    * Returns whether the goal state has been reached
* Path Cost(s<sub>i</sub>,s<sub>i+1</sub>,s<sub>i+2</sub>) -> cost value(n)
    * Sequence of state-action transtitions (path) as input
    * Returns cost of the path
    * Sum of step costs
* Step Cost(s, a, s') -> n
    * state, action, resulting state
    * returns cost of taking that action

## Mapping Definition to Problem Domain
* State Space = set of all states
    * Navigate state space by applying actions

    ![](../images/2017-11-01-12-04-55.png)

* In each state, the space is partitioned into three components:
    * Frontier = Furthest nodes/states that have been explored

        ![](../images/2017-11-01-12-02-49.png)

    * Explored State = Nodes that have been searched
        
        ![](../images/2017-11-01-12-03-29.png)

    * Unexplored State = Nodes yet to be searched

        ![](../images/2017-11-01-12-04-20.png)

