import sys

from pathlib import Path

path = str(Path(Path(__file__).parent.absolute()).parent.absolute())

sys.path.insert(0, path)

from src.character import Character


class TestCharacterMethods():
    def test_character_creation(self):
        characterName = "name"
        characterAge = 240
        testCharacter = Character(characterName, characterAge)
        
        assert characterName == testCharacter.getName()
        assert characterAge  == testCharacter.getAge()
        assert characterAge // 12 == testCharacter.getFormatedAge()["years"]
        assert characterAge % 12  == testCharacter.getFormatedAge()["months"]

        assert "randomName" != testCharacter.getName()
        assert 40 != testCharacter.getAge()

