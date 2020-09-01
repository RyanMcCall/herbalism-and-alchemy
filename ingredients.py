class Ingredient:
    def __init__(
        self,
        name,
        rarity,
        ingredient_type,
        details,
        DC,
        regions,
        description,
        shorthand,
        special_rolling=None,
    ):
        self.name = name
        self.rarity = rarity
        self.ingredient_type = ingredient_type
        self.details = details
        self.DC = DC
        self.regions = regions
        self.description = description
        self.shorthand = shorthand
        self.special_rolling = special_rolling

    def describe(self):
        print(
            f"Ingredient: {self.name}, \nrarity: {self.rarity}, \ndetails: {self.details}, \nDC: {self.DC}, \nregions: {self.regions}, \ndescription: {self.description}"
        )


arctic_creeper = Ingredient(
    "Arctic Creeper",
    "Common",
    "Toxin Modifier",
    "Heals for 2d4 + Alchemy Modifier",
    2,
    ["Arctic", "Mountain"],
    """This noxious weed usually grows in extremely cold 
                            environments, or at higher elevations where snow tends to 
                            accumulate. The leaves of the plant characterized by a pleasant 
                            sweet minty flavor, whereas the root is bitter and acidic. The 
                            weed is one of an assassin’s favorite plants, due to the root’s 
                            ability to freeze a creature’s bloodstream, which leads to a 
                            slow and agonizing death. The Arctic Creeper is toxic to many 
                            unwary travelers, as it is quite easy to consume the root’s 
                            toxins while enjoying the sweet flavorsome leaves.""",
    "ACr",
    "2x",
)
arrow_root = Ingredient(
    "Arrow Root",
    "Uncommon",
    "Enchantment",
    "+1 to attack rolls for one minute when applied to a weapon.",
    2,
    ["Desert", "Forest", "Grasslands"],
    """This unusually elongated plant can stand up to
                        four feet tall, and is very easy to spot due to its distinctive white
                        and brown speckled pattern. The Arrow Root thrives in desert
                        and drought environments, as the plant needs very little water to
                        survive. When diced and boiled in water the plant creates a frothy
                        silver liquid, which is ideal for sharpening and polishing weapons
                        and armor without the use of magic or other means.""",
    "AR",
)
amanita_cap = None
basilisks_breath = None
bloodgrass = None
blue_toadshade = None
cactus_juice = None
chromus_slime = None
cosmos_glond = None
devils_bloodleaf = None
drakus_flower = None
dried_ephedra = None
elemental_water = None
emetic_wax = None
fennel_silk = None
fiends_ivy = None
frozen_seedlings = None
harrada_leaf = None
hyancinth_nectar = None
hydrathistle = None
ironwood_heart = None
lavender_sprig = None
luminous_cap_dust = None
mandrake_root = None
milkweed_seeds = None
mortflesh_powder = None
nightshade_berries = None
primordial_balm = None
quicksilver_lichen = None
radiant_synthseed = None
rock_vine = None
scillia_beans = None
silver_hibiscus = None
spineflower_berries = None
tail_leaf = None
verdant_nettle = None
voidroot = None
wild_sageroot = None
wisp_stalks = None
wrackwort_bulbs = None
wyrmtongue_petals = None
