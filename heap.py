import random

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
        print "hi"
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


