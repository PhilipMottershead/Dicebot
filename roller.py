import random

def rollDices(dice:str):
    diceSizes =dice.split(" ")
    rolls = []
    for dice in diceSizes:
        if "d" in dice:
            rolls.append(parseSingleDiceString(dice))
    return rolls

def parseSingleDiceString(dice:str):
    diceSizes1 =dice.split("d")
    roll_num = 0
    max_rolls = 0
    rolls = []
    
    if diceSizes1[0].isdigit():
        max_rolls = int(diceSizes1[0])
    elif diceSizes1[0] == "":
        max_rolls = 1
    
    while(max_rolls>roll_num):
        rolls.append(rollSingleDice(diceSizes1[1]))
        roll_num = roll_num + 1
    return rolls


def rollSingleDice(diceSides):
    if diceSides.isdigit() :
        size = int(diceSides)
        return random.randint(1,size)
    else: 
        return -1
