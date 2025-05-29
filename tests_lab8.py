import unittest
import os
from lab8 import compute_min_fiber_length


class TestFiberNetwork(unittest.TestCase):
    def setUp(self):
        self.test_file = "test/test_wells.csv"
        os.makedirs("test", exist_ok=True)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def write_csv(self, lines):
        with open(self.test_file, "w") as f:
            for line in lines:
                f.write(line + "\n")

    def test_mst_basic(self):
        """Перевіряє коректне MST"""
        self.write_csv([
            "A,B,1",
            "B,C,2",
            "A,C,3"
        ])
        result = compute_min_fiber_length(self.test_file)
        self.assertEqual(result, 3)  

    def test_disconnected(self):
        """Окремі компоненти графу"""
        self.write_csv([
            "A,B,5",
            "C,D,7"
        ])
        result = compute_min_fiber_length(self.test_file)
        self.assertEqual(result, -1)

unittest.main()