# Local Beam Search
* Begins with *k* random states
* All successors of *k* states are generated
    * If any state is a goal state -> terminate
    * Else, selects the *k* best successors from the complete list and repeats.

* Quickly abandons searches where little progress is being made.

Tracks *k* states between search iterations - passing useful information among parallel search threads. 

* Can become concentrated in a small region of state space
    * All *k* states converge on each other
    * Becomes inefficient:
        * More expensive version of hill-climbing
* Avoid this using **stochastic local beam search**:    
    * Chooses best *k* successors from candidate successors at **random**
        * With probability of choosing a given state and **increasing function of its value**
            * Similar to 'Natural Selection'