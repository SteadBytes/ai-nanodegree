# Hidden Markov Models
Markov model for which the state is only partially observable
* Only observation sequence **O** is known
* Don't know which state matches which physical event
    * Underlying state sequence is hidden
* Each state yields certain outputs
* Observe output over time and produce a sequence of states based on how likely they are to produce the outputs

## Parameters
* **X<sub>t</sub>** = discrete random variable with **N** possible values
* Transition matrix = A= {a<sub>ij</sub>}=P(X<sub>t</sub>|X<sub>t-1</sub>=i)
* Initial state distribution = &pi;<sub>i</sub>=P(X<sub>1</sub>=i)
* Observation variables O<sub>t</sub> take one of *K* possible values
* Probability of observation at time *t* for state *j* = b<sub>j</sub>(o<sub>t</sub>)=P(O<sub>t</sub>=o<sub>t</sub>|X<sub>t</sub>=j)
* All values of O<sub>t</sub> and X<sub>t</sub> give matrix B={b<sub>j</sub>()v<sub>k</sub>}
    * *N*x*K* matrix
* Observation sequence = **O** = (O<sub>1</sub>=o<sub>1</sub>,O<sub>2</sub>=o<sub>2</sub>,...O<sub>T</sub>=o<sub>T</sub>)
* HMM = &theta;(A,B,&pi;)

## HMM Representation
Markov Generation Model:

![](../images/2017-12-02-12-12-55.png)

Left to right representation:

![](../images/2017-11-29-11-57-03.png)
* Each X<sub>i</sub> = frame of data (state)
* Each E<sub>i</sub> = output at time frame 

## Output Probability Distributions
Output Distributions = {b<sub>j</sub>(**o**<sub>t</sub>)}
* Continuous density distributions
    * For observation sequences with discrete symbols they are discrete distributions

Often represented by **Gaussian Mixture Densities**
* ![](../images/2017-12-02-14-23-18.png)
* &gamma;<sub>s</sub> = stream weight
    * Can be used to give a particular stream more emphasis

## HMM Problems
1. Evaluation: Given an observation sequence and a model, efficiently compute the probability of the obesrvation sequence, given the model:
    * Observation sequence O=O<sub>1</sub>,..., O<sub>T</sub>
    * Model = &lambda;(A,B,&pi;)
    * P(O|&lambda;)
2. Given an observation sequence and model, choose a corresponding **state sequence** which is optimal in a meaningful sense
    * Explains the observations
3. **Adjust model parameters** to maximise P(O|&lambda;)

## Viterbi Algorithm
Find the single best state sequence for the given observation sequence

Computes maximum likelihood state sequence:
* &phi;<sub>j</sub>(t) = maximum likelihood of observations **o**<sub>1</sub> to **o**<sub>t</sub> and being in state *j* at time *t*
* Recursive:
    * &phi;<sub>j</sub>(t)=max<sub>i</sub>{&phi;<sub>i</sub>(t-1)a<sub>ij</sub>}b<sub>j</sub>(**o**<sub>t</sub>)
    * Where:
        * &phi;<sub>1</sub>(1) = 1
        * &phi;<sub>j</sub>(1)=a<sub>1j</sub>b<sub>j</sub>(**o**<sub>1</sub>)
    * Max likelihood P(O|M) = &phi;<sub>N</sub>(T)=max<sub>i</sub>{&phi;<sub>i</sub>(T)a<sub>iN</sub>}
    * For i < j < N and model M
* Use **log likelihoods** to avoid **underflow**:
    * &phi;<sub>j</sub>(t)=max<sub>i</sub>{&phi;<sub>i</sub>(t-1)log(a<sub>ij</sub>)}+log(b<sub>j</sub>(**o**<sub>t</sub>))

Finding the best path through a matrix where:
* Vertical dimension = states of the HMM
* Horizontal dimension = frames of time

Example for isolated word recognition:

![](../images/2017-12-04-07-48-50.png)
* Dots = log probability of observing a frame at that time
* Arcs = log transition probabilities
* Log probability of any path is the sum of the log transition probabilities and the log output probabilites along the path.
* Paths grown left->right, column by column
* At each time *t*, each **partial path** &psi;<sub>i</sub>(t-1) is known for all states **

### Example
Recognising a 'We' gesture in sign language

![](../images/2017-12-04-08-02-10.png)


## Baum-Welch Re-Estimation
Increase accuracy (maximum likelihood) of the parameters in the model, given a set of observed features.
* Local maximum for &theta;<sup>*</sup>=argmax<sub>&theta;</sub>P(Y|&theta;)
* HMM parameters &theta; that maximise the probability of the observation

Uses **Expectation Maximization**

### Algorithm
Set &theta;=(A,B,&pi;) with random initial conditions or good estimates using prior information if possible

#### Forward Procedure
&alpha;<sub>i</sub>(t)=P(O<sub>1</sub>=o<sub>1</sub>,...,O<sub>T</sub>=o<sub>t</sub>,X<sub>t</sub>=i|&theta;)
* Probability of seeing o<sub>1</sub>,...o<sub>t</sub> observation sequence and bing in state *i* at time *t*

Found recursively:
1. &alpha;<sub>i</sub>(1)=&pi;<sub>i</sub>b<sub>i</sub>(o<sub>1</sub>)
2. &alpha;<sub>i</sub>(t+1)=b<sub>i</sub>(y<sub>t</sub>+1)&sum;<sub>j=1</sub><sup>N</sup>&alpha;<sub>j</sub>(t)a<sub>ji</sub>

#### Backward Procedure
&beta;<sub>i</sub>(t)=P(O<sub>t+1</sub>=o<sub>t+1</sub>,...,O<sub>T</sub>=o<sub>t</sub>|X<sub>t</sub>=i,&theta;)
* Probability of the ending partial sequence o<sub>t+1</sub>,...,o<sub>T</sub> given starting state *i* at time *t*

Found recursively:
1. &beta;<sub>i</sub>(T)=1
2. &beta;<sub>i</sub>(T)=&sum;<sub>j=1</sub><sup>N</sup>&beta;<sub>j</sub>(t+1)a<sub>ij</sub>b<sub>j</sub>(o<sub>t+1</sub>)

#### Update
&gamma;<sub>i</sub>(t)=P(X<sub>t</sub>=i|O,&theta;)=P(X<sub>t</sub>=i,O|&theta;)/P(O|&theta;)=&alpha;<sub>i</sub>(t)&beta;<sub>i</sub>(t)/&sum;<sub>j=1</sub><sup>N</sup>&alpha;<sub>j</sub>j(t)&beta;<sub>j</sub>j(t)
* Probability of being in state *i* at time *t* given observed sequence *O* and parameters &theta;
* Bayes theorem

&epsilon;<sub>ij</sub>(t)=P(X<sub>t</sub>=i,X<sub>t+1</sub>=j|O,&theta;)=P(X<sub>t</sub>=i,X<sub>t+1</sub>=j,O|&theta;/P(O|&theta;) = &alpha;<sub>i</sub>(t)a<sub>ij</sub>&beta;<sub>j</sub>(t+1)b<sub>j</sub>(o<sub>t+1</sub>)/&sum;<sub>i=1</sub><sup>N</sup>&sum;<sub>j=1</sub><sup>N</sup>&alpha;<sub>i</sub>j(t)a<sub>ij</sub>&beta;<sub>j</sub>(t+1)b<sub>j</sub>(o<sub>t+1</sub>)
* Probability of being in state *i*  and *j* at times *t* and *t+1* respectively, given observeration sequence *O* and parameters &theta;

Denominators of &gamma;<sub>i</sub>(t) and &epsilon;<sub>ij</sub> are **the same**
* Probability of making the observation *O* given parameters &theta;

Update paramaters of HMM:
* &pi;<sup>*</sup><sub>i</sub>= &gamma;<sub>i</sub>(1)
    * Expected frequency spent in state *i* at time 1
* a<sup>*</sup><sub>ij</sub>=&sum;<sub>t=1</sub><sup>T</sup>&epsilon;<sub>ij</sub>(t)/&sum;<sub>t=1</sub><sup>T-1</sup>&gamma;<sub>i</sub>(T)
    * Expected number of transitions from state *i* to state *j* compared to the expected total number of transition away from state *i* (transitions to any state including itself)
* b<sup>*</sup><sub>i</sub>(v<sub>k</sub>)=&sum;<sub>t=1</sub><sup>T</sup>1<sub>y<sub>t</sub>=v<sub>k</sub></sub>&gamma;<sub>i</sub>(t)/&sum;<sub>t=1</sub><sup>T</sup>&gamma;<sub>i</sub>(t)
    * Where 1<sub>y<sub>t</sub>=v<sub>k</sub></sub> is an **indicator function**:
        * 1 if y<sub>t</sub>=v<sub>k</sub>
        * 0 otherwise
    * Expected number of times the ouput observations have been equal to v<sub>k</sub> while in state *i* over the expected total number of times in state *i*
* Steps repeated iteratively until desired convergence is reached

Note: **Does not guarantee a global maximum**