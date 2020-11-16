import unittest
from datetime import datetime, timedelta,date
import Roller

class TestRollSingleDice(unittest.TestCase):
    def test_RollSingleDice_isWithinRange(self):
        diceSides = "3"
        roll = Roller.rollSingleDice(diceSides)
        self.assertLessEqual(roll,int(diceSides))
    
    def test_inputNotNumber(self):
        diceSides = "d"
        roll = Roller.rollSingleDice(diceSides)
        self.assertEqual(roll,-1)
       
class TestParseSingleDiceString(unittest.TestCase):
    def test_SingleDiceRoll(self):
        rolls = Roller.parseSingleDiceString("d6")
        self.assertEqual(len(rolls),1)
        
    def test_RollSingleDice_MultipleDiceRolls(self):
        rolls = Roller.parseSingleDiceString("3d6")
        self.assertEqual(len(rolls),3)

class TestRollDices(unittest.TestCase):
    def test_SingleDice(self):
        rolls = Roller.rollDices("!r d6")
        self.assertEqual(len(rolls),1)
        self.assertEqual(len(rolls[0]),1)
    
    def test_MultipleDicesOfSameSides(self):
        rolls = Roller.rollDices("!r 5d6")
        self.assertEqual(len(rolls),1)
        self.assertEqual(len(rolls[0]),5)

    def test_SingleDicesOfDifferentSides(self):
        rolls = Roller.rollDices("!r d6 d5")
        self.assertEqual(len(rolls),2)
        self.assertEqual(len(rolls[0]),1)
        self.assertEqual(len(rolls[1]),1)

    def test_MultipleDicesOfDifferentSides(self):
        rolls = Roller.rollDices("!r 3d6 5d5")
        self.assertEqual(len(rolls),2)
        self.assertEqual(len(rolls[0]),3)
        self.assertEqual(len(rolls[1]),5)
    
if __name__ == '__main__':
    unittest.main()