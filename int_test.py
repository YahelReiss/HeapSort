import unittest
from heapSort import HeapSort


class MyTestCase(unittest.TestCase):
    def test_array(self):
        arr = [3, 71, 12, 53, 0, -4]
        hs = HeapSort(arr)
        res = []
        for _ in hs.h.heap:
            res.append(hs.h.remove_min())
        self.assertEqual(res, sorted(res))  # add assertion here

    def test_empty_array(self):
        arr = []
        hs = HeapSort(arr)
        res = []
        for _ in hs.h.heap:
            res.append(hs.h.remove_min())
        self.assertEqual(res, [])

    def test_already_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        hs = HeapSort(arr)
        res = []
        for _ in hs.h.heap:
            res.append(hs.h.remove_min())
        self.assertEqual(res, [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        arr = [5, 4, 3, 2, 1]
        hs = HeapSort(arr)
        res = []
        for _ in hs.h.heap:
            res.append(hs.h.remove_min())
        self.assertEqual(res, sorted([5, 4, 3, 2, 1]))

    def test_equal(self):
        # Test case where all elements are equal
        arr = [5, 5, 5, 5, 5]
        hs = HeapSort(arr)
        res = []
        for _ in hs.h.heap:
            res.append(hs.h.remove_min())
        self.assertEqual(res, arr)


if __name__ == '__main__':
    unittest.main()
