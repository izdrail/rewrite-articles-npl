
__author__ = 'LzoMedia'
__git__ = 'https://github.com/LzoMedia/rewrite-articles-npl'

from spacy.tokenizer import Tokenizer
from spacy.lang.en.examples import sentences
from best_syn import *
import sys
if sys.version_info[0] >= 3:
    unicode = str


if sys.version_info[0] == 3:
    from urllib.request import urlopen
else:
    # Not Python 3 - today, it is most likely to be Python 2
    # But note that this might need an update when Python 4
    # might be around one day
    from urllib import urlopen

class TextRewrite:


    def __init__(self, sentence):
        self.sentence = sentence

    def work(self):
        """
        @var rewrite_types: Type of words that can rewrited 
        """
        rewrite_types = [u'NN', u'NNS', u'JJ', u'JJS']
        pos_tokenizer = nlp(unicode(self.sentence))
        words = []
        for token in pos_tokenizer:
            #print(token.pos_, token.text, token.tag_)
            if token.tag_ in rewrite_types:
                words.append(token.text)
        rewrited_sentence = self.sentence
        for word in words:
            word_syn = BestSyn(word).pull()[1]
            rewrited_sentence = rewrited_sentence.replace(word, word_syn)
        return rewrited_sentence

    def __del__(self):
        self.sentence = False

