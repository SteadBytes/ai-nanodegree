# Monty Hall Problem
3 doors `A, B, C`
Randomly asssigned:
* 2 doors have a goat behind
* 1 door has a car behind

Aim is for the player to choose the door with the car behind it.

Player must pick a door. Then, a door **with a goat behind** is opened. The player then has a choice whether to switch to the other remaining door or stay with their original choice.

What is the best overall strategy?
* It is **always better to switch** after the door is opened.

## Explanantion
It is given that the car *must* be behind one of the doors, so the overall probability of the car behind behind any door **must be 1**:
```
P(CarA) + P(CarB) + P(CarC) = 1
```

Since the assignment of car/goats to doors is **random**, the probability of the car being behind one door is **the same** as being behind any of the others:
```
P(CarA) = 1/3, P(CarB) = 1/3, P(CarC) = 1/3
```
* This is a **prior probability**

The door that is then opened, will **always** have a goat behind and therefore cannot have a car behind. If this is door B for example:
* `OpenB` is an **observation**
```
P(CarB | OpenB) = 0
```
* Posterior Probability
* Probability after incorporating an observation

Since the door opened will **never** have a car behind it, we are interested in the **posterior** probability that the car is behind the remaining door given the observation that the goat is behind the opened door. If `A` chosen initially and `B` was revealed to have a goat:
* **Bayes Rule** = likelihood * prior / marginal probability
* Given door A is chosen first:
```
P(CarC | OpenB) = ?
    = (P(OpenB | CarC) * P(Car)) / P(OpenB)

    P(OpenB | CarC) = 1

    P(CarC) = 1/3

    P(OpenB) = P(CarA) * P(OpenB|CarA)
        + P(CarB) * P(OpenB | CarB) # wont be revealed as car behind B in this case
        + P(CarC) * P(OpenB | CarC) # Must open B -> Car behind C, player Chose A
    = (1/3 * 1/2) * (1/3 * 0) + (1/3 * 1)
    = 1/6 + 1/3 
    = 1/2
P(CarC | OpenB) = (1 * 1/3) / 1/2
    = 2/3
```
Probability that the car is behind the **other door** to the one that was initial chosen is **2/3**.