from random import randrange

from ingredients import *

common = {
    2: mandrake_root,
    3: quicksilver_lichen,
    4: quicksilver_lichen,
    5: wild_sageroot,
    6: wild_sageroot,
    7: bloodgrass,
    8: wyrmtongue_petals,
    9: wyrmtongue_petals,
    10: milkweed_seeds,
    11: milkweed_seeds,
    12: mandrake_root,
}


def get_common_ingredient():
    '''Rolls for a common ingredient and returns the corresponding ingredient from common'''
    common_ingredient_roll = randrange(1, 7) + randrange(1, 7)
    return common[common_ingredient_roll]


roll_tables = {
    "arctic": {
        2: silver_hibiscus,
        3: mortflesh_powder,
        4: ironwood_heart,
        5: frozen_seedlings,
        6: get_common_ingredient(),
        7: get_common_ingredient(),
        8: get_common_ingredient(),
        9: arctic_creeper,
        10: fennel_silk,
        11: fiends_ivy,
        12: voidroot,
    },
    "coastal": {
        2: hydrathistle,
        3: amanita_cap,
        4: hyancinth_nectar,
        5: chromus_slime,
        6: get_common_ingredient(),
        7: get_common_ingredient(),
        8: get_common_ingredient(),
        9: lavender_sprig,
        10: blue_toadshade,
        11: wrackwort_bulbs,
        12: cosmos_glond,
    },
    "underwater": {
        2: hydrathistle,
        4: hyancinth_nectar,
        5: chromus_slime,
        6: get_common_ingredient(),
        7: get_common_ingredient(),
        8: get_common_ingredient(),
        11: wrackwort_bulbs,
        12: cosmos_glond,
    },
    "desert": {
        2: cosmos_glond,
        3: arrow_root,
        4: dried_ephedra,
        5: cactus_juice,
        6: get_common_ingredient(),
        7: get_common_ingredient(),
        8: get_common_ingredient(),
        9: drakus_flower,
        10: scillia_beans,
        11: spineflower_berries,
        12: voidroot,
    },
    "forest": {
        2: harrada_leaf,
        3: nightshade_berries,
        4: emetic_wax,
        5: verdant_nettle,
        6: get_common_ingredient(),
        7: get_common_ingredient(),
        8: get_common_ingredient(),
        9: arrow_root,
        10: ironwood_heart,
        11: blue_toadshade,
        12: wisp_stalks,
    },
    "grasslands": {
        2: harrada_leaf,
        3: drakus_flower,
        4: lavender_sprig,
        5: arrow_root,
        6: get_common_ingredient(),
        7: get_common_ingredient(),
        8: get_common_ingredient(),
        9: scillia_beans,
        10: cactus_juice,
        11: tail_leaf,
        12: hyancinth_nectar,
    },
    "hills": {
        2: devils_bloodleaf,
        3: nightshade_berries,
        4: tail_leaf,
        5: lavender_sprig,
        6: get_common_ingredient(),
        7: get_common_ingredient(),
        8: get_common_ingredient(),
        9: ironwood_heart,
        10: gengko_brush,
        11: rock_vine,
        12: harrada_leaf,
    },
    "mountain": {
        2: basilisks_breath,
        3: frozen_seedlings,
        4: arctic_creeper,
        5: dried_ephedra,
        6: get_common_ingredient(),
        7: get_common_ingredient(),
        8: get_common_ingredient(),
        9: drakus_flower,
        10: luminous_cap_dust,
        11: rock_vine,
        12: primordial_balm,
    },
    "swamp": {
        2: devils_bloodleaf,
        3: spineflower_berries,
        4: emetic_wax,
        5: amanita_cap,
        6: get_common_ingredient(),
        7: get_common_ingredient(),
        8: get_common_ingredient(),
        9: blue_toadshade,
        10: wrackwort_bulbs,
        11: hydrathistle,
        12: primordial_balm,
    },
    "underdark": {
        2: primordial_balm,
        3: silver_hibiscus,
        4: devils_bloodleaf,
        5: chromus_slime,
        6: mortflesh_powder,
        7: fennel_silk,
        8: fiends_ivy,
        9: gengko_brush,
        10: luminous_cap_dust,
        11: radiant_synthseed,
        12: wisp_stalks,
    },
}


def run(given_region):
    print("Rolling ingredients...")
    number_of_ingredients = randrange(1, 5)
    found_ingredients = []

    for num in range(0, number_of_ingredients):
        ingredient_roll = randrange(1, 7) + randrange(1, 7)
        while ingredient_roll not in roll_tables[given_region].keys():
            ingredient_roll = randrange(1, 7) + randrange(1, 7)
        if 2 <= ingredient_roll <= 4 or 10 <= ingredient_roll <= 12:
            if randrange(1, 101) >= 75:
                found_ingredients.append(elemental_water)
            else:
                found_ingredients.append(roll_tables[given_region][ingredient_roll])
        else:    
            found_ingredients.append(roll_tables[given_region][ingredient_roll])

    return found_ingredients
