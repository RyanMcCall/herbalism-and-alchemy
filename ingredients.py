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
drakus_flower = Ingredient(
    "Drakus Flower",
    "Common",
    "Toxin Modifier",
    """Change poison damage to fire or acid damage; target is
    still [poisoned] for 1 minute on a failed CON saving throw; this toxin is still
    considered poison damage when combining with other ingredients.""",
    2,
    ["Desert", "Grasslands", "Moutain"],
    """This bright red and pale green flower can be
    found in both temperate and warm environments. It’s a natural
    favorite amongst entertainers, due to the petal’s ability to ignite
    with a moderate application of friction. This ignition does not
    cause harm, but instead creates theatrical sparks with the ability
    to light fires and create warmth.""",
    "DF",
)
dried_ephedra = Ingredient(
    "Dried Ephedra",
    "Uncommon",
    "Potion Modifier",
    "Increase the dice-type by 1 size for any healing Effect.",
    2,
    ["Desert", "Mountain"],
    """A bush often found in dry environments, it is
    thorny and hard to harvest without scratching your skin. It has a
    distinct dark purple hue when viewed at a distance, but up close it
    looks black. Herbalists love to use this plant when making healing
    tonics as it has the odd ability to enhance Wild Sageroot.""",
    "DE",
)
elemental_water = Ingredient(
    "Elemental Water",
    "Rare",
    "Special (Enchantment)",
    "This is required as the base catalyst for all Enchantment ingredients.",
    3,
    ["Special"],
    """This unique liquid shares properties of
    the planar realms of the 4 elements. At times you can see rocks
    floating unnaturally in the middle and at other times you can
    swear you see fire in the water. This special water can be found in
    all environments as it is not bound to our physical world’s rules.""",
    "EWat",
)
emetic_wax = Ingredient(
    "Emetic Wax",
    "Common",
    "Special (Potion Modifier & Toxin Modifier",
    "Delay the Effect of an ingredient this was combined with by 1d6 rounds.",
    2,
    ["Forest", "Swamp"],
    """This thick, white wax is often found seeping out
    of trees near lush and wet areas. It is commonly used in candle
    making, as the wax melts and re-hardens rather quickly, yet is
    strong enough to form delicate shapes. Herbalists use it to control
    how their tonics enter the body, performing miraculous feats.""",
    "EWax",
)
fennel_silk = Ingredient(
    "Fennel Silk",
    "Common",
    "Potion Effect",
    """Stabilizes body heat to resist cold weather or wet condition penalties for 1 hour. 
    Cannot be altered by other ingredients.""",
    2,
    ["Arctic", "Underdark"],
    """Often mistaken for a spider’s web, this white
    web like plant grows amongst frigid and dark environments.
    It uses sharp hooked tendrils to help secure the edges of the
    plant to nearby rocks or plants. Adventurers that are adept in
    the use of Fennel Silk will recognize the many applications it
    has for protecting your extremities from harsh-low temperature
    environments.""",
    "FS",
)
fiends_ivy = Ingredient(
    "Fiend's Ivy",
    "Rare",
    "Enchantment",
    "User creates a potion of mind reading (DMG 188)",
    4,
    ["Arctic", "Underdark"],
    """These long, red thorn-encrusted vines can stretch
    up to 3 feet long and have sharp thorns that reach up to an inch
    or two long. It isn’t rare to find blood stains amongst these vines
    as many animals and adventurers can easily trip or get caught
    in a bushel of the vines. The vines also seem to have a sentient
    quality to them as they relax when prey is near, and contract when
    captured.""",
    "FI",
)
frozen_seedlings = Ingredient(
    "Frozen Seedlings",
    "Rare",
    "Toxin Modifier",
    """While poisoned, target’s movement speed is reduced by 10 ft for 1 minute. Cannot be 
    altered by other ingredients.""",
    4,
    ["Arctic", "Mountain"],
    """These small, pea sized pods can be found
    amongst resilient flowers in very cold environments. Named for
    their almost frozen appearance, they can be plucked with relative
    ease and are often used in cold alcoholic drinks. Some assassins
    have found ways to crush these into a paste and hamper one’s
    movements.""",
    "FS",
)
harrada_leaf = Ingredient(
    "Harrada Leaf",
    "Common",
    "Toxin Modifier",
    """While [poisoned], target has disadvantage on ability checks. Cannot be altered by 
    other ingredients.""",
    1,
    ["Forest"],
    """This huge yellow leaf can often be found near
    tree tops in lush environments. It is often cultivated and harvested
    by gangs or the Thieves Guilds to be sold as a street drug. The
    potent nature of this addictive substance will cause a brief
    euphoric state coupled with an increase in a specific attribute;
    followed by a long recovery period in which the user is extremely
    weakened in that attribute.""",
    "HL",
)
hyancinth_nectar = Ingredient(
    "Hyancinth Nectar",
    "Common",
    "Potion Effect",
    """Removes 1d6 rounds of poison in the target’s system, but cannot remove it completely. 
    One round of poison damage will still occur at minimum.""",
    1,
    ["Coastal", "Grasslands"],
    """This blue and white thick liquid can be
    extracted from the Hyancinth’s near somewhat wet areas. This
    nectar is of high demand and is often used by highly trained
    guards to counter poisons that evil people attempt to use on them.
    While it does not cure the mean of poisons, it severely limits its
    effects.""",
    "HN",
)
hydrathistle = Ingredient(
    "Hydrathistle",
    "Uncommon",
    "Enchantment",
    "User creates a potion of water breathing (DMG 188)",
    2,
    ["Coastal, Swamp"],
    """Named for its appearance, this three-
    pronged blue and black flower is often found in dark and dank
    environments. When used alone, the thistle has no real beneficial
    effects. However, skilled alchemists have been able to use highly
    powerful and natural water to concoct potions that allow them to
    breath in water.""",
    "H",
)
ironwood_heart = Ingredient(
    "Ironwood Heart",
    "Uncommon",
    "Enchantment",
    "User creates a potion of growth (DMG 187)",
    3,
    ["Arctic", "Forest", "Hills"],
    """This gnarled white seed is commonly found in
    the nooks of Ironwood Trees. These large seeds pulse with a slow
    repetitive beat when gripped tightly, often referred to as “Nature’s
    Heartbeat”. It is said that when cooked or properly prepared by a
    Herbalist these seeds can increase a beings physical size greatly.""",
    "IH",
)
lavender_sprig = Ingredient(
    "Lavender Sprig",
    "Common",
    "Special (Potion Modifier & Toxin Modifier)",
    "Makes the potion or toxin more stable and safer to craft.",
    -2,
    ["Coastal", "Grasslands", "Hills"],
    """These long stemmed purple-petal flowers can
    often be found swaying in the wind in huge patches. They are very
    common amongst green environments and have a distinct sweet
    smell. However, they taste extremely bitter when eaten.""",
    "LS",
)
luminous_cap_dust = Ingredient(
    "Luminous Cap Dust",
    "Rare",
    "Enchantment",
    "User creates a potion of heroism (DMG 188).",
    4,
    ["Mountain", "Underdark"],
    """This powder can be shook from the
    glowing yellow mushrooms often found in extremely dark
    environments and it keeps an ember-like glow for about a week
    after extracted. Many Herbalists keep the glowing mushrooms
    themselves in dark cellars in order to harvest this dust every
    chance they can.""",
    "LCD",
)
mandrake_root = Ingredient(
    "Mandrake Root",
    "Common",
    "Potion Effect",
    """Reduce any disease or poison’s potency by half for 2d12
    ours. Only hinders already existing poisons or diseases in the body.
    Cannot be altered by other ingredients.""",
    0,
    [
        "Arctic",
        "Coastal",
        "Underwater",
        "Desert",
        "Forest",
        "Grasslands",
        "Hills",
        "Swamp",
    ],
    """This tan root has serrated edges all along
    its body that often cause injury to Herbalists that do not properly
    know how to handle it. When stripped of its outer skin, the soft
    tender center can be eaten with relative ease and is often used by
    Doctors to reduce pain from poison or disease.""",
    "MR",
)
milkweed_seeds = Ingredient(
    "Milkweed Seeds",
    "Common",
    "Potion Modifier",
    """Double the dice rolled of any healing Effect, but remove all Alchemy Modifier bonuses. 
    This modifier can stack.""",
    2,
    [
        "Arctic",
        "Coastal",
        "Underwater",
        "Desert",
        "Forest",
        "Grasslands",
        "Hills",
        "Swamp",
    ],
    """These small, white translucent seeds can
    be found when opening up a Milkweed Flower. They are often
    eaten by children due to their friendly look, but can cause negative
    digestive effects this way. When crushed up and diluted with other
    liquid these seeds offer very powerful healing effects.""",
    "MS",
)
mortflesh_powder = Ingredient(
    "Mortflesh Powder",
    "Very Rare",
    "Enchantment",
    "User creates a potion of longevity (DMG 188).",
    5,
    ["Arctic", "Underdark"],
    """This dark purple powder is often found
    growing on top of moss in dark, cold environments. This powder
    is often used as makeup for young men and women to reduce
    the look of age from their faces. When imbibed with a magical
    catalyst, the effect is said to be permanent when consumed.""",
    "MP",
)
nightshade_berries = Ingredient(
    "Nightshade Berries",
    "Uncommon",
    "Enchantment",
    """The effect of this "potion" is similiar to the oil of slipperiness (DMG 184).""",
    3,
    ["Forest", "Hills"],
    """These light blue berries can be found in
    small clumped packs among small bushes in lush environments.
    They can be safely ingested and are often eaten by wild animals
    for their sweet, but tangy flavor. A skilled Herbalist can enhance
    the berries natural ability to affect a persons body.""",
    "NB",
)
primordial_balm = Ingredient(
    "Primordial Balm",
    "Rare",
    "Enchantment",
    "User creates a potion of frost/fire/stone giant strength (DMG 187)",
    4,
    ["Mountain", "Swamp", "Underdark"],
    """This thick substance has been observed
    changing its coloring, almost at will. The balm is unusually warm
    to the touch, and can seem to retain heat for weeks on end.
    Herbalists often find this substance growing on rocks in humid
    environments. The exact rarity of the substance is unknown, as its
    constantly changing appearance makes it difficult to identify.""",
    "PB",
)
quicksilver_lichen = Ingredient(
    "Quicksilver Lichen",
    "Uncommon",
    "Toxin Modifier",
    """Double the dice rolled of any Toxin Effect, but reduce that
    Effect duration by half. This modifier can stack.""",
    3,
    [
        "Arctic",
        "Coastal",
        "Underwater",
        "Desert",
        "Forest",
        "Grasslands",
        "Hills",
        "Swamp",
    ],
    """This silver and grey silky moss can be
    found growing amongst almost any substance as it seems to
    ignore environmental standards. Assassins have been able to
    use this lichen to quickly administer their toxins into the target’s
    system without any drawbacks. However, this takes some
    preparation and is often forgotten by common folk.""",
    "QL",
)
radiant_synthseed = Ingredient(
    "Radiant Synthseed",
    "Rare",
    "Toxin Modifier",
    """Change poison damage to radiant damage; target is still
    [poisoned] for 1 minute on a failed CON saving throw; this toxin is still
    considered poison damage when combining with other ingredients.""",
    2,
    ["Underdark"],
    """This long black and boat shaped seed
    emanates a strong yellow glow, and often exerts the smell of
    flowers. When the seed is cracked open, a person can find a few
    smaller looking seeds of the same nature. These smaller seeds
    can often be crushed or blended into mixtures to enhance toxins.""",
    "RS",
)
rock_vine = Ingredient(
    "Rock Vine",
    "Rare",
    "Enchantment",
    "User creates a potion of invulnerability (DMG 188).",
    4,
    ["Hills", "Mountain"],
    """This extremely hardened dark green vine can be
    found growing in the ground near very old minerals, often seeming
    to feed off the minerals themselves. At first glance this vine seems
    completely useless to mortals, but arcane studies have shown
    this vine to harden a person’s skin significantly if combined with a
    powerful catalyst.""",
    "RV",
)
scillia_beans = Ingredient(
    "Scillia Beans",
    "Common",
    "Enchantment",
    "User creates a potion of climbing (DMG 187).",
    1,
    ["Desert", "Grasslands"],
    """These light brown beans can occasionally
    be found hanging from Scillia Bushes in dry atmosphere
    environments. They are often used to enhance flavors in stew and
    other meals, but have a much stranger effect. At full potency, some
    of these beans can offer the user the ability to climb steep cliffs
    and rock faces with ease.""",
    "SBea",
)
silver_hibiscus = Ingredient(
    "Silver Hibiscus",
    "Rare",
    "Enchantment",
    """When consumed by target, they can unleash a random
    elemental breathe weapon 3 times (PHB 34). Cannot be altered by other
    ingredients.""",
    4,
    ["Arctic", "Underdark"],
    """This silver-grey plant looks as though it
    represents madness itself. It often has random patterns and
    unplanned shapes, but always has a black web-like pattern on it.
    Although it may look deadly to touch, when prepared properly a
    Herbalist can unleash a torrent of elemental power representing a
    breath weapon.""",
    "SH"
)
spineflower_berries = Ingredient(
    "Spineflower Berries",
    "Uncommon",
    "Toxin Modifier",
    "Increase the dice-type by 1 size for any Toxin Effect",
    3,
    ["Desert", "Swamp"],
    """Often found hanging amongst the bone-
    like flowers, this white berry can be harvested and crushed to
    enhance toxins made by scoundrels. However, this effect only
    applies when introduced directly to the bloodstream. When
    ingested normally these berries provide little sustenance, but do
    not harm the person.""",
    "SBer"
)
tail_leaf = None
verdant_nettle = None
voidroot = None
wild_sageroot = None
wisp_stalks = None
wrackwort_bulbs = None
wyrmtongue_petals = None
