'''
File: FinalCode.py
Description: This file is for the final code for the 2nd assignment in Object-Oriented Programming.
Author: Liam Henke.
StudentID: 110377752
EmailID: henld003
This is my own work as defined by the University's Academic Misconduct Policy.
'''

class Laboratory:
    def __init__(self, potions, herbs, catalysts):
        pass

class Alchemist:
    def __init__(self, attack, strength, defense, magic, ranged, necromancy, laboratory, recipes):
        pass

class Potion:
    def __init__(self, name, stat, boost):
        pass

class SuperPotion(Potion):
    def __init__(self, name, stat, boost, herb, catalyst):
        pass

class ExtremePotion(Potion):
    def __init__(self, name, stat, boost, reagent, potion):
        pass

class Reagent:
    def __init__(self, name, potency):
        pass

class Herb(Reagent):
    def __init__(self, name, potency, grimy):
        pass

class Catalyst(Reagent):
    def __init__(self, name, potency, quality):
        pass