# Simulated Annealing
General form of optimization for finding **global optima** in the presence of many **local optima** in a search space.

Simlar to [Hill-Climbing](./hill-climbing.md) **but** aims to **avoid getting 'stuck' at local optima**.

* Chooses a **random 'move'**:
    * If move improves solution:
        * Move is always accepted
    * Else:
        * Algorithm makes the move anyway with **some probability**

## Pseudocode
* T = the simulated 'temperature' at time t, which reduces from a high value at the beginning to near zero eventually.
* ΔE = the change in energy going from current to next.

for t=1 to &infin; do:
    T = schedule(t)
    if T=0 then return current
    next = a randomly selected successor of current
    if &Delta;E > 0:
        current = next
    else
        current = next only with probability e<sup>&Delta;E/T</sup>

* High *T* = Large amount of randomness:
    * High probability of choosing next random move

* Low *T* = Low amount of randomness:
    * Low probabillity of choosing next random move
    * For *T = 0.01*:
        * Probability = e<sup>&Delta;E/T</sup> = e<sup>-1/0.01</sup> = e<sup>-100</sup>
    * *Effectively* normal hill-climbing
* Won't get 'stuck' at a plateau:
    * *&Delta;E = 0*
    * Therefore *e<sup>&Delta;E/T</sup>* = 1
        * Choose new random move

* Guaranteed to find **global optima** if initial *T* is high and then decreased slowly enough.