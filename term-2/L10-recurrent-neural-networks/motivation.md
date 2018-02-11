# RNN Motivation
Supervised learning with **ordered sequences**
* Financial time series
    * Input: Ordered sequence of past series values
    * Output: Ordered sequence of future series values
* Natural langauge processing
    * Input: Ordered sequence of words or characters (training corpus)
    * Output: Ordered sequence of characters
* Machine Translation
    * Input: Ordered sequence of words (language X)
    * Output: Ordered sequence of words (language Y)
* Speech recognition:
    * Input: Ordered sequence of audio signal
    * Output: Ordered sequence of words

## Vanilla Supervised Learners and Structured Input
Vanilla supervised models e.g feedforward networks.

Assume **no input structure**:
* Input features can be arranged in any order to the learner
    * Could feed in images with 'jumbled' pixels as well as correct order of pixels and the result is the same
    * Could feed text in any order
        * i.e. Input 'the dog is brown' and 'brown the is dog' will produce the same result
* 'Wastes' information from highly structured input data
    * i.e. Images/Videos contain spatially correlated features
        * CNN's exploit these spatial features
    * i.e. Text has a 'naturally' ordered structure

Want a learner that **exploits the ordered features** to improve learning