import unittest
import subprocess

class TestCareer(unittest.TestCase):
    def test_example(self):
        subprocess.run(['python3', 'career.py'])
        
        with open('career.out', 'r') as f:
            result = f.read().strip()
        
        self.assertEqual(result, '12')

unittest.main()

