# Bayes Theorem
Describes the probability of an event, based on **prior knowledge** of conditions related to the event - observations.
[Good article](http://www.eng.utah.edu/~cs5961/Resources/bayes.pdf)

## Definition
P(A|B) = (P(B|A)&middot;P(A)) / P(B)
 
 posterior = likelihood * prior / marginal probability

Where A and B are events and P(B) != 0

* P(A) = **prior** or marginal probability  of A, doesn't take into account any onformation about B.
* P(A|B) = conditional probabiliy of A, given B. Called **posterior probaility** as it depends on an observation of B.
* P(B) = **prior** or marginal probability or B.
    * Often computed using **total probability**:
    * P(B) = &sum;<sub>a</sub>P(B|A=a)P(A=a)
## Alternative Form
P(A|B) = &eta;&middot;P'(A|B)

P(¬A|B) = &eta;&middot;P'(¬A|B)
* Where &eta; is the **normalizer** given by:
    * &eta; = (P'(A|B)+P'(¬A|B))<sup>-1</sup>
* This defers the calculation of the normalizer, using easier to calculate pseudo probabilities denoted by P'()
### Derivation
* Normal Bayes Rule gives:
    * P(A|B) = (P(B|A)&middot;P(A)) / P(B)
    *P(¬A|B) = (P(B|¬A)&middot;P(¬A)) / P(B)
* Know that P(A|B) + P(¬A|B)=1
    * Complimentary 
* The denominator (normalizer) is the same, so can be ignored to give*pseudo* probabilities from the numerators:
    * P'(A|B) = P(B|A)&middot;P(A)
    * P'(¬A|B) = P(B|¬A)&middot;P(¬A)
* Therefore:
    * P(A|B) = &eta;&middot;P'(A|B)
    * P(¬A|B) = &eta;&middot;P'(¬A|B)
    * Where &eta; is the normalizer
* Normalizer is then given by the reciprocal of the sum of the two pseudo probabilities:
    * &eta; = (P'(A|B)+P'(¬A|B))<sup>-1</sup>

