class Heap:
    def __init__(self, comparator=lambda x, y: x > y):
        self.storage = []
        self.comparator = comparator

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        if self.get_size() == 0:
            return None
        removed = self.storage[0]
        # if removing final element
        if self.get_size() == 1:
            self.storage = []
            return removed
        # replace the root value with the last element
        self.storage[0] = self.storage[-1]

        # cut off the tail to avoid duplication
        self.storage = self.storage[:-1]

        # move it down into true position
        self._sift_down(0)
        return removed

    def get_priority(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        # child changes place with parent after parent
        # root can't bubble up
        if index == 0:
            return
        # generic comparator: comp(parent, child) needs to be made True
        p_loc = (index - 1) // 2
        if not self.comparator(self.storage[p_loc], self.storage[index]):
            self.storage[p_loc], self.storage[index] = self.storage[index], self.storage[p_loc]
            self._bubble_up(p_loc)
        else:
            return

    def _sift_down(self, index):
        # small parent changes places with the larger child
        left_loc = (2 * index) + 1
        right_loc = (2 * index) + 2
        try:
            left = self.storage[left_loc]
        except IndexError:
            left = None
        try:
            right = self.storage[right_loc]
        except IndexError:
            right = None

        # if there are no children, stop
        if left == None and right == None:
            return
        
        # if there are two children
        if left != None and right != None:
            if self.comparator(left, right):
                if self.comparator(left, self.storage[index]):
                    self.storage[index], self.storage[left_loc] = self.storage[left_loc], self.storage[index]
                    self._sift_down(left_loc)
                else:
                    return
            else:
                if self.comparator(right, self.storage[index]):
                    self.storage[index], self.storage[right_loc] = self.storage[right_loc], self.storage[index]
                    self._sift_down(right_loc)
        
        # if only right exists
        if left == None and right != None:
            if self.comparator(right, self.storage[index]):
                self.storage[index], self.storage[right_loc] = self.storage[right_loc], self.storage[index]
                self._sift_down(right_loc)
        
        # if only left exists
        if left != None and right == None:
            if self.comparator(left, self.storage[index]):
                self.storage[index], self.storage[left_loc] = self.storage[left_loc], self.storage[index]
                self._sift_down(left_loc)
