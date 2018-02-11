# Recursive Sequences
* Seed = Original value(s) of a recursive sequence which must be defined
* Order = number of prior elements future values are dependent on
* Odd numbers:
    * S<sub>1</sub> = 1 -> Seed
    * S<sub>n</sub> = 2 + S<sub>n-1</sub>
    * Order = 1
* Fibonacci Sequence:
    * S<sub>1</sub> = 1, S<sub>2</sub> = 1 -> Seed values
    * S<sub>n</sub> = S<sub>n-2</sub> + S<sub>n-1</sub>
    * Order = 2

* Unfolded view (Odd numbers):
    * ![](../../images/2018-02-11-07-44-51.png)
* Folded view (Odd numbers):
    * s<sub>1</sub> = 1
    * f(s) = 2 + s
    * s<sub>t</sub> = f(s<sub>t-1</sub>) t = 2,3,4...
* Folded view (fibonacci):
    * s<sub>1</sub> = 1, s<sub>2</sub> = 1
    * f(s<sub>t-2</sub>,s<sub>t-1</sub>) = s<sub>n-2</sub> + s<sub>n-1</sub>
    * s<sub>t</sub> = f(s<sub>t-2</sub>,s<sub>t-1</sub>) t= 3,4,5...

## Driving Recursive Sequences
* **Driver Sequence** = Receive input values as data 
* **Hidden Sequence** = Generate values recursively using driver sequence

![](../../images/2018-02-11-07-58-07.png)