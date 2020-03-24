from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.storage = DoublyLinkedList()
        self.reference = {}

    def __str__(self):
        li = []
        current_node = self.storage.head
        while current_node != None:
            li.append(current_node.value)
            current_node = current_node.next
        return str(li)
        

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key not in self.reference:
            return None
        # TODO: move reference to front
        # self.storage.move_to_front(self.reference[key])
        return self.reference[key]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # CASE: key is not already stored and list is not at limit
        if key not in self.reference and self.size < self.limit:
            self.reference.update({key: value})
            self.storage.add_to_head((key, value))
            self.size += 1

        # CASE: key is not already stored and list IS at limit
        if key not in self.reference and self.size == self.limit:
            # remove data from list and dict
            removed = self.storage.remove_from_tail()
            self.reference.pop(removed[0])

            # add data to list and dict
            self.reference.update({key: value})
            self.storage.add_to_head((key, value))
        
        # CASE: key is already stored
        if key in self.reference:
            self.reference.update({key: value})
            # TODO: update node and move to head. or delete node and create new head
            # TEMP: do it iteratively


# c = LRUCache(limit=2)
# c.set(1, "the number one is here")
# print(c)
# print(c.reference)
# c.set(2, "exists two")
# print(c)
# print(c.reference)
# c.set(3, "no, three!")
# print(c)
# print(c.reference)
# c.set(4, "fooooouuuur")
# print(c)
# print(c.reference)
