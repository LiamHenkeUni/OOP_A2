'''
File: test_final_code.py
Description: This file is for the test code for the 2nd assignment in Object-Oriented Programming.
Author: Liam Henke
StudentID: 110377752
EmailID: henld003
This is my own work as defined by the University's Academic Misconduct Policy.
'''

import unittest
from final_code import Alchemist, Herb, Catalyst, Laboratory, SuperPotion, Potion, Reagent, ExtremePotion

class TestReagent(unittest.TestCase):
    def test_refine(self):
        herb = Herb("Rosemary", 10.0)
        result = herb.refine()
        self.assertIn("refined", result)

class TestHerb(unittest.TestCase):
    def test_refine(self):
        herb = Herb("Rosemary", 10.0)
        result = herb.refine()
        self.assertIn("refined", result)

class TestCatalyst(unittest.TestCase):
    def test_refine(self):
        catalyst = Catalyst("Iron", 15.0, 8.0)
        catalyst.refine()
        self.assertEqual(catalyst.getQuality(), 9.1)

class TestPotion(unittest.TestCase):
    def test_calculateBoost(self):
        potion = Potion("Health Potion", "health", 10.0)
        result = potion.calculateBoost()
        self.assertEqual(result, 0.0)

class TestSuperPotion(unittest.TestCase):
    def test_calculateBoost(self):
        herb = Herb("Rosemary", 10.0)
        catalyst = Catalyst("Iron", 15.0, 8.0)
        super_potion = SuperPotion("Super Health Potion", "health", 0.0, herb, catalyst)
        result = super_potion.calculateBoost()
        self.assertEqual(result, 190.0)

class TestExtremePotion(unittest.TestCase):
    def test_calculateBoost(self):
        reagent = Reagent("TestReagent", 5.0)
        potion = Potion("TestPotion", "test", 3.0)
        extreme_potion = ExtremePotion("Extreme Test Potion", "test", 0.0, reagent, potion)
        result = extreme_potion.calculateBoost()
        self.assertEqual(result, 45.0)

class TestLaboratory(unittest.TestCase):
    def test_mixPotion(self):
        laboratory = Laboratory([], [], [])
        herb = Herb("Rosemary", 10.0)
        catalyst = Catalyst("Iron", 15.0, 8.0)
        laboratory.addReagent(herb, 1)
        laboratory.addReagent(catalyst, 1)
        result = laboratory.mixPotion("Test Potion", "Super", "health", herb.getName(), catalyst.getName())
        self.assertIn("successfully created", result)

    def test_refineReagent(self):
        laboratory = Laboratory([], [], [])
        herb = Herb("Rosemary", 10.0)
        catalyst = Catalyst("Iron", 15.0, 8.0)
        laboratory.addReagent(herb, 1)
        laboratory.addReagent(catalyst, 1)
        laboratory.refineReagent()
        self.assertEqual(herb.getPotency(), 25.0)
        self.assertEqual(catalyst.getQuality(), 9.1)

class TestAlchemist(unittest.TestCase):
    def test_mixPotion_invalidRecipe(self):
        laboratory = Laboratory([], [], [])
        alchemist = Alchemist(10, 15, 20, 5, 12, 8, laboratory, {})
        result = alchemist.mixPotion("invalid_recipe")
        self.assertIn("Invalid recipe.", result)
        self.assertNotIn("successfully created", result)

    def test_drinkPotion(self):
        laboratory = Laboratory([], [], [])
        alchemist = Alchemist(10, 15, 20, 5, 12, 8, laboratory, {})
        potion = Potion("Test Potion", "health", 10.0)
        result = alchemist.drinkPotion(potion)
        self.assertIn("increased", result)

    def test_collectHerb(self):
        laboratory = Laboratory([], [], [])
        alchemist = Alchemist(10, 15, 20, 5, 12, 8, laboratory, {})
        herb = Herb("Rosemary", 10.0)
        alchemist.collectReagent(herb, 2)
        self.assertEqual(len(laboratory.get_herbs()), 2)

    def test_refineReagent(self):
        laboratory = Laboratory([], [], [])
        alchemist = Alchemist(10, 15, 20, 5, 12, 8, laboratory, {})
        herb = Herb("Rosemary", 10.0)
        catalyst = Catalyst("Iron", 15.0, 8.0)
        laboratory.addReagent(herb, 1)
        laboratory.addReagent(catalyst, 1)
        alchemist.refineReagent()
        self.assertEqual(herb.getPotency(), 25.0)
        self.assertEqual(catalyst.getQuality(), 9.1)

if __name__ == "__main__":
    unittest.main()
