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
        characterName = "name"
        characterAge = 240
        testCharacter = Character(characterName, characterAge)
        
        self.assertEqual(characterName, testCharacter.getName(), "Name should match")
        self.assertEqual(characterAge, testCharacter.getAge(), "Age should match")

        self.assertNotEqual("randomName", testCharacter.getName(), "Name should not match")
        self.assertNotEqual(40, testCharacter.getAge(), "Age should not match")

if __name__ == '__main__':
    unittest.main()
