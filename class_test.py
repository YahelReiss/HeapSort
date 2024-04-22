import unittest
from heapSort import HeapSort
from Person import Person


class MyTestCase(unittest.TestCase):
    def test_sorted(self):
        p1 = Person("Yahel")
        p2 = Person("Yoav")
        p3 = Person("Tal")
        p4 = Person("Amit")
        p5 = Person("Gal")
        arr = [p1, p2, p3, p4, p5]
        hs = HeapSort(arr)
        res = []
        for _ in hs.h.heap:
            res.append(hs.h.remove_min())
        self.assertEqual(res, sorted(res))

    def test_reversed_sorted(self):
        p1 = Person("Yahel")
        p2 = Person("Yoav")
        p3 = Person("Tal")
        p4 = Person("Amit")
        p5 = Person("Gal")
        arr = [p5, p4, p3, p2, p1]
        hs = HeapSort(arr)
        res = []
        for _ in hs.h.heap:
            res.append(hs.h.remove_min())
        self.assertEqual(res, sorted(res))

    def test_sort_by_name(self):
        # Test case sorting Persons by name
        p1 = Person("Yahel")
        p2 = Person("Yoav")
        p3 = Person("Tal")
        p4 = Person("Amit")
        p5 = Person("Gal")
        arr = [p1, p2, p3, p4, p5]
        for p in arr:
            p.id = p.name

        hs = HeapSort(arr)
        res = []
        for _ in hs.h.heap:
            p = hs.h.remove_min()
            res.append(p)
        self.assertEqual(res, sorted(res))

    def test_negative(self):
        # Test case sorting Persons by name
        p1 = Person("Yahel")
        p2 = Person("Yoav")
        p3 = Person("Tal")
        p4 = Person("Amit")
        p5 = Person("Gal")
        arr = [p1, p2, p3, p4, p5]
        p1.id = -7
        p2.id = -14.5
        p3.id = 0
        p4.id = 24

        hs = HeapSort(arr)
        res = []
        for _ in hs.h.heap:
            p = hs.h.remove_min()
            res.append(p)
        self.assertEqual(res, sorted(res))


if __name__ == '__main__':
    unittest.main()
