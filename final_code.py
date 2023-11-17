'''
File: final_code.py
Description: This file is for the final code for the 2nd assignment in Object-Oriented Programming.
Author: Liam Henke.
StudentID: 110377752
EmailID: henld003
This is my own work as defined by the University's Academic Misconduct Policy.
'''

class Reagent:
    def __init__(self, name: str, potency: float):
        self.__name = name
        self.__potency = potency

    def refine(self):
        pass

    def getName(self):
        return self.__name

    def getPotency(self):
        return self.__potency

    def setPotency(self, potency: float):
        self.__potency = potency

class Herb(Reagent):
    def __init__(self, name: str, potency: float, grimy: bool = True):
        super().__init__(name, potency)
        self.__grimy = grimy

    def refine(self):
        if self.__grimy:
            self.__grimy = False
            self.setPotency(self.getPotency() * 2.5)
            return f"{self.getName()} has been refined. It is now non-grimy, and its potency has been multiplied by 2.5."
    
    def getGrimy(self):
        return self.__grimy

    def setGrimy(self, grimy: bool):
        self.__grimy = grimy

class Catalyst(Reagent):
    def __init__(self, name: str, potency: float, quality: float):
        super().__init__(name, potency)
        self.__quality = quality

    def refine(self):
        if self.__quality < 8.9:
            self.__quality += 1.1
        else:
            print("This catalyst cannot be refined any further.")
    
    def getQuality(self):
        return self.__quality

class Potion:
    def __init__(self, name: str, stat: str, boost: float):
        self.__name = name
        self.__stat = stat
        self.__boost = boost

    def calculateBoost(self):
        return 0.0

    def getName(self):
        return self.__name

    def getStat(self):
        return self.__stat

    def getBoost(self):
        return self.__boost

    def setBoost(self, boost: float):
        self.__boost = boost

class SuperPotion(Potion):
    def __init__(self, name: str, stat: str, boost: float, herb: Herb, catalyst: Catalyst):
        super().__init__(name, stat, boost)
        self.__herb = herb
        self.__catalyst = catalyst

    def calculateBoost(self):
        herb_potency = self.__herb.getPotency()
        catalyst_potency = self.__catalyst.getPotency()
        catalyst_quality = self.__catalyst.getQuality()

        calculated_boost = herb_potency + (catalyst_potency * catalyst_quality) * 1.5
        return round(calculated_boost, 2)
    
    def getHerb(self):
        return self.__herb

    def getCatalyst(self):
        return self.__catalyst

class ExtremePotion(Potion):
    def __init__(self, name: str, stat: str, boost: float, reagent: Reagent, potion: Potion):
        super().__init__(name, stat, boost)
        self.__reagent = reagent
        self.__potion = potion

    def calculateBoost(self):
        reagent_potency = self.__reagent.getPotency()
        super_potion_boost = self.__potion.getBoost()

        calculated_boost = (reagent_potency * super_potion_boost) * 3.0
        return round(calculated_boost, 2)
    
    def getReagent(self):
        return self.__reagent

    def getPotion(self):
        return self.__potion

class Laboratory:
    def __init__(self, potions: list, herbs: list, catalysts: list):
        self.__potions = potions
        self.__herbs = herbs
        self.__catalysts = catalysts

    def get_potions(self):
        return self.__potions

    def get_herbs(self):
        return self.__herbs

    def get_catalysts(self):
        return self.__catalysts
    
    def mixPotion(self, name: str, type: str, stat: str, primaryIngredient: str, secondaryIngredient: str):

        herbs = [herb.getName() for herb in self.get_herbs()]
        catalysts = [catalysts.getName() for catalysts in self.get_catalysts()]
        if type == "Super":
            if primaryIngredient in herbs and secondaryIngredient in catalysts:
                potion = SuperPotion(name, stat, 0.0, primaryIngredient, secondaryIngredient)
                self.__potions.append(potion)
                return f"Potion {name} successfully created."
                
            else:
                return f"Not enough ingredients for {name}"

        elif type == "Extreme":
            if primaryIngredient in herbs or primaryIngredient in catalysts:
                potion = ExtremePotion(name, stat, 0.0, primaryIngredient, secondaryIngredient)
                self.__potions.append(potion)
                return f"Potion {name} successfully created."
            else:
                return(f"Not enough ingredients for {name}")
        else:
            return f"Invalid potion type: {type}."
        

    def addReagent(self, reagent: Reagent, amount: int):
        if isinstance(reagent, Herb):
            self.__herbs.extend([reagent] * amount)
        elif isinstance(reagent, Catalyst):
            self.__catalysts.extend([reagent] * amount)
        else:
            raise ValueError("Invalid reagent type.")

    def refineReagent(self):
        for herb in self.__herbs:
            if isinstance(herb, Herb):
                herb.refine()

        for catalyst in self.__catalysts:
            if isinstance(catalyst, Catalyst):
                catalyst.refine()

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
    
    def getAttack(self):
        return self.__attack

    def getStrength(self):
        return self.__strength
    
    def getDefense(self):
        return self.__defense
    
    def getMagic(self):
        return self.__magic
    
    def getRanged(self):
        return self.__ranged
    
    def getNecromancy(self):
        return self.__necromancy

    def getLaboratory(self):
        return self.__laboratory

    def getRecipes(self):
        return self.__recipes

    def mixPotion(self, recipe: str):
        if recipe in self.__recipes:
            potion_info = self.__recipes[recipe]
            name, primary_ingredient, secondary_ingredient = potion_info
            a = name.split(" ")
            

            # Call the mixPotion method in the Laboratory
            result = self.getLaboratory().mixPotion(name, a[0], a[1], potion_info[1], potion_info[2])
            return result
        else:
            return "Invalid recipe."

    def drinkPotion(self, potion: Potion):
        if isinstance(potion, Potion):
            stat = potion.getStat()
            boost = potion.calculateBoost()

            
            current_stat = getattr(self, f"_{type(self).__name__}__{stat.lower()}", 0)

            
            setattr(self, f"_{type(self).__name__}__{stat.lower()}", current_stat + boost)

            return f"Drank {potion.getName()} potion. {stat} increased by {boost}."
            
    def collectReagent(self, reagent: Reagent, amount: int):
        self.__laboratory.addReagent(reagent, amount)
        
    def refineReagent(self):
        self.__laboratory.refineReagent()