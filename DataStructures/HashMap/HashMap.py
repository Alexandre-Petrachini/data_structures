class HashMap:
    def __init__(self) -> None:
        """Initialize the hash map with a fixed size and an empty map."""
        self.size = 20
        self.map = [None] * self.size
    
    def _get_hash(self, key: str) -> int:
        """Generate a hash for a given key.
        
        Args:
            key: The key to hash.
        
        Returns:
            An integer hash value.
        """
        return sum(ord(char) for char in str(key)) % self.size
    
    def add(self, key: str, value) -> bool:
        """Add a key-value pair to the hash map.
        
        Args:
            key: The key to add.
            value: The value associated with the key.
        
        Returns:
            True if the operation is successful.
        """
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = [key_value]
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
        return True
        
    def get(self, key: str):
        """Retrieve the value for a given key.
        
        Args:
            key: The key to retrieve the value for.
        
        Returns:
            The value associated with the key, or None if the key does not exist.
        """
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None
        
    def delete(self, key: str) -> bool:
        """Delete a key-value pair from the hash map.
        
        Args:
            key: The key to delete.
        
        Returns:
            True if the key was deleted, False otherwise.
        """
        key_hash = self._get_hash(key)

        if self.map[key_hash] is not None:
            for i, pair in enumerate(self.map[key_hash]):
                if pair[0] == key:
                    self.map[key_hash].pop(i)
                    return True
        return False

    def keys(self) -> list:
        """Retrieve all keys in the hash map.
        
        Returns:
            A list of keys.
        """
        return [pair[0] for bucket in self.map if bucket for pair in bucket]
        
    def print(self) -> None:
        """Print all key-value pairs in the hash map."""
        for bucket in self.map:
            if bucket:
                for key_value in bucket:
                    print(str(key_value))