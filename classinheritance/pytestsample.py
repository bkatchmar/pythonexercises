# pytest pytestsample.py
import sys
sys.path.append('./classes')

import pets

def test_answer():
    randompet = pets.Pet("Brutus", 5)
    mydog = pets.Dog("Brutus", 2)
    mycat = pets.Cat("Floyd", 10)
        
    assert(isinstance(mydog, pets.Pet))
    assert(isinstance(mydog, pets.Dog))
    assert(not isinstance(mydog, pets.Cat))