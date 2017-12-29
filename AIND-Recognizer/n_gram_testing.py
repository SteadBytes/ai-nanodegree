import numpy as np
import pandas as pd
from asl_data import AslDb

asl = AslDb()
asl.df['grnd-ry'] = asl.df['right-y'] - asl.df['nose-y']
asl.df['grnd-rx'] = asl.df['right-x'] - asl.df['nose-x']
asl.df['grnd-ly'] = asl.df['left-y'] - asl.df['nose-y']
asl.df['grnd-lx'] = asl.df['left-x'] - asl.df['nose-x']

features_ground = ['grnd-rx', 'grnd-ry', 'grnd-lx', 'grnd-ly']
training = asl.build_training(features_ground)

df_means = asl.df.groupby('speaker').mean()
asl.df['left-x-mean'] = asl.df['speaker'].map(df_means['left-x'])
df_std = asl.df.groupby('speaker').std()


def z_score(col):
    Xmean = asl.df['speaker'].map(df_means[col])
    Xstd = asl.df['speaker'].map(df_std[col])
    return (asl.df[col] - Xmean) / Xstd


#  x: array([-0.891,  0.742,  1.153,  1.663])
#  y: array([ 1.153,  1.663, -0.891,  0.742])
cols = ['right-x', 'right-y', 'left-x', 'left-y']
features_norm = ['norm-rx', 'norm-ry', 'norm-lx', 'norm-ly']
for f_norm, col in zip(features_norm, cols):
    asl.df[f_norm] = z_score(col)

# add features for polar coordinate values where the nose is the origin
# Name these 'polar-rr', 'polar-rtheta', 'polar-lr', and 'polar-ltheta'
# Note that 'polar-rr' and 'polar-rtheta' refer to the radius and angle


def polar_coords_r(col_x, col_y):
    return np.sqrt(np.square(asl.df[col_x]) + np.square(asl.df[col_y]))


def polar_coords_theta(col_x, col_y):
    # ASL often has hand moving to nose-height which would make the angle jump
    # from 0->2Pi very quickly - looking like a large change.
    # arctan2(x,y) used instead of arctan2(y,x) to move 0->2Pi discontinuity
    # above speakers head (ASL doesn't often use that space) to avoid this.
    return np.arctan2(asl.df[col_x], asl.df[col_y])


features_polar = ['polar-rr', 'polar-rtheta', 'polar-lr', 'polar-ltheta']
asl.df['polar-rr'] = polar_coords_r('grnd-rx', 'grnd-ry')
asl.df['polar-rtheta'] = polar_coords_theta('grnd-rx', 'grnd-ry')
asl.df['polar-lr'] = polar_coords_r('grnd-lx', 'grnd-ly')
asl.df['polar-ltheta'] = polar_coords_theta('grnd-lx', 'grnd-ly')

# add features for left, right, x, y differences by one time step, i.e. the "delta" values discussed in the lecture
# Name these 'delta-rx', 'delta-ry', 'delta-lx', and 'delta-ly'

features_delta = ['delta-rx', 'delta-ry', 'delta-lx', 'delta-ly']
for f_delta, col in zip(features_delta, cols):
    asl.df[f_delta] = asl.df[col].diff().fillna(0)


def feature_rescale(orig, min_, max_):
    return (orig - min_) / (max_ - min_)


df_max = asl.df.groupby('speaker').max()
df_min = asl.df.groupby('speaker').min()

features_max = ['polar-rr-max', 'polar-rtheta-max',
                'polar-lr-max', 'polar-ltheta-max']
features_min = ['polar-rr-min', 'polar-rtheta-min',
                'polar-lr-min', 'polar-ltheta-min']

polar_rescaled = ['polar-rr-rescaled', 'polar-rtheta-rescaled',
                  'polar-lr-rescaled', 'polar-ltheta-rescaled']
for f_index, f_val in enumerate(features_polar):
    # Map the Max and Min onto the data
    asl.df[features_max[f_index]] = asl.df['speaker'].map(
        df_max[f_val], na_action=None)
    asl.df[features_min[f_index]] = asl.df['speaker'].map(
        df_min[f_val], na_action=None)

    # Normalise by rescaling using the Feature Scaling equation
    asl.df[polar_rescaled[f_index]] = feature_rescale(asl.df[f_val],
                                                      asl.df[features_min[f_index]],
                                                      asl.df[features_max[f_index]])
features_custom = polar_rescaled[:]
import warnings
from hmmlearn.hmm import GaussianHMM

from sklearn.model_selection import KFold
from my_model_selectors import SelectorConstant, SelectorDIC, SelectorBIC, SelectorCV
from my_recognizer import recognize
from asl_utils import show_errors

all_features = {'features_ground': features_ground, 'features_norm': features_norm,
                'features_polar': features_polar, 'features_delta': features_delta,
                'features_custom': features_custom}
all_model_selectors = {'SelectorConstant': SelectorConstant, 'SelectorCV': SelectorCV,
                       'SelectorBIC': SelectorBIC, 'SelectorDIC': SelectorDIC}


import arpa
import json
import os
import itertools


def train_all_words(features, model_selector):
    # Experiment here with different feature sets defined in part 1
    training = asl.build_training(features)
    sequences = training.get_all_sequences()
    Xlengths = training.get_all_Xlengths()
    model_dict = {}
    for word in training.words:
        model = model_selector(sequences, Xlengths, word,
                               n_constant=3).select()
        model_dict[word] = model
    return model_dict


def calc_WER(guesses, test_set, verbose=False):
    """ Modified show_errors to calculate and return WER without detailed breakdown.

    :param guesses: list of test item answers, ordered
    :param test_set: SinglesData object
    :param verbose: If True, will print summary output. Default=False
    :return:
        float: WER
    """
    S = 0
    N = len(test_set.wordlist)
    num_test_words = len(test_set.wordlist)
    if len(guesses) != num_test_words:
        print("Size of guesses must equal number of test words ({})!".format(
            num_test_words))
    for word_id in range(num_test_words):
        if guesses[word_id] != test_set.wordlist[word_id]:
            S += 1
    wer = float(S) / float(N)
    if verbose:
        print("\n**** WER = {}".format(wer))
        print("Total correct: {} out of {}".format(N - S, N))
    return wer


def recognize_ngram(lm, models, test_set):
    probabilities, guesses = recognize(models, test_set, num_guesses=3)
    # train for these values?
    alpha = 1
    beta = 25

    # Takes a long time to run With 3 guesses per word, longest sentence with 8
    # words has 3^8=6561 possibilities -> Reduce somehow?
    sentence_guesses = {}
    for video_num in test_set.sentences_index:
        sentence_word_indexes = test_set.sentences_index[video_num]
        hmm_max_l_words = [guesses[i] for i in sentence_word_indexes]
        possible_sentences = itertools.product(*hmm_max_l_words)
        best_sentence = None
        best_l = float("-inf")
        for s in possible_sentences:
            try:
                hmm_sentence_l = sum([probabilities[video_num][w] for w in s])
                lm_sentence_l = lm.log_s(' '.join(s))
                total_sentence_l = alpha * hmm_sentence_l + beta * lm_sentence_l
                if total_sentence_l > best_l:
                    best_l = total_sentence_l
                    best_sentence = s
            except:
                continue
        if best_sentence is not None:
            sentence_guesses[video_num] = best_sentence

    errors = 0
    for video_num in sentence_guesses:
        correct_sentence = [test_set.wordlist[i]
                            for i in test_set.sentences_index[video_num]]
        recognised_sentence = sentence_guesses[video_num]
        for c, r in zip(correct_sentence, list(recognised_sentence)):
            if c != r:
                errors += 1
        # print('Correct {}'.format(correct_sentence))
        # print('Recognised {}'.format(recognised_sentence))
        # print()
    print(float(errors) / float(178))


if __name__ == '__main__':
    # use n-gram
    models = train_all_words(features_custom,
                             all_model_selectors['SelectorBIC'])
    test_set = asl.build_test(features_custom)
    # load 3-gram language model
    lm_models = arpa.loadf(os.path.join('data', 'n-grams', 'ukn.3.lm'))
    lm = lm_models[0]
    recognize_ngram(lm, models, test_set)
