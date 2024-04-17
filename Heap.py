class Heap:
    def __init__(self):
        self.heap = []
        self.heap_length = 0

    def get_parent_index(self, i):
        return (i - 1) // 2

    def get_left_child_index(self, i):
        return 2 * i + 1

    def get_right_child_index(self, i):
        return 2 * i + 2

    def add_element(self, val):
        self.heap.append(val)
        self.heap_length += 1
        self.siftup(self.heap_length - 1)

    def siftup(self, index):
        while index > 0:
            p_index = self.get_parent_index(index)
            if self.heap[index] < self.heap[p_index]:
                self.swap(index, p_index)
                index = p_index
            else:
                break

    def swap(self, index, p_index):
        self.heap[index], self.heap[p_index] = self.heap[p_index], self.heap[index]

    def remove_min(self):
        min_val = self.heap[0]
        self.heap[0] = self.heap[self.heap_length - 1]
        self.siftdown()
        self.heap_length -= 1
        return min_val

    def siftdown(self):
        index = 0
        while 2 * index + 1 < self.heap_length:
            child_index = 2 * index + 1
            if child_index + 1 < self.heap_length:
                child_index = child_index if self.heap[child_index] < self.heap[child_index + 1] else child_index + 1
            if self.heap[index] <= self.heap[child_index]:
                break
            else:
                self.swap(index, child_index)
                index = child_index
