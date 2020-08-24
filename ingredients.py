class Ingredient():
    def __init__(self, name, rarity, details, DC, regions, description):
        self.name = name
        self.rarity = rarity
        self.details = details
        self.DC = DC
        self.regions = regions
        self.description = description

    def describe(self):
        print(f'Ingredient: {self.name}, \nrarity: {self.rarity}, \ndetails: {self.details}, \nDC: {self.DC}, \nregions: {self.regions}, \ndescription: {self.description}')