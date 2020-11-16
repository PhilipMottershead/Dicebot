import unittest
from datetime import datetime, timedelta,date
import roller

class TestRollSingleDice(unittest.TestCase):
    def test_RollSingleDice_isWithinRange(self):
        diceSides = "3"
        roll = roller.rollSingleDice(diceSides)
        self.assertLessEqual(roll,int(diceSides))
    
    def test_inputNotNumber(self):
        diceSides = "d"
        roll = roller.rollSingleDice(diceSides)
        self.assertEqual(roll,-1)
       
class TestParseSingleDiceString(unittest.TestCase):
    def test_SingleDiceRoll(self):
        rolls = roller.parseSingleDiceString("d6")
        self.assertEqual(len(rolls),1)
        
    def test_RollSingleDice_MultipleDiceRolls(self):
        rolls = roller.parseSingleDiceString("3d6")
        self.assertEqual(len(rolls),3)

class TestRollDices(unittest.TestCase):
    def test_SingleDice(self):
        rolls = roller.rollDices("!r d6")
        self.assertEqual(len(rolls),1)
        self.assertEqual(len(rolls[0]),1)
    
    def test_MultipleDicesOfSameSides(self):
        rolls = roller.rollDices("!r 5d6")
        self.assertEqual(len(rolls),1)
        self.assertEqual(len(rolls[0]),5)

    def test_SingleDicesOfDifferentSides(self):
        rolls = roller.rollDices("!r d6 d5")
        self.assertEqual(len(rolls),2)
        self.assertEqual(len(rolls[0]),1)
        self.assertEqual(len(rolls[1]),1)

    def test_MultipleDicesOfDifferentSides(self):
        rolls = roller.rollDices("!r 3d6 5d5")
        self.assertEqual(len(rolls),2)
        self.assertEqual(len(rolls[0]),3)
        self.assertEqual(len(rolls[1]),5)
    
if __name__ == '__main__':
    unittest.main()