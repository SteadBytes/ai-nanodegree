import warnings
from asl_data import SinglesData


def recognize(models: dict, test_set: SinglesData, num_guesses=1):
    """ Recognize test word sequences from word models set

   :param models: dict of trained models
       {'SOMEWORD': GaussianHMM model object, 'SOMEOTHERWORD': GaussianHMM model object, ...}
   :param test_set: SinglesData object
   :return: (list, list)  as probabilities, guesses
       both lists are ordered by the test set word_id
       probabilities is a list of dictionaries where each key a word and value is Log Liklihood
           [{SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            {SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            ]
       guesses is a list of the best guess words ordered by the test set word_id
       When num_guesses==1, 1d list: 
           ['WORDGUESS0', 'WORDGUESS1', 'WORDGUESS2',...]
       When num_guesses > 1, 2d list of num_guesses for each word:
           [['WORDGUESS0_0','WORDGUESS0_1'], ['WORDGUESS1_0','WORDGUESS0_2']]
           Used for optional part 4 where choices for each word needed
   """
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    probabilities = []
    guesses = []
    for i in range(test_set.num_items):
        X, Xlengths = test_set.get_item_Xlengths(i)
        this_probs = {}
        for word, model in models.items():
            try:
                this_probs[word] = model.score(X, Xlengths)
            except:
                pass
        probabilities.append(this_probs)
        if num_guesses == 1:
            guesses.append(max(this_probs, key=lambda k: this_probs[k]))
        else:
            guesses.append(sorted(this_probs, key=this_probs.get,
                                  reverse=True)[:num_guesses])
    return probabilities, guesses
