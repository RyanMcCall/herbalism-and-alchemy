class Ingredient():
    def __init__(self, name, rarity, details, DC, regions, description):
        self.name = name
        self.rarity = rarity
        self.details = details
        self.DC = DC
        self.regions = regions
        self.description = description

    def describe(self):
        print(f'Ingredient: {self.name}, rarity: {self.rarity}, details: {self.details}, DC: {self.DC}, regions: {self.regions}, description: {self.description})
        