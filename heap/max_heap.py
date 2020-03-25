# left child = 2i + 1
# right child = 2i + 2
# parent = (i-1) // 2 

class Heap:
    def __init__(self):
        self.storage = []

    def __str__(self):
        return str(self.storage)

    def insert(self, value):
        # add at the end, then bubble up
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        # replace the root value with the last element
        self.storage[0] = self.storage[-1]

        # cut off the tail to avoid duplication
        self.storage = self.storage[:-1]

        # move it down into true position
        self._sift_down(0)

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        # child changes place with small parent after small parent
        # root can't bubble up
        if index == 0:
            return
        p_loc = (index - 1) // 2
        if self.storage[p_loc] < self.storage[index]:
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
            left = float('-inf')
        try:
            right = self.storage[right_loc]
        except IndexError:
            right = float('-inf')
        
        # if parent is already greater than or equal to both children, stop
        if right <= self.storage[index] >= left:
            return

        # if left is larger, swap with left and bubble on
        if left > right:
            self.storage[index], self.storage[left_loc] = self.storage[left_loc], self.storage[index]
            self._sift_down(left_loc)
        
        # otherwise right must be the largest of the three
        else:
            self.storage[index], self.storage[right_loc] = self.storage[right_loc], self.storage[index]
            self._sift_down(right_loc)

h = Heap()
print(h)
h.insert(5)
print(h)
h.insert(4)
print(h)
h.insert(3)
print(h)
h.insert(10)
print(h)