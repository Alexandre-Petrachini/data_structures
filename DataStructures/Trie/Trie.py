class Trie:
    """
    A Trie implementation for efficient insertion, search, prefix search, and deletion operations on strings.
    """

    def __init__(self) -> None:
        """
        Initializes an empty Trie.
        """
        self.words = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the Trie.
        
        Args:
            word (str): The word to insert.
        """
        current = self.words
        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
        current['#'] = True

    def search(self, word: str) -> bool:
        """
        Searches for a word in the Trie.
        
        Args:
            word (str): The word to search for.
        
        Returns:
            bool: True if the word exists in the Trie, False otherwise.
        """
        current = self.words
        for char in word:
            if char not in current:
                return False
            current = current[char]
        return '#' in current

    def prefix_search(self, prefix: str) -> bool:
        """
        Searches for a prefix in the Trie.
        
        Args:
            prefix (str): The prefix to search for.
        
        Returns:
            bool: True if the prefix exists in the Trie, False otherwise.
        """
        current = self.words
        for char in prefix:
            if char not in current:
                return False
            current = current[char]
        return True

    def delete(self, word: str) -> bool:
        """
        Deletes a word from the Trie.
        
        Args:
            word (str): The word to delete.
        
        Returns:
            bool: True if the word was successfully deleted, False if the word was not found.
        """
        def delete_helper(node, word, depth):
            if node is None:
                return False
            
            # If end of the word is reached
            if depth == len(word):
                if '#' in node:
                    del node['#']  # Remove end of word marker
                    return len(node) == 0  # Return True if node has no other children
                return False
            
            char = word[depth]
            if char in node:
                should_delete_current_node = delete_helper(node[char], word, depth + 1)
                
                if should_delete_current_node:
                    del node[char]
                    return len(node) == 0
            
            return False

        return delete_helper(self.words, word, 0)