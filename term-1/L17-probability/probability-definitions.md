# Probability Definitions and Formulae
* Probability is used to express uncertainty

## Complimentary Probability
* P(A) = p &rarr; P(¬A) = 1-p
## Independence
* X &perp; Y = P(X)P(Y) = P(X,Y)
* Two random variables are independent, the **joint probability** is the **product of the marginals**
## Total Probability
* P(Y) = &sum;<sub>i</sub>P(Y|X=i)P(X=i)
## Negation of Probabilities
* P(¬X|Y) = 1-P(X|Y)
positive test = 0.207
## Conditional Probability
* P(A|B) = P(A&cap;B) / P(B)

* Alternate form: P(A&cap;B) = P(A|B)&middot;P(B)
* The measure of the probability of an event **given** that another event has occured.
* Dependent events
## Joint Probability
* P(A&cap;B) = P(A|B)&middot;P(B)
    * Uses conditional probability 
* Measure of two events happening at the same time
* Only applicable when multiple observations can occur at the same time
## Inclusion-Exclusion Principle
* Probability of a disjunction
* P(a &or; b) = P(a) + P(b) - P(a &and; b)
    * Cases where a holds and cases where b holds cover all cases where a&or;b holds but summing the two sets counts their intersection twice so need to subtract P(a&and;b)

