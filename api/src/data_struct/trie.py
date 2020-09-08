import queue

ALPHABET_SIZE = 26

class TrieNode(object):
    
    def __init__(self, info):
        self.info = info
        self.is_leaf = False
        self.actual_word = list()
        self.children = dict()

class Trie(object):
    def __init__(self):
        self.root = None

    def insert_word_to_trie(self, word):
        """
        Adds a new word to the data structure for grouping words.
            Parameters:
                word (str): word that needs to be added to the data structure
        """
        if self.root is None:
            self.root = TrieNode(None)
        
        word_len = len(word)
        
        iter = self.root
        index = 0
        while word_len > index:
            start = index
            ch = word[index]
            prefix_word = ch
            # Check if the character is an alphabet
            while self._is_alphabet(ch):
                index = index + 1
                if word_len <= index:
                    break
                ch = word[index]
            # Get the word slice separated by a delimiter     
            tag = word[start:index]
            if iter.children.get(tag) is None:
                # This sliced tag doesn't exist on the trie yet so add it.
                node = TrieNode(tag)
                iter.children[tag] = node
            else:
                # This sliced tag already exists on the Trie.
                # If it was a leaf node before then it might not be a leaf node now.
                iter.children[tag].is_leaf = False
                iter.actual_word = []
            
            #Move to the next delimiter separated word tag
            iter = iter.children[tag]
            index = index + 1
        
        # Mark last node as leaf.
        iter.is_leaf = True
        # Append the actual word to the leaf
        # Could be a list for example same sliced words with different delimiters like abc_cde_fgh and abc-cde-fgh
        iter.actual_word.append(word)


    @staticmethod
    def _traverse(node):
        """
        Returns a list of actual words saved at each leaf node in recursive way.
        """
        all_words = []
        if node.is_leaf:
            return node.actual_word
        for key, value in node.children.items():
            curr_word = Trie._traverse(value)
            all_words = all_words + curr_word
        return all_words
        
        
    def get_grouped_items(self):
        """
        Returns a dict of items with keys as the grouping name and values as all the keywords that have this as prefix.
        """
        word_map = dict()
        it = self.root
        
        # Get all immediate children of root.
        for prefix, node in self.root.children.items():
            prefix_key = ''
            it = node
            # Continue with each child of root node till it has one child for finding common prefixes.
            # Once a node has more than one child it means, two words which share prefixes.
            while it is not None and len(it.children) == 1:
                key = next(iter(it.children))
                prefix_key = prefix_key + it.info + ' '
                it = it.children[key]
            prefix_key = prefix_key + it.info
            # Already grabbed the common prefix. Now find out all strings which share this prefix.
            word_map[prefix_key] = Trie._traverse(it)
        return word_map


    def _is_alphabet(self, ch):
        ch_pos = ord(ch) - ord('a')
        return ch_pos >= 0 and ch_pos < ALPHABET_SIZE

def main():
    trie.insert_word_to_trie('abc_def')
    trie.insert_word_to_trie('abc_def_ghi')
    trie.insert_word_to_trie('abc_def_jkl')
    trie.insert_word_to_trie('abc-def-jkl')
    trie.insert_word_to_trie('xyz_mnop')
    trie.insert_word_to_trie('xyz_rst')
    trie.insert_word_to_trie('wd_none')

    trie.get_grouped_items()


if __name__ == "__main__":
    main()
        
            