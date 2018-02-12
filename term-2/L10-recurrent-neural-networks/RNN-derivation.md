# RNN Fundamental Derivations
Using FNN's with recursivity - [injecting-recursivity.md](./injecting-recursivity.md) lead to a **loss of dependence** between recursive levels.

-> Need to enforce greater dependency between levels.

## Derivation
* Recursive sequence:
    * s<sub>1</sub> = &alpha;
    * s<sub>2</sub> = g(s<sub>1</sub>)
    * s<sub>3</sub> = g(s<sub>2</sub>)
    * s<sub>4</sub> = g(s<sub>3</sub>)
    * ...
* Equalities are **desired** not absolute or guaranteed -> **approximately** hold the equalities as well as possible
    * s<sub>1</sub> = &alpha;
    * s<sub>2</sub> &asymp;	g(s<sub>1</sub>)
    * s<sub>3</sub> &asymp;	 g(s<sub>2</sub>)
    * s<sub>4</sub> &asymp;	 g(s<sub>3</sub>)
* Introduce auxillary variable to better display the sequence given by the right hand sides of the equations:
    * s<sub>1</sub> = h<sub>1</sub> = &alpha; 
    * s<sub>2</sub> &asymp;	h<sub>2</sub> = g(s<sub>1</sub>)
    * s<sub>3</sub> &asymp;	h<sub>3</sub> = g(s<sub>2</sub>)
    * s<sub>4</sub> &asymp;	h<sub>4</sub> = g(s<sub>3</sub>)
* Remove LHS for clarity:
    * h<sub>1</sub> = &alpha; 
    * h<sub>2</sub> = g(s<sub>1</sub>)
    * h<sub>3</sub> = g(s<sub>2</sub>)
    * h<sub>4</sub> = g(s<sub>3</sub>)
* Enforce consecutive level dependedency -> ensure each level is **functionally dependent** on the preceding level
    * Need to use a parameterized function of two inputs
        * Often a linear combination of the inputs, passed through an activation function such as tanh
            * i.e f(h<sub>t</sub>, s<sub>t</sub>) = tanh(w<sub>0</sub>+w<sub>1</sub>h<sub>t</sub>+w<sub>2</sub>s<sub>t</sub>)
    * h<sub>1</sub> = &alpha; 
    * h<sub>2</sub> = f(h<sub>1</sub>, s<sub>1</sub>)
    * h<sub>3</sub> = f(h<sub>2</sub>, s<sub>2</sub>)
    * h<sub>4</sub> = f(h<sub>3</sub>, s<sub>3</sub>)
    * ...
    * h<sub>t</sub> = f(h<sub>t-1</sub>, s<sub>t-1</sub>)
* Auxillary variables h<sub>1</sub>, hsub>2</sub>.. are **hidden states**
    * Whilst recursing on h, s is observed and s *drives* h

## Least Squares Loss
* Removing hidden state variables (h) 
    * s<sub>2</sub> &asymp; f(h<sub>1</sub>, s<sub>1</sub>)
    * s<sub>3</sub> &asymp; f(h<sub>2</sub>, s<sub>2</sub>)
    * s<sub>4</sub> &asymp; f(h<sub>3</sub>, s<sub>3</sub>)
    * ...
    * s<sub>t</sub> &asymp; f(h<sub>t-1</sub>, s<sub>t-1</sub>)
* Square errors:
    * (s<sub>2</sub> - f(h<sub>1</sub>, s<sub>1</sub>))<sup>2</sup>
    * (s<sub>3</sub> - f(h<sub>2</sub>, s<sub>2</sub>))<sup>2</sup>
    * (s<sub>4</sub> - f(h<sub>3</sub>, s<sub>3</sub>))<sup>2</sup>
    * ...
    * (s<sub>t</sub>  f(h<sub>t-1</sub>, s<sub>t-1</sub>))<sup>2</sup>
* Minimize sum:
    * &sum;<sup>P</sup><sub>t=2</sub>(s<sub>t</sub>f(h<sub>t-1</sub>, s<sub>t-1</sub>))<sup>2</sup>

* Recursion broken into levels, but are **explicitly dependent** (unlike FNN)
* When using architectures with bounded output use linear combination in the loss -> ensure values > 1 can be reached
    * i.e if f(h, s) = tanh(w<sub>0</sub>+w<sub>1</sub>h<sub>t</sub>+w<sub>2</sub>s<sub>t</sub>)
    * -> &sum;<sup>P</sup><sub>t=2</sub>(s<sub>t</sub>-(b+wf(h<sub>t-1</sub>, s<sub>t-1</sub>)))<sup>2</sup>