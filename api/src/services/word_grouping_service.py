import os
import json
from data_struct.trie import Trie

class WordGroupingService(object):

    def __init__(self):
        self.trie = Trie()
        pass

    def init_words(self):
        words_file = os.environ['WORDS_FILE']
        init_words = open(words_file, 'r')
        for word in init_words:
            self.trie.insert_word_to_trie(word)
        return json.dumps(self.trie.get_grouped_items())

    def add_word(self, word):
        self.trie.insert_word_to_trie(word)
        return json.dumps(self.trie.get_grouped_items())