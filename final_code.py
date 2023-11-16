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
        pass

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
        primary_found = False
        secondary_found = False

        primary_herb = None
        secondary_catalyst = None

        for herb in self.__herbs:
            if herb.getName() == primaryIngredient:
                primary_found = True
                primary_herb = herb
            elif herb.getName() == secondaryIngredient:
                secondary_found = True

        for catalyst in self.__catalysts:
            if catalyst.getName() == primaryIngredient:
                primary_found = True
            elif catalyst.getName() == secondaryIngredient:
                secondary_found = True
                secondary_catalyst = catalyst

        # Check if both primary and secondary ingredients are found
        if primary_found and secondary_found:
            if type == "Super":
                potion = SuperPotion(name, stat, 0.0, primary_herb, secondary_catalyst)
            elif type == "Extreme":
                potion = ExtremePotion(name, stat, 0.0, reagent, secondary_catalyst)
            else:
                print("Invalid potion type.")
                return

            self.__potions.append(potion)
            print(f"Potion {name} successfully created.")

            # Remove used ingredients from the laboratory
            self.__herbs.remove(primary_herb)
            self.__catalysts.remove(secondary_catalyst)
        else:
            print("Insufficient ingredients to create the potion.")

    def addReagent(self, reagent: Reagent, amount: int):
        if isinstance(reagent, Herb):
            self.__herbs.extend([reagent] * amount)
        elif isinstance(reagent, Catalyst):
            self.__catalysts.extend([reagent] * amount)
        else:
            print("Invalid reagent type.")

    def refineReagent(self):
        for herb in self.__herbs:
            if isinstance(herb, Herb):
                herb.refine()

        for catalyst in self.__catalysts:
            if isinstance(catalyst, Catalyst):
                catalyst.refine()

    def getPotions(self):
        return self.__potions
    
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
            print(a)

            # Call the mixPotion method in the Laboratory
            self.getLaboratory().mixPotion(name, a[0], a[1], potion_info[1], potion_info[2])
        else:
            print("Invalid recipe.")

    def drinkPotion(self, potion: Potion):
        if isinstance(potion, Potion):
            stat = potion.getStat()
            boost = potion.calculateBoost()

            current_stat = getattr(self, f"_{type(self).__name__}__{stat.lower()}")
            setattr(self, f"_{type(self).__name__}__{stat.lower()}", current_stat + boost)

            print(f"Drank {potion.getName()} potion. {stat} increased by {boost}.")
            
    def collectReagent(self, reagent: Reagent, amount: int):
        self.__laboratory.addReagent(reagent, amount)

    def refineReagent(self):
        self.__laboratory.refineReagent()



# Create an Alchemist and a Laboratory
alchemist = Alchemist(80, 90, 70, 60, 85, 40, Laboratory([], [], []), {"Super Attack": ["Super Attack", "Irit", "Eye of Newt"],
    "Super Strength": ["Super Strength", "Kwuarm", "Limpwurt Root"],
    "Super Defence": ["Super Defence", "Cadantine", "White Berries"],
    "Super Magic": ["Super Magic", "Lantadyme", "Potato Cactus"],
    "Super Ranging": ["Super Ranging", "Dwarf Weed", "Wine of Zamorak"],
    "Super Necromancy": ["Super Necromancy", "Arbuck", "Blood of Orcus"],
    "Extreme Attack": ["Extreme Attack", "Avantoe", "Super Attack"],
    "Extreme Strength": ["Extreme Strength", "Dwarf Weed", "Super Strength"],
    "Extreme Defence": ["Extreme Defence", "Lantadyme", "Super Defence"],
    "Extreme Magic": ["Extreme Magic", "Ground Mud Rune", "Super Magic"],
    "Extreme Ranging": ["Extreme Ranging", "Grenwall Spike", "Super Ranging"],
    "Extreme Necromancy": ["Extreme Necromancy", "Ground Miasma Rune", "Super Necromancy"],
})

# Create herbs
arbuck_herb = Herb("Arbuck", 2.6)
avantoe_herb = Herb("Avantoe", 3.0)
cadantine_herb = Herb("Cadantine", 1.5)
dwarf_weed_herb = Herb("Dwarf Weed", 2.5)
irit_herb = Herb("Irit", 1.0)
kwuarm_herb = Herb("Kwuarm", 1.2)
lantadyme_herb = Herb("Lantadyme", 2.0)
torstol_herb = Herb("Torstol", 4.5)

# Create catalysts
eye_of_newt_catalyst = Catalyst("Eye of Newt", 4.3, 1.0)
limpwurt_root_catalyst = Catalyst("Limpwurt Root", 3.6, 1.7)
white_berries_catalyst = Catalyst("White Berries", 1.2, 2.0)
potato_cactus_catalyst = Catalyst("Potato Cactus", 7.3, 0.1)
wine_of_zamorak_catalyst = Catalyst("Wine of Zamorak", 1.7, 5.0)
blood_of_orcus_catalyst = Catalyst("Blood of Orcus", 4.5, 2.2)
ground_mud_rune_catalyst = Catalyst("Ground Mud Rune", 2.1, 6.7)
grenwall_spike_catalyst = Catalyst("Grenwall Spike", 6.3, 4.9)
ground_miasma_rune_catalyst = Catalyst("Ground Miasma Rune", 3.3, 5.2)

# Add herbs and catalysts to the laboratory
alchemist.getLaboratory().addReagent(arbuck_herb, 5)
alchemist.getLaboratory().addReagent(avantoe_herb, 5)
alchemist.getLaboratory().addReagent(cadantine_herb, 5)
alchemist.getLaboratory().addReagent(dwarf_weed_herb, 5)
alchemist.getLaboratory().addReagent(irit_herb, 5)
alchemist.getLaboratory().addReagent(kwuarm_herb, 5)
alchemist.getLaboratory().addReagent(lantadyme_herb, 5)
alchemist.getLaboratory().addReagent(torstol_herb, 5)

alchemist.getLaboratory().addReagent(eye_of_newt_catalyst, 5)
alchemist.getLaboratory().addReagent(limpwurt_root_catalyst, 5)
alchemist.getLaboratory().addReagent(white_berries_catalyst, 5)
alchemist.getLaboratory().addReagent(potato_cactus_catalyst, 5)
alchemist.getLaboratory().addReagent(wine_of_zamorak_catalyst, 5)
alchemist.getLaboratory().addReagent(blood_of_orcus_catalyst, 5)
alchemist.getLaboratory().addReagent(ground_mud_rune_catalyst, 5)
alchemist.getLaboratory().addReagent(grenwall_spike_catalyst, 5)
alchemist.getLaboratory().addReagent(ground_miasma_rune_catalyst, 5)



for recipe in alchemist.getRecipes():
    alchemist.mixPotion(recipe)

# Print the current state of the laboratory
print("\nCurrent state of the laboratory:")
print("Herbs:", [herb.getName() for herb in alchemist.getLaboratory().get_herbs()])
print("Catalysts:", [catalyst.getName() for catalyst in alchemist.getLaboratory().get_catalysts()])
print("Potions:", [potion.getName() for potion in alchemist.getLaboratory().get_potions()])

