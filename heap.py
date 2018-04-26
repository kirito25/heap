class Heap():
    def __init__(self):
        self.l = []

    def put(self, item):
        self.l.append(item)
        self.rise(self.size() - 1)

    def pop(self):
        val = self.l[0]
        self.sink()
        return val

    def size(self):
        return len(self.l)

    def leftChildIndex(self, index):
        index = int(index)
        return 2 * index + 1

    def rightChildIndex(self, index):
        return self.leftChildIndex(index) + 1

    def parentIndex(self, index):
        if index == 0:
            return 0
        return int((index - 1) / 2)
    
    def exist(self, index):
        return index < len(self.l)

    def peek(self):
        return self.l[0]
    

class MinHeap(Heap):
    def __init__(self):
        Heap.__init__(self)

    def rise(self, index):
        parentIndex = self.parentIndex(index)
        while self.l[parentIndex] > self.l[index]:
            self.l[parentIndex], self.l[index] = self.l[index], self.l[parentIndex]
            index = parentIndex
            parentIndex = self.parentIndex(index)

    def sink(self):
        self.l[0] = self.l[-1]
        self.l = self.l[:-1]
        index = 0
        while index < len(self.l):
            # child index that is less than, assume left for now
            minIndex = self.leftChildIndex(index)
            # check that the index exist, if not we are done
            if not self.exist(minIndex):
                break
            # try the right child
            try:
                if self.l[self.rightChildIndex(index)] < self.l[minIndex]:
                    minIndex = self.rightChildIndex(index)
            except IndexError:
                pass
            if self.l[minIndex] < self.l[index]:
                self.l[index], self.l[minIndex] = self.l[minIndex], self.l[index]
                index = minIndex
            else:
                # done sinking
                break

class MaxHeap(Heap):
    def __init__(self):
        Heap.__init__(self)

    def rise(self, index):
        parentIndex = self.parentIndex(index)
        while self.l[parentIndex] < self.l[index]:
            self.l[parentIndex], self.l[index] = self.l[index], self.l[parentIndex]
            index = parentIndex
            parentIndex = self.parentIndex(index)

    def sink(self):
        self.l[0] = self.l[-1]
        self.l = self.l[:-1]
        index = 0
        while index < len(self.l):
            # child index that is less than, assume left for now
            minIndex = self.leftChildIndex(index)
            # check that the index exist, if not we are done
            if not self.exist(minIndex):
                break
            # try the right child
            try:
                if self.l[self.rightChildIndex(index)] > self.l[minIndex]:
                    minIndex = self.rightChildIndex(index)
            except IndexError:
                pass
            if self.l[minIndex] > self.l[index]:
                self.l[index], self.l[minIndex] = self.l[minIndex], self.l[index]
                index = minIndex
            else:
                # done sinking
                break

class MedianHeap():
    def __init__(self):
        self.highers = MaxHeap()
        self.lowers = MinHeap()

    def put(self, item):
        if self.lowers.size() == 0:
            self.lowers.put(item)
            return
        elif item < self.lowers.peek():
            self.lowers.put(item)
        elif self.highers.size() == 0:
            self.highers.put(item)
            return
        else:
            self.highers.put(item)
        self.rebalance()

    def peek(self):
        if self.lowers.size() == self.highers.size():
            return ( self.lowers.peek() + self.highers.peek() ) / 2.0
        elif self.lowers.size() > self.highers.size():
            return self.lowers.peek() / 1.0
        else:
            return self.highers.peek() / 1.0

    def pop(self):
        if self.lowers.size() == self.highers.size():
            return ( self.lowers.pop() + self.highers.pop() ) / 2.0
        elif self.lowers.size() > self.highers.size():
            return self.lowers.pop() / 1.0
        else:
            return self.highers.pop() / 1.0
        self.rebalance()

    def rebalance(self):
        while self.lowers.size() - 1 < self.highers.size():
            self.lowers.put(self.highers.pop())
        while self.lowers.size() > self.highers.size():
            self.highers.put(self.lowers.pop())


import sys
n = int(sys.stdin.readline().strip())
h = MedianHeap()
for a_i in xrange(n):
    a_t = int(sys.stdin.readline().strip())
    h.put(a_t)
    print h.peek()
