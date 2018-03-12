# Voice User Interfaces (VUI)

Interacting with a computer via human voice/speech.

Popular area of development:

* Speech is natural for humans to convey what they want
* Fast
* Easier than typing (i.e. whilst driving)

## VUI Pipeline

### Voice to Text

* Speech recognition
* Sound waves converted into an audio signal via a microphone
* Signal is sampled and converted to vectors of component frequencies -> features of sound in a dataset
  * **Feature Extraction**
* Decode/recognize vectors as a word/sentence:
* Need models that work well with time series data
  * HMM
  * RNN
  * Acoustic Model
    * 'Best Guess' as to what the words are based on signal data
  * Language model
    * 'Experience model' -> extract and recognize probabilities of sequences
  * Accent model
    * Deal with different intonations/accents in the input

### Text to Text

* Reasoning/logic part of the VUI
* Understand/process request
* Formulate response
* Fully understanding text is very difficult - field of NLP
* Take a 'shortcut':
  * Map the most **probable** request phrases
  * i.e. a weather application may only recognise 'weather in [place]'
  * Doesn't work if request hasnt been pre-mapped
  * Works well for limited-domain applications

### Text to to Speech

* Speech synthesis
* Train a model based on examples of how words are spoken
* Produce most probable pronunciation of spoken words
