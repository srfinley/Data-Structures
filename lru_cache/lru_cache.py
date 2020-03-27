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

        # PERM version, O(1) time:
        self.storage.move_to_front(self.reference[key])
        self.reference[key] = self.storage.head
        return self.reference[key].value[1]

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
            self.storage.add_to_head((key, value))
            self.reference.update({key: self.storage.head})
            self.size += 1

        # CASE: key is not already stored and list IS at limit
        if key not in self.reference and self.size == self.limit:
            # remove data from list and dict
            removed = self.storage.remove_from_tail()
            self.reference.pop(removed[0])

            # add data to list and dict
            self.storage.add_to_head((key, value))
            self.reference.update({key: self.storage.head})
        
        # CASE: key is already stored
        if key in self.reference:
            # PERM:
            former = self.reference[key]
            self.storage.delete(former)

            self.storage.add_to_head((key, value))
            self.reference.update({key: self.storage.head})
