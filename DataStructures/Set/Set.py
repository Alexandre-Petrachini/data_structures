from typing import Any, Iterable, Dict


class Set:
    """
    A simple implementation of a set data structure in Python 3.

    This class uses a dictionary to store elements, where each key is an element
    of the set, and the value is always True (to denote presence).
    """

    def __init__(self, values: Iterable[Any] = None) -> None:
        """
        Initializes a new Set object. If an iterable of values is provided,
        those values are added to the set.

        Args:
            values (Iterable[Any], optional): An iterable of values to initialize the set with.
        """
        self.dict: Dict[Any, bool] = {}  # Each instance of Set has its own dict property

        if values is not None:
            for value in values:
                self.add(value)

    def __repr__(self) -> str:
        """
        Returns the string representation of the Set object.

        Returns:
            str: A string representation of the set.
        """
        return f"Set: {list(self.dict.keys())}"

    def add(self, value: Any) -> None:
        """
        Adds a value to the set.

        Args:
            value (Any): The value to be added to the set.
        """
        self.dict[value] = True

    def contains(self, value: Any) -> bool:
        """
        Checks if a value is in the set.

        Args:
            value (Any): The value to check for presence in the set.

        Returns:
            bool: True if the value is in the set, False otherwise.
        """
        return value in self.dict

    def remove(self, value: Any) -> None:
        """
        Removes a value from the set.

        Args:
            value (Any): The value to be removed from the set.

        Raises:
            KeyError: If the value is not found in the set.
        """
        del self.dict[value]