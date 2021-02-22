class LRUCache:

    # Initialize capacity
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    # return the value of the key queried in O(1) and -1 if we don't find it
    # move the key to the end to show that it was recently used
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    # add/update the key by conventional methods
    # also move the key to the end to show it was recently used
    # check whether the length of our ordereddict has exceeded our capacity
    # if so, remove the first key (least recently used)
    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

# Time Complexity: O(1) on get, put

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# Initialize a data structure with a size constraint of capacity, or at least an initial size of capacity.  Could be an array or a dictionary.
# On get, get the value corresponding to whatever key is being used.  Then move it to the front or the back (depending on how we set up our data structure), or at least flag it in such a way that proves that it's been used.  If the key isn't there simply return -1, not found.
# On put, check whether the data structure is at its capacity or not.  Depending on how we initialize our data structure, it might start that way.  Also, if the key exists already, we just update the value of the key.  Pop off, or evict the least recently used tuple, and then insert the new tuple.  Insertion counts as a use.  Getting counts as a use.


# Which data structure makes sense?
# An array makes sense but it blows up our time complexity to N on every get and probably put since we need to reshuffle the entire array.


# An OrderedDict helps us keep order of insertion of keys and we can change that order if required.  This makes it so that all operations have O(1) time compexity.
# Maintain our OrderedDict to show how recently they were used.  If any update or query is made to a key, move it to the end (to signify it's been most recently used).  If anything is added, add it to the end (most recently used/added)
# For get(key), return the value of the key given in O(1) and return -1 if we don't find the key in the ordereddict/cache.  Also move the key to the end to show it was recently used.
# For put(key, value), first add/update the key with conventional methods.  Also move the key to the end to show that it was recently used.  Here, also check whether the length of our ordered dictionary has exceeded our capacity, if so remove the first key (least recently used)
