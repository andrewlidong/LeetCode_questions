from random import choice


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dictionary = {}
        self.list = []

    # add value -> its index into dictionary, average O(1) time
    # append value to array list, average O(1) time as well
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dictionary:
            return False
        self.dictionary[val] = len(self.list)
        self.list.append(val)
        return True

    # delete an index of elements to delete from the hashmap
    # move the last element to the place of the element to delete, O(1) time
    # pop the last element out, O(1) time

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dictionary:
            # move the last element to the place idx of the element to delete
            last_element, idx = self.list[-1], self.dictionary[val]
            self.list[idx], self.dictionary[last_element] = last_element, idx
            # delete the last element
            self.list.pop()
            del self.dictionary[val]
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.list)

# Time: GetRandom is always O(1).  Insert and Delete both have O(1) time complexity and O(N) in the worst case exceeds the capacity of currently allocated array/hashmap and invokes space reallocation.
# Space: O(N) to store N elements.


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# initialize (likely with a dictionary)

# insert (takes an integer value) -> true if item is present, false otherwise.  Also inserts item into the dictionary

# remove (takes an integer value) -> true if item is present, false otherwise.  Also removes an item from the set.

# getRandom (takes no input) -> returns a random integer.  Can probably just use python rand(keys(set))
