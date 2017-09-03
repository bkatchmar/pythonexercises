import unittest
import sys
sys.path.append('./classes')

import pets

class TestClassInstance(unittest.TestCase):
    def testinstances(self):
        randompet = pets.Pet("Brutus", 5)
        mydog = pets.Dog("Brutus", 2)
        mycat = pets.Cat("Floyd", 10)

        self.assertIsInstance(mydog, pets.Pet)
        self.assertIsInstance(mydog, pets.Dog)
        self.assertFalse(isinstance(mydog, pets.Cat))
        
# python -m unittest standardpythonunittests