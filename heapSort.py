from Heap import Heap


class HeapSort:
    def __init__(self, arr_to_sort):
        self.arr = arr_to_sort
        self.h = Heap()
        self.build_heap()

    def build_heap(self):
        self.h.heap = self.arr
        for _ in range(len(self.arr)):
            self.h.heap_length += 1
            self.h.siftup(self.h.heap_length - 1)

    def sort(self):
        pass
