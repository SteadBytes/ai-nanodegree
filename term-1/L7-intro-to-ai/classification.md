## Classification of AI problems
Can be done using properties of the environment and components of state that need to be captured.

## Environment States
* Fully observable
    * Entire state can be seen
    * Chess or Tic Tac Toe
* Partially observable
    * Only part of the environment state can be seen
    * Battleships
* Deterministic
    * Results of each action are certain
* Stochastic
    * Results of each action are uncertain
* Discrete
    * Finite number of states environment can be in
* Continuous
    * Infinite number of states
    * Often due to some properties needing to be stored as real numbers
* Benign
    * Agent is the only thing taking actions that **intentionally** affect its goal
    * Other **random** actions can take place
* Adversarial
    * Other agents are present **deliberately** attempting to defeat the agents goal
    * Competitive games

1. Playing Poker = partially observable, stochastic, adversarial
2. Recognizing Handwritten Text = Stochastic, continuous
    * Source of input = human hand -> can go though arbitrary and unpredictable motions to procduce images that need analyzing.
3. Driving a car on the road = Partially Observable, Stochastic, Continuous
4. Playing Chess = Adversarial