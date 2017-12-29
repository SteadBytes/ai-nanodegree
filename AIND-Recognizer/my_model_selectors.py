import math
import statistics
import warnings

import numpy as np
from hmmlearn.hmm import GaussianHMM
from sklearn.model_selection import KFold
from asl_utils import combine_sequences

# NOTE: Try/Except block around any hmm model initialisation/training/scoring as
#       hmmlearn may not work on all attempted models (too few samples etc)


class ModelSelector(object):
    '''
    base class for model selection (strategy design pattern)
    '''

    def __init__(self, all_word_sequences: dict, all_word_Xlengths: dict, this_word: str,
                 n_constant=3,
                 min_n_components=2, max_n_components=10,
                 random_state=14, verbose=False):
        self.words = all_word_sequences
        self.hwords = all_word_Xlengths
        self.sequences = all_word_sequences[this_word]
        self.X, self.lengths = all_word_Xlengths[this_word]
        self.this_word = this_word
        self.n_constant = n_constant
        self.min_n_components = min_n_components
        self.max_n_components = max_n_components
        self.random_state = random_state
        self.verbose = verbose

    def select(self):
        raise NotImplementedError

    def base_model(self, num_states):
        # with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        # warnings.filterwarnings("ignore", category=RuntimeWarning)
        try:
            hmm_model = GaussianHMM(n_components=num_states, covariance_type="diag", n_iter=1000,
                                    random_state=self.random_state, verbose=False).fit(self.X, self.lengths)
            if self.verbose:
                print("model created for {} with {} states".format(
                    self.this_word, num_states))
            return hmm_model
        except:
            if self.verbose:
                print("failure on {} with {} states".format(
                    self.this_word, num_states))
            return None


class SelectorConstant(ModelSelector):
    """ select the model with value self.n_constant

    """

    def select(self):
        """ select based on n_constant value

        :return: GaussianHMM object
        """
        best_num_components = self.n_constant
        return self.base_model(best_num_components)


class SelectorCV(ModelSelector):
    ''' select best model based on average log Likelihood of cross-validation folds

    :return: GaussianHMM object
    '''

    def select(self):
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        best_n = None
        best_avg_logL = float("-inf")
        n_splits = min(self.min_n_components, len(self.lengths))
        if n_splits < 2:
            n_splits = 2
        split_method = KFold(n_splits=n_splits)
        for n in range(self.min_n_components, self.max_n_components):
            try:
                folds = total_logL = 0
                for train_idx, test_idx in split_method.split(self.sequences):
                    folds += 1
                    train_X, train_lengths = combine_sequences(
                        train_idx, self.sequences)
                    test_X, test_lengths = combine_sequences(
                        test_idx, self.sequences)
                    try:
                        model = GaussianHMM(n, n_iter=1000, random_state=self.random_state).fit(
                            train_X, train_lengths)
                        score = model.score(test_X, test_lengths)
                        total_logL += score
                    except:
                        pass
                avg_logL = total_logL / folds
                if avg_logL > best_avg_logL:
                    best_avg_logL = avg_logL
                    best_n = n
            except:
                pass
        # retrain using best n_components with FULL DATA SET, not split set
        # used above
        if best_n is not None:
            return self.base_model(best_n)
        return None


class SelectorBIC(ModelSelector):
    """ select the model with the lowest Bayesian Information Criterion(BIC) score

    http://www2.imm.dtu.dk/courses/02433/doc/ch6_slides.pdf
    Bayesian information criteria: BIC = -2 * logL + p * logN
    """

    def select(self):
        """ select the best model for self.this_word based on
        BIC score for n between self.min_n_components and self.max_n_components

        :return: GaussianHMM object
        """
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        best_model = None
        best_bic = float("+inf")
        for n in range(self.min_n_components, self.max_n_components):
            model = self.base_model(n)
            try:
                logL = model.score(self.X, self.lengths)
                # num_model_params = num_initial state occupation probs +
                # num_transition probs + num_emission probs
                # initial state occupation probs = n-1 (learned size =n,
                # add up to 1 therefore n-1)
                # transition probs = n(n-1) (n*n, add to 1 so learned size
                # = n(n-1))
                # emission probs=num means+num covars
                # num means = n* num_features, num_covars = n*num_features
                # = 2(n*num_features)
                # gives model_params = n*n-1+2(n*num_features)
                num_model_params = n**2 - 1 + 2 * n * model.n_features
                bic = -2 * logL + n * np.log(num_model_params)
                if bic < best_bic:
                    best_bic = bic
                    best_model = model
            except:
                pass
        return best_model


class SelectorDIC(ModelSelector):
    ''' select best model based on Discriminative Information Criterion

    Biem, Alain. "A model selection criterion for classification: Application to hmm topology optimization."
    Document Analysis and Recognition, 2003. Proceedings. Seventh International Conference on. IEEE, 2003.
    http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.58.6208&rep=rep1&type=pdf
    https://pdfs.semanticscholar.org/ed3d/7c4a5f607201f3848d4c02dd9ba17c791fc2.pdf
    DIC = log(P(X(i)) - 1/(M-1)SUM(log(P(X(all but i))
    '''

    def select(self):
        """ Select the best model for self.this_word based on DIC score for n
        between self.min_n_components and self.max_n_components

        :return: GaussianHMM object
        """
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        best_model = None
        best_dic = float("-inf")

        for n in range(self.min_n_components, self.max_n_components):
            try:
                model = self.base_model(n)
                logL = model.score(self.X, self.lengths)
                other_words = [f for w, f in self.hwords.items()
                               if w != self.this_word]
                other_logLs = [model.score(Y, Ylengths)
                               for (Y, Ylengths) in other_words]
                dic = logL - sum(other_logLs) / (len(other_words))
                if dic > best_dic:
                    best_dic = dic
                    best_model = model
            except:
                pass
        return best_model
