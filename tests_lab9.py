import unittest
from lab9 import max_wire_length

class TestMaxWireLength(unittest.TestCase):
    def test_cases(self):
        cases = [
            (2, [3, 3, 3], 5.65),
            (100, [1, 1, 1, 1], 300.00),
            (4, [100, 2, 100, 2, 100], 396.32),
        ]
        
        for i, (w, h, expected) in enumerate(cases, start=1):
            with self.subTest(f"Test case {i}: w={w}, h={h}"):
                got = max_wire_length(w, h)
                r = int(got * 100 + 0.5) / 100.0
                self.assertAlmostEqual(r, expected, delta=0.01)


unittest.main()