import unittest, sys

from pathlib import Path

path = str(Path(Path(__file__).parent.absolute()).parent.absolute())

sys.path.insert(0, path)

from Character import Character

print(sys.path)

class TestCharacterMethods(unittest.TestCase):
    def setUp(self):
        pass

    def test_character_creation(self):
        
        testCharacter = Character("Name", 240)
        
        self.assertEqual("Name", testCharacter.getName())
        self.assertEqual(240, testCharacter.getAge())

if __name__ == '__main__':
    unittest.main()
