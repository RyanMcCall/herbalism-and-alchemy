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
    ):
        self.name = name
        self.rarity = rarity
        self.ingredient_type = ingredient_type
        self.details = details
        self.DC = DC
        self.regions = regions
        self.description = description
        self.shorthand = shorthand

    def describe(self):
        print(
            f"""Ingredient: {self.name}, \nrarity: {self.rarity}, \ndetails: {self.details}, 
            \nDC: {self.DC}, \nregions: {self.regions}, \ndescription: {self.description}"""
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
amanita_cap = Ingredient(
    "Amanita Cap",
    "Common",
    "Toxin Modifier",
    "Changes any poison Effect to be non-lethal and only incapacitate the target.",
    1,
    ["Coastal", "Swamp"],
    """This large mushroom is often found growing in clusters near bodies of water, or 
    around other damp terrain. It has a bold blue stem accompanied by a large red cap, 
    which makes this fungi extremely easy to identify. Professional herbalists often cut 
    the head from the root, as the mushroom has the rare ability to re-grow its cap within 
    a few short weeks.""",
    "ACa",
)
basilisks_breath = Ingredient(
    "Basilisk's Breath",
    "Very Rare",
    "Special (Toxin Effect}",
    """Slowly paralyzes opponent. Target makes a DC 5 +
    Alchemy Modifier CON saving throw each turn for 4 turns. While under
    this affect, target is considered slowed by the slow spell. On a failed save,
    the target is considered [paralyzed] for 4 rounds. Cannot be modified or
    altered by other ingredients.""",
    5,
    ["Mountain"],
    """Often referred to as Grey Restraints amongst
    the nobles of the world, this dark grey vine is only rarely found
    atop the highest peaks of mountainous regions. It is fabled that
    this vine is a gift from the gods, as a way to test humanity. Often
    sold for outrageous sums of gold, Basilisk’s Breath can attract
    unwanted attention to those trying to sell it for profit.""",
    "BB",
)
bloodgrass = Ingredient(
    "Bloodgrass",
    "Common",
    "Special (Potion Effect)",
    """Can combine with any other Potion Effect ingredient to become a food source for 1 
    day. Cannot be altered by other ingredients.""",
    0,
    [
        "Arctic",
        "Coastal",
        "Underwater",
        "Desert",
        "Forest",
        "Grasslands",
        "Hills",
        "Mountain",
        "Swamp",
    ],
    """The most boring, common plant life found in the
    wild is this dark brown grass. It has absolutely no remarkable
    qualities, other than being relatively harmless, and its use as basic
    sustenance when properly prepared. Herbalists do not find this
    grass very unique, but still tend to collect it as it occupies almost
    no space in their packs.""",
    "B",
)
blue_toadshade = Ingredient(
    "Blue Toadshade",
    "Rare",
    "Enchantment",
    """User creates a potion of gaseous form (DMG 187)""",
    3,
    ["Coastal", "Forest", "Swamp"],
    """Another common mushroom is this dark blue
    cap with a yellow striped stem. When disturbed, this mushroom
    lets off a puff of blue powder. Usually this causes no permanent
    harm to the surrounding creatures, but it can stain their skin and
    equipment for a short while. The powder is commonly used to
    color various inks and dyes. Herbalists usually search for the fungi
    around small watering holes, where aquatic life often thrives.""",
    "BT",
)
cactus_juice = Ingredient(
    "Cactus Juice",
    "Common",
    "Toxin Modifier",
    """The target will not notice any poison damage Effect in their system until they take 
    5 rounds of damage from the toxin.""",
    2,
    ["Desert", "Grasslands"],
    """This usually clear liquid can be found within most
    cacti around the world. It’s reasonably difficult to extract, as many
    cacti are dangerous to work with. Brewers love to use this juice in
    many recipes, as one of its effects is to delay alcohol intoxication,
    allowing people to purchase and consume more before it hits
    them.""",
    "CJ",
)
chromus_slime = Ingredient(
    "Chromus Slime",
    "Rare",
    "Special (Potion Modifier & Toxin Modifier)",
    """The final Effect after all other calculations is the exact opposite. This is up to 
    the DM's discretion on the specifics per potion/poison.""",
    4,
    ["Coastal", "Underdark"],
    """This thin slime substance is often observed
    to flow within water current as if it had a mind of its own. Often
    times, scientists mistake this slime with mercury, as it has the
    same consistency and look. When attempting to alter the slime, it
    reverberates and alters the other plant life it touches instead.""",
    "CS",
)
cosmos_glond = Ingredient(
    "Cosmos Glond",
    "Rare",
    "Enchantment",
    "User creates a potion of clairvoyance (DMG 187).",
    3,
    ["Coastal", "Desert"],
    """This thin slime substance is often observed
    to flow within water current as if it had a mind of its own. Often
    times, scientists mistake this slime with mercury, as it has the
    same consistency and look. When attempting to alter the slime, it
    reverberates and alters the other plant life it touches instead.""",
    "CG",
)
devils_bloodleaf = Ingredient(
    "Devil's Bloodleaf",
    "Very Rare",
    "Enchantment",
    "User creates a potion of vitality (DMG 188).",
    5,
    ["Hills", "Swamp", "Underdark"],
    """Only a few recorded instances of this red
    and yellow flower exist. This large and bold red leaf can be going
    back in history to the dawn of humankind. It was once a popular
    decoration around homes and gardens, but has become one of the
    rarest plants in the world. It is said to give immense vitality and
    health to one who can properly prepare the plant.""",
    "DB",
)
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
