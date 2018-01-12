# Map Coloring 
Assigning a color to each region of a map in such a way that no neighboring regions have the same color

![](../images/2017-11-07-16-35-28.png)

Can only use red, green or blue in this example.

* *X = {WA, NT, Q, NSW, V, SA, T}*
* *D<sub>i</sub> = {red, green, blue}*
* *C = {SA!=WA, SA!=NT, SA!=Q, SA!=NSW, SA!=V, WA!=NT, NT!=Q, NSW!=Q, NSW!=V}*
    * Abbreviations, i.e. *SA!=WA = <(SA,WA), SA!=WA>*

Constraint Graph:

![](../images/2017-11-07-16-40-44.png)