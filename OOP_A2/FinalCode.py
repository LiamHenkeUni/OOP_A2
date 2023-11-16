'''
File: FinalCode.py
Description: This file is for the final code for the 2nd assignment in Object-Oriented Programming.
Author: Liam Henke.
StudentID: 110377752
EmailID: henld003
This is my own work as defined by the University's Academic Misconduct Policy.
'''

class Laboratory:
    def __init__(self, potions: list, herbs: list, catalysts: list):
        self.__potions = potions
        self.__herbs = herbs
        self.__catalysts = catalysts

class Alchemist:
    def __init__(self, attack: int, strength: int, defense: int, magic: int, ranged: int, necromancy: int, laboratory: Laboratory, recipes: dict):
        self.__attack = attack
        self.__strength = strength
        self.__defense = defense
        self.__magic = magic
        self.__ranged = ranged
        self.__necromancy = necromancy
        self.__laboratory = laboratory
        self.__recipes = recipes

class Reagent:
    def __init__(self, name: str, potency: float):
        self.__name = name
        self.__potency = potency

class Herb(Reagent):
    def __init__(self, name: str, potency: float, grimy: True):
        self.__name = name
        self.__potency = potency
        self.__grimy = grimy

class Catalyst(Reagent):
    def __init__(self, name: str, potency: float, quality: float):
        self.__name = name
        self.__potency = potency
        self.__quality = quality

class Potion:
    def __init__(self, name: str, stat: str, boost: float):
        self.__name = name
        self.__stat = stat
        self.__boost = boost

class SuperPotion(Potion):
    def __init__(self, name: str, stat: str, boost: str, herb: Herb, catalyst: Catalyst):
        self.__name = name
        self.__stat = stat
        self.__boost = boost
        self.__herb = herb
        self.__catalyst = catalyst

class ExtremePotion(Potion):
    def __init__(self, name: str, stat: str, boost: str, reagent: Reagent, potion: Potion):
        self.__name = name
        self.__stat = stat
        self.__boost = boost
        self.__reagent = reagent
        self.__potion = potion