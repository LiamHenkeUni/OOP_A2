'''
File: final_code.py
Description: This file is for the final code for the 2nd assignment in Object-Oriented Programming.
Author: Liam Henke.
StudentID: 110377752
EmailID: henld003
This is my own work as defined by the University's Academic Misconduct Policy.
'''

class Reagent:
    """Class representing a generic reagent."""
    def __init__(self, name: str, potency: float):
        """Initialize a reagent with a name and potency."""
        self.__name = name
        self.__potency = potency

    def refine(self):
        """Placeholder method for refining the reagent."""
        pass

    def getName(self):
        """Get the name of the reagent."""
        return self.__name

    def getPotency(self):
        """Get the potency of the reagent."""
        return self.__potency

    def setPotency(self, potency: float):
        """Set the potency of the reagent."""
        self.__potency = potency

class Herb(Reagent):
    """Class representing a herb reagent."""
    def __init__(self, name: str, potency: float, grimy: bool = True):
        """Initialize a herb with a name, potency, and grimy status."""
        super().__init__(name, potency)
        self.__grimy = grimy

    def refine(self):
        """Refine the herb, making it non-grimy and increasing potency."""
        if self.__grimy:
            self.__grimy = False
            self.setPotency(self.getPotency() * 2.5)
            return f"{self.getName()} has been refined. It is now non-grimy, and its potency has been multiplied by 2.5."
    
    def getGrimy(self):
        """Get the grimy status of the herb."""
        return self.__grimy

    def setGrimy(self, grimy: bool):
        """Set the grimy status of the herb."""
        self.__grimy = grimy

class Catalyst(Reagent):
    """Class representing a catalyst reagent."""
    def __init__(self, name: str, potency: float, quality: float):
        """Initialize a catalyst with a name, potency, and quality."""
        super().__init__(name, potency)
        self.__quality = quality

    def refine(self):
        """Refine the catalyst by increasing its quality if below a certain threshold."""
        if self.__quality < 8.9:
            self.__quality += 1.1
        else:
            print("This catalyst cannot be refined any further.")
    
    def getQuality(self):
        """Get the quality of the catalyst."""
        return self.__quality

class Potion:
    """Class representing a generic potion."""
    def __init__(self, name: str, stat: str, boost: float):
        """Initialize a potion with a name, stat, and boost."""
        self.__name = name
        self.__stat = stat
        self.__boost = boost

    def calculateBoost(self):
        """Placeholder method for calculating the boost of the potion."""
        return 0.0

    def getName(self):
        """Get the name of the potion."""
        return self.__name

    def getStat(self):
        """Get the stat affected by the potion."""
        return self.__stat

    def getBoost(self):
        """Get the boost provided by the potion."""
        return self.__boost

    def setBoost(self, boost: float):
        """Set the boost provided by the potion."""
        self.__boost = boost

class SuperPotion(Potion):
    """Class representing a super potion."""
    def __init__(self, name: str, stat: str, boost: float, herb: Herb, catalyst: Catalyst):
        """Initialize a super potion with a name, stat, boost, herb, and catalyst."""
        super().__init__(name, stat, boost)
        self.__herb = herb
        self.__catalyst = catalyst

    def calculateBoost(self):
        """Calculate the boost provided by the super potion."""
        herb_potency = self.__herb.getPotency()
        catalyst_potency = self.__catalyst.getPotency()
        catalyst_quality = self.__catalyst.getQuality()

        calculated_boost = herb_potency + (catalyst_potency * catalyst_quality) * 1.5
        return round(calculated_boost, 2)
    
    def getHerb(self):
        """Get the herb used in the super potion."""
        return self.__herb

    def getCatalyst(self):
        """Get the catalyst used in the super potion."""
        return self.__catalyst

class ExtremePotion(Potion):
    """Class representing an extreme potion."""
    def __init__(self, name: str, stat: str, boost: float, reagent: Reagent, potion: Potion):
        """Initialize an extreme potion with a name, stat, boost, reagent, and base potion."""
        super().__init__(name, stat, boost)
        self.__reagent = reagent
        self.__potion = potion

    def calculateBoost(self):
        """Calculate the boost provided by the extreme potion."""
        reagent_potency = self.__reagent.getPotency()
        super_potion_boost = self.__potion.getBoost()

        calculated_boost = (reagent_potency * super_potion_boost) * 3.0
        return round(calculated_boost, 2)
    
    def getReagent(self):
        """Get the reagent used in the extreme potion."""
        return self.__reagent

    def getPotion(self):
        """Get the base potion used in the extreme potion."""
        return self.__potion

class Laboratory:
    """Class representing a laboratory."""
    def __init__(self, potions: list, herbs: list, catalysts: list):
        """Initialize a laboratory with lists of potions, herbs, and catalysts."""
        self.__potions = potions
        self.__herbs = herbs
        self.__catalysts = catalysts

    def get_potions(self):
        """Get the list of potions in the laboratory."""
        return self.__potions

    def get_herbs(self):
        """Get the list of herbs in the laboratory."""
        return self.__herbs

    def get_catalysts(self):
        """Get the list of catalysts in the laboratory."""
        return self.__catalysts
    
    def mixPotion(self, name: str, type: str, stat: str, primaryIngredient: str, secondaryIngredient: str):
        """Mix a potion in the laboratory based on ingredients."""
        herbs = [herb.getName() for herb in self.get_herbs()]
        catalysts = [catalyst.getName() for catalyst in self.get_catalysts()]
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
                return f"Not enough ingredients for {name}"
        else:
            return f"Invalid potion type: {type}."
        

    def addReagent(self, reagent: Reagent, amount: int):
        """Add reagents to the laboratory."""
        if isinstance(reagent, Herb):
            self.__herbs.extend([reagent] * amount)
        elif isinstance(reagent, Catalyst):
            self.__catalysts.extend([reagent] * amount)
        else:
            raise ValueError("Invalid reagent type.")

    def refineReagent(self):
        """Refine herbs and catalysts in the laboratory."""
        for herb in self.__herbs:
            if isinstance(herb, Herb):
                herb.refine()

        for catalyst in self.__catalysts:
            if isinstance(catalyst, Catalyst):
                catalyst.refine()

class Alchemist:
    """Class representing an alchemist."""
    def __init__(self, attack: int, strength: int, defense: int, magic: int, ranged: int, necromancy: int, laboratory: Laboratory, recipes: dict):
        """Initialize an alchemist with stats, a laboratory, and recipes."""
        self.__attack = attack
        self.__strength = strength
        self.__defense = defense
        self.__magic = magic
        self.__ranged = ranged
        self.__necromancy = necromancy
        self.__laboratory = laboratory
        self.__recipes = recipes

    def getLaboratory(self):
        """Get the laboratory of the alchemist."""
        return self.__laboratory

    def getRecipes(self):
        """Get the recipes of the alchemist."""
        return self.__recipes

    def mixPotion(self, recipe: str):
        """Mix a potion based on a recipe."""
        if recipe in self.__recipes:
            potion_info = self.__recipes[recipe]
            name, primary_ingredient, secondary_ingredient = potion_info
            a = name.split(" ")
            
            result = self.getLaboratory().mixPotion(name, a[0], a[1], potion_info[1], potion_info[2])
            return result
        else:
            return "Invalid recipe."

    def drinkPotion(self, potion: Potion):
        """Drink a potion and increase stats accordingly."""
        if isinstance(potion, Potion):
            stat = potion.getStat()
            boost = potion.calculateBoost()

            
            current_stat = getattr(self, f"_{type(self).__name__}__{stat.lower()}", 0)

            
            setattr(self, f"_{type(self).__name__}__{stat.lower()}", current_stat + boost)

            return f"Drank {potion.getName()} potion. {stat} increased by {boost}."
            
    def collectReagent(self, reagent: Reagent, amount: int):
        """Collect reagents and add them to the laboratory."""
        self.__laboratory.addReagent(reagent, amount)
        
    def refineReagent(self):
        """Refine herbs and catalysts in the laboratory."""
        self.__laboratory.refineReagent()
