from ingredients import *


def get_common_ingredient():
    print("Getting common ingredient...")


def run():
    print("Rolling ingredients...")


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
}
