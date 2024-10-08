from BaseClasses import ItemClassification
from typing import TypedDict, Dict, Set 


class ItemDict(TypedDict, total=False): 
    classification: ItemClassification 
    count: int 
    name: str 
    classname: int
    spawnflags: int
    episode: int
    map: int 


item_table: Dict[int, ItemDict] = {
    730000: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Slipgate Complex (E1M1)',
             'classname': 'level',
             'spawnflags': 0,
             'episode': 1,
             'map': 1},
    730001: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Slipgate Complex (E1M1) - Complete',
             'classname': 'exit',
             'spawnflags': 0,
             'episode': 1,
             'map': 1},
    730002: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Castle of the Damned (E1M2)',
             'classname': 'level',
             'spawnflags': 0,
             'episode': 1,
             'map': 2},
    730003: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Castle of the Damned (E1M2) - Silver Key',
             'classname': 'item_key1',
             'spawnflags': 0,
             'episode': 1,
             'map': 2},
    730004: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Castle of the Damned (E1M2) - Complete',
             'classname': 'exit',
             'spawnflags': 0,
             'episode': 1,
             'map': 2},
    730005: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Necropolis (E1M3)',
             'classname': 'level',
             'spawnflags': 0,
             'episode': 1,
             'map': 3},
    730006: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Necropolis (E1M3) - Gold Key',
             'classname': 'item_key2',
             'spawnflags': 0,
             'episode': 1,
             'map': 3},
    730007: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Necropolis (E1M3) - Complete',
             'classname': 'exit',
             'spawnflags': 0,
             'episode': 1,
             'map': 3},
    730008: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Grisly Grotto (E1M4)',
             'classname': 'level',
             'spawnflags': 0,
             'episode': 1,
             'map': 4},
    730009: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Grisly Grotto (E1M4) - Silver Key',
             'classname': 'item_key1',
             'spawnflags': 0,
             'episode': 1,
             'map': 4},
    730010: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Grisly Grotto (E1M4) - Complete',
             'classname': 'exit',
             'spawnflags': 0,
             'episode': 1,
             'map': 4},
    730011: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Gloom Keep (E1M5)',
             'classname': 'level',
             'spawnflags': 0,
             'episode': 1,
             'map': 5},
    730012: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Gloom Keep (E1M5) - Silver Key',
             'classname': 'item_key1',
             'spawnflags': 0,
             'episode': 1,
             'map': 5},
    730013: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Gloom Keep (E1M5) - Gold Key',
             'classname': 'item_key2',
             'spawnflags': 0,
             'episode': 1,
             'map': 5},
    730014: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Gloom Keep (E1M5) - Complete',
             'classname': 'exit',
             'spawnflags': 0,
             'episode': 1,
             'map': 5},
    730015: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Door to Chthon (E1M6)',
             'classname': 'level',
             'spawnflags': 0,
             'episode': 1,
             'map': 6},
    730016: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Door to Chthon (E1M6) - Silver Runekey',
             'classname': 'item_key1',
             'spawnflags': 0,
             'episode': 1,
             'map': 6},
    730017: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Door to Chthon (E1M6) - Gold Runekey',
             'classname': 'item_key2',
             'spawnflags': 0,
             'episode': 1,
             'map': 6},
    730018: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Door to Chthon (E1M6) - Complete',
             'classname': 'exit',
             'spawnflags': 0,
             'episode': 1,
             'map': 6},
    730019: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The House of Chthon (E1M7)',
             'classname': 'level',
             'spawnflags': 0,
             'episode': 1,
             'map': 7},
    730020: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The House of Chthon (E1M7) - Complete',
             'classname': 'exit',
             'spawnflags': 0,
             'episode': 1,
             'map': 7},
    730021: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Ziggurat Vertigo (E1M8)',
             'classname': 'level',
             'spawnflags': 0,
             'episode': 1,
             'map': 8},
    730022: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Ziggurat Vertigo (E1M8) - Silver Runekey',
             'classname': 'item_key1',
             'spawnflags': 0,
             'episode': 1,
             'map': 8},
    730023: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Ziggurat Vertigo (E1M8) - Complete',
             'classname': 'exit',
             'spawnflags': 0,
             'episode': 1,
             'map': 8},
    730024: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Installation (E2M1)',
             'classname': 'level',
             'spawnflags': 0,
             'episode': 2,
             'map': 1},
    730025: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Installation (E2M1) - Silver Keycard',
             'classname': 'item_key1',
             'spawnflags': 0,
             'episode': 2,
             'map': 1},
    730026: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Installation (E2M1) - Gold Keycard',
             'classname': 'item_key2',
             'spawnflags': 0,
             'episode': 2,
             'map': 1},
    730027: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Installation (E2M1) - Complete',
             'classname': 'exit',
             'spawnflags': 0,
             'episode': 2,
             'map': 1},
    730028: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Ogre Citadel (E2M2)',
             'classname': 'level',
             'spawnflags': 0,
             'episode': 2,
             'map': 2},
    730029: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Ogre Citadel (E2M2) - Gold Key',
             'classname': 'item_key2',
             'spawnflags': 0,
             'episode': 2,
             'map': 2},
    730030: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Ogre Citadel (E2M2) - Complete',
             'classname': 'exit',
             'spawnflags': 0,
             'episode': 2,
             'map': 2},
    730031: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Crypt of Decay (E2M3)',
             'classname': 'level',
             'spawnflags': 0,
             'episode': 2,
             'map': 3},
    730032: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Crypt of Decay (E2M3) - Gold Key',
             'classname': 'item_key2',
             'spawnflags': 0,
             'episode': 2,
             'map': 3},
    730033: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Crypt of Decay (E2M3) - Complete',
             'classname': 'exit',
             'spawnflags': 0,
             'episode': 2,
             'map': 3},
    730034: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Ebon Fortress (E2M4)',
             'classname': 'level',
             'spawnflags': 0,
             'episode': 2,
             'map': 4},
    730035: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Ebon Fortress (E2M4) - Silver Key',
             'classname': 'item_key1',
             'spawnflags': 0,
             'episode': 2,
             'map': 4},
    730036: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Ebon Fortress (E2M4) - Gold Key',
             'classname': 'item_key2',
             'spawnflags': 0,
             'episode': 2,
             'map': 4},
    730037: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Ebon Fortress (E2M4) - Complete',
             'classname': 'exit',
             'spawnflags': 0,
             'episode': 2,
             'map': 4},
    730038: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Wizard\'s Manse (E2M5)',
             'classname': 'level',
             'spawnflags': 0,
             'episode': 2,
             'map': 5},
    730039: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Wizard\'s Manse (E2M5) - Gold Key',
             'classname': 'item_key2',
             'spawnflags': 0,
             'episode': 2,
             'map': 5},
    730040: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Wizard\'s Manse (E2M5) - Complete',
             'classname': 'exit',
             'spawnflags': 0,
             'episode': 2,
             'map': 5},
    730041: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Dismal Oubliette (E2M6)',
             'classname': 'level',
             'spawnflags': 0,
             'episode': 2,
             'map': 6},
    730042: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Dismal Oubliette (E2M6) - Gold Key',
             'classname': 'item_key2',
             'spawnflags': 0,
             'episode': 2,
             'map': 6},
    730043: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Dismal Oubliette (E2M6) - Complete',
             'classname': 'exit',
             'spawnflags': 0,
             'episode': 2,
             'map': 6},
    730044: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Underearth (E2M7)',
             'classname': 'level',
             'spawnflags': 0,
             'episode': 2,
             'map': 7},
    730045: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Underearth (E2M7) - Gold Key',
             'classname': 'item_key2',
             'spawnflags': 0,
             'episode': 2,
             'map': 7},
    730046: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Underearth (E2M7) - Complete',
             'classname': 'exit',
             'spawnflags': 0,
             'episode': 2,
             'map': 7},
    730047: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Termination Central (E3M1)',
             'classname': 'level',
             'spawnflags': 0,
             'episode': 3,
             'map': 1},
    730048: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Termination Central (E3M1) - Gold Keycard',
             'classname': 'item_key2',
             'spawnflags': 0,
             'episode': 3,
             'map': 1},
    730049: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Termination Central (E3M1) - Complete',
             'classname': 'exit',
             'spawnflags': 0,
             'episode': 3,
             'map': 1},
    730050: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Vaults of Zin (E3M2)',
             'classname': 'level',
             'spawnflags': 0,
             'episode': 3,
             'map': 2},
    730051: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Vaults of Zin (E3M2) - Gold Runekey',
             'classname': 'item_key2',
             'spawnflags': 0,
             'episode': 3,
             'map': 2},
    730052: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Vaults of Zin (E3M2) - Silver Runekey',
             'classname': 'item_key1',
             'spawnflags': 0,
             'episode': 3,
             'map': 2},
    730053: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Vaults of Zin (E3M2) - Complete',
             'classname': 'exit',
             'spawnflags': 0,
             'episode': 3,
             'map': 2},
    730054: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Tomb of Terror (E3M3)',
             'classname': 'level',
             'spawnflags': 0,
             'episode': 3,
             'map': 3},
    730055: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Tomb of Terror (E3M3) - Silver Runekey',
             'classname': 'item_key1',
             'spawnflags': 0,
             'episode': 3,
             'map': 3},
    730056: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Tomb of Terror (E3M3) - Complete',
             'classname': 'exit',
             'spawnflags': 0,
             'episode': 3,
             'map': 3},
    730057: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Satan\'s Dark Delight (E3M4)',
             'classname': 'level',
             'spawnflags': 0,
             'episode': 3,
             'map': 4},
    730058: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Satan\'s Dark Delight (E3M4) - Complete',
             'classname': 'exit',
             'spawnflags': 0,
             'episode': 3,
             'map': 4},
    730059: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Wind Tunnels (E3M5)',
             'classname': 'level',
             'spawnflags': 0,
             'episode': 3,
             'map': 5},
    730060: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Wind Tunnels (E3M5) - Complete',
             'classname': 'exit',
             'spawnflags': 0,
             'episode': 3,
             'map': 5},
    730061: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Chambers of Torment (E3M6)',
             'classname': 'level',
             'spawnflags': 0,
             'episode': 3,
             'map': 6},
    730062: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Chambers of Torment (E3M6) - Silver Runekey',
             'classname': 'item_key1',
             'spawnflags': 0,
             'episode': 3,
             'map': 6},
    730063: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Chambers of Torment (E3M6) - Gold Runekey',
             'classname': 'item_key2',
             'spawnflags': 0,
             'episode': 3,
             'map': 6},
    730064: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Chambers of Torment (E3M6) - Complete',
             'classname': 'exit',
             'spawnflags': 0,
             'episode': 3,
             'map': 6},
    730065: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Haunted Halls (E3M7)',
             'classname': 'level',
             'spawnflags': 0,
             'episode': 3,
             'map': 7},
    730066: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Haunted Halls (E3M7) - Complete',
             'classname': 'exit',
             'spawnflags': 0,
             'episode': 3,
             'map': 7},
    730067: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Sewage System (E4M1)',
             'classname': 'level',
             'spawnflags': 0,
             'episode': 4,
             'map': 1},
    730068: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Sewage System (E4M1) - Gold Keycard',
             'classname': 'item_key2',
             'spawnflags': 0,
             'episode': 4,
             'map': 1},
    730069: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Sewage System (E4M1) - Complete',
             'classname': 'exit',
             'spawnflags': 0,
             'episode': 4,
             'map': 1},
    730070: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Tower of Despair (E4M2)',
             'classname': 'level',
             'spawnflags': 0,
             'episode': 4,
             'map': 2},
    730071: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Tower of Despair (E4M2) - Silver Key',
             'classname': 'item_key1',
             'spawnflags': 0,
             'episode': 4,
             'map': 2},
    730072: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Tower of Despair (E4M2) - Complete',
             'classname': 'exit',
             'spawnflags': 0,
             'episode': 4,
             'map': 2},
    730073: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Elder God Shrine (E4M3)',
             'classname': 'level',
             'spawnflags': 0,
             'episode': 4,
             'map': 3},
    730074: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Elder God Shrine (E4M3) - Silver Key',
             'classname': 'item_key1',
             'spawnflags': 0,
             'episode': 4,
             'map': 3},
    730075: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Elder God Shrine (E4M3) - Gold Key',
             'classname': 'item_key2',
             'spawnflags': 0,
             'episode': 4,
             'map': 3},
    730076: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Elder God Shrine (E4M3) - Complete',
             'classname': 'exit',
             'spawnflags': 0,
             'episode': 4,
             'map': 3},
    730077: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Palace of Hate (E4M4)',
             'classname': 'level',
             'spawnflags': 0,
             'episode': 4,
             'map': 4},
    730078: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Palace of Hate (E4M4) - Silver Key',
             'classname': 'item_key1',
             'spawnflags': 0,
             'episode': 4,
             'map': 4},
    730079: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Palace of Hate (E4M4) - Complete',
             'classname': 'exit',
             'spawnflags': 0,
             'episode': 4,
             'map': 4},
    730080: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Hell\'s Atrium (E4M5)',
             'classname': 'level',
             'spawnflags': 0,
             'episode': 4,
             'map': 5},
    730081: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Hell\'s Atrium (E4M5) - Silver Key',
             'classname': 'item_key1',
             'spawnflags': 0,
             'episode': 4,
             'map': 5},
    730082: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Hell\'s Atrium (E4M5) - Gold Key',
             'classname': 'item_key2',
             'spawnflags': 0,
             'episode': 4,
             'map': 5},
    730083: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Hell\'s Atrium (E4M5) - Complete',
             'classname': 'exit',
             'spawnflags': 0,
             'episode': 4,
             'map': 5},
    730084: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Pain Maze (E4M6)',
             'classname': 'level',
             'spawnflags': 0,
             'episode': 4,
             'map': 6},
    730085: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Pain Maze (E4M6) - Silver Key',
             'classname': 'item_key1',
             'spawnflags': 0,
             'episode': 4,
             'map': 6},
    730086: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Pain Maze (E4M6) - Gold Key',
             'classname': 'item_key2',
             'spawnflags': 0,
             'episode': 4,
             'map': 6},
    730087: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Pain Maze (E4M6) - Complete',
             'classname': 'exit',
             'spawnflags': 0,
             'episode': 4,
             'map': 6},
    730088: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Azure Agony (E4M7)',
             'classname': 'level',
             'spawnflags': 0,
             'episode': 4,
             'map': 7},
    730089: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Azure Agony (E4M7) - Silver Key',
             'classname': 'item_key1',
             'spawnflags': 0,
             'episode': 4,
             'map': 7},
    730090: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Azure Agony (E4M7) - Complete',
             'classname': 'exit',
             'spawnflags': 0,
             'episode': 4,
             'map': 7},
    730091: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Nameless City (E4M8)',
             'classname': 'level',
             'spawnflags': 0,
             'episode': 4,
             'map': 8},
    730092: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Nameless City (E4M8) - Silver Key',
             'classname': 'item_key1',
             'spawnflags': 0,
             'episode': 4,
             'map': 8},
    730093: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Nameless City (E4M8) - Gold Key',
             'classname': 'item_key2',
             'spawnflags': 0,
             'episode': 4,
             'map': 8},
    730094: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Nameless City (E4M8) - Complete',
             'classname': 'exit',
             'spawnflags': 0,
             'episode': 4,
             'map': 8},
    730095: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Rune of Earth Magic',
             'classname': 'item_sigil',
             'spawnflags': 1,
             'episode': 5,
             'map': 1},
    730096: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Rune of Black Magic',
             'classname': 'item_sigil',
             'spawnflags': 2,
             'episode': 5,
             'map': 1},
    730097: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Rune of Hell Magic',
             'classname': 'item_sigil',
             'spawnflags': 4,
             'episode': 5,
             'map': 1},
    730098: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Rune of Elder Magic',
             'classname': 'item_sigil',
             'spawnflags': 8,
             'episode': 5,
             'map': 1},
    730099: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Shub-Niggurath\'s Pit (END) - Complete',
             'classname': 'exit',
             'spawnflags': 0,
             'episode': 5,
             'map': 1},
    730100: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Double-Barreled Shotgun',
             'classname': 'weapon_supershotgun',
             'spawnflags': 0,
             'episode': -1,
             'map': -1},
    730101: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Nailgun',
             'classname': 'weapon_nailgun',
             'spawnflags': 0,
             'episode': -1,
             'map': -1},
    730102: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Super Nailgun',
             'classname': 'weapon_supernailgun',
             'spawnflags': 0,
             'episode': -1,
             'map': -1},
    730103: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Grenade Launcher',
             'classname': 'weapon_grenadelauncher',
             'spawnflags': 0,
             'episode': -1,
             'map': -1},
    730104: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Rocket Launcher',
             'classname': 'weapon_rocketlauncher',
             'spawnflags': 0,
             'episode': -1,
             'map': -1},
    730105: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Thunderbolt',
             'classname': 'weapon_lightning',
             'spawnflags': 0,
             'episode': -1,
             'map': -1},
    730106: {'classification': ItemClassification.filler,
             'count': 0,
             'name': 'Green Armor',
             'classname': 'item_armor1',
             'spawnflags': 0,
             'episode': -1,
             'map': -1},
    730107: {'classification': ItemClassification.filler,
             'count': 0,
             'name': 'Yellow Armor',
             'classname': 'item_armor2',
             'spawnflags': 0,
             'episode': -1,
             'map': -1},
    730108: {'classification': ItemClassification.filler,
             'count': 0,
             'name': 'Red Armor',
             'classname': 'item_armorInv',
             'spawnflags': 0,
             'episode': -1,
             'map': -1},
    730109: {'classification': ItemClassification.filler,
             'count': 0,
             'name': 'Megahealth',
             'classname': 'item_health',
             'spawnflags': 2,
             'episode': -1,
             'map': -1},
    730110: {'classification': ItemClassification.filler,
             'count': 0,
             'name': 'Ring of Shadows',
             'classname': 'item_artifact_invisibility',
             'spawnflags': 0,
             'episode': -1,
             'map': -1},
    730111: {'classification': ItemClassification.filler,
             'count': 0,
             'name': 'Pentagram of Protection',
             'classname': 'item_artifact_invulnerability',
             'spawnflags': 0,
             'episode': -1,
             'map': -1},
    730112: {'classification': ItemClassification.filler,
             'count': 0,
             'name': 'Quad Damage',
             'classname': 'item_artifact_super_damage',
             'spawnflags': 0,
             'episode': -1,
             'map': -1},
    730113: {'classification': ItemClassification.filler,
             'count': 0,
             'name': '25 Health',
             'classname': 'item_health',
             'spawnflags': 0,
             'episode': -1,
             'map': -1},
    730114: {'classification': ItemClassification.filler,
             'count': 0,
             'name': 'Large Box of Shells',
             'classname': 'item_shells',
             'spawnflags': 1,
             'episode': -1,
             'map': -1},
    730115: {'classification': ItemClassification.filler,
             'count': 0,
             'name': 'Large Box of Nails',
             'classname': 'item_spikes',
             'spawnflags': 1,
             'episode': -1,
             'map': -1},
    730116: {'classification': ItemClassification.filler,
             'count': 0,
             'name': 'Large Box of Rockets',
             'classname': 'item_rockets',
             'spawnflags': 1,
             'episode': -1,
             'map': -1},
    730117: {'classification': ItemClassification.filler,
             'count': 0,
             'name': 'Large Box of Cells',
             'classname': 'item_cells',
             'spawnflags': 1,
             'episode': -1,
             'map': -1},
}


item_name_groups: Dict[str, Set[str]] = {
    'Ammos': {'Large Box of Shells', 'Large Box of Nails', 'Large Box of Rockets', 'Large Box of Cells'},
    'Keys': {'Castle of the Damned (E1M2) - Silver Key', 'The Necropolis (E1M3) - Gold Key', 'The Grisly Grotto (E1M4) - Silver Key', 'Gloom Keep (E1M5) - Gold Key', 'Gloom Keep (E1M5) - Silver Key', 'The Door to Chthon (E1M6) - Gold Runekey', 'The Door to Chthon (E1M6) - Silver Runekey', 'Ziggurat Vertigo (E1M8) - Silver Runekey', 'The Installation (E2M1) - Gold Keycard', 'The Installation (E2M1) - Silver Keycard', 'The Installation (E2M1) - Silver Keycard 2', 'The Ogre Citadel (E2M2) - Gold Key', 'The Crypt of Decay (E2M3) - Gold Key', 'The Ebon Fortress (E2M4) - Silver Key', 'The Ebon Fortress (E2M4) - Gold Key', 'The Wizard\'s Manse (E2M5) - Gold Key', 'The Dismal Oubliette (E2M6) - Gold Key', 'The Underearth (E2M7) - Gold Key', 'Termination Central (E3M1) - Gold Keycard', 'The Vaults of Zin (E3M2) - Silver Runekey', 'The Vaults of Zin (E3M2) - Gold Runekey', 'The Tomb of Terror (E3M3) - Silver Runekey', 'Chambers of Torment (E3M6) - Silver Runekey', 'Chambers of Torment (E3M6) - Gold Runekey', 'The Sewage System (E4M1) - Gold Keycard', 'The Tower of Despair (E4M2) - Silver Key', 'The Tower of Despair (E4M2) - Silver Key 2', 'The Elder God Shrine (E4M3) - Silver Key', 'The Elder God Shrine (E4M3) - Gold Key', 'The Palace of Hate (E4M4) - Silver Key', 'Hell\'s Atrium (E4M5) - Silver Key', 'Hell\'s Atrium (E4M5) - Gold Key', 'The Pain Maze (E4M6) - Gold Key', 'The Pain Maze (E4M6) - Silver Key', 'Azure Agony (E4M7) - Silver Key', 'The Nameless City (E4M8) - Gold Key', 'The Nameless City (E4M8) - Silver Key', 'Rune of Earth Magic', 'Rune of Black Magic', 'Rune of Hell Magic', 'Rune of Hell Magic'},
    'Levels': {'The Slipgate Complex (E1M1)', 'Castle of the Damned (E1M2)', 'The Necropolis (E1M3)', 'The Grisly Grotto (E1M4)', 'Gloom Keep (E1M5)', 'The Door to Chthon (E1M6)', 'The House of Chthon (E1M7)', 'Ziggurat Vertigo (E1M8)', 'The Installation (E2M1)', 'The Ogre Citadel (E2M2)', 'The Crypt of Decay (E2M3)', 'The Ebon Fortress (E2M4)', 'The Wizard\'s Manse (E2M5)', 'The Dismal Oubliette (E2M6)', 'The Underearth (E2M7)', 'Termination Central (E3M1)', 'The Vaults of Zin (E3M2)', 'The Tomb of Terror (E3M3)', 'Satan\'s Dark Delight (E3M4)', 'The Wind Tunnels (E3M5)', 'Chambers of Torment (E3M6)', 'The Haunted Halls (E3M7)', 'The Sewage System (E4M1', 'The Tower of Despair (E4M2)', 'The Elder God Shrine (E4M3)', 'The Palace of Hate (E4M4)', 'Hell\'s Atrium (E4M5)', 'The Pain Maze (E4M6)', 'Azure Agony (E4M7)', 'The Nameless City (E4M8)'},
    'Powerups': {'Green Armor', 'Yellow Armor', 'Red Armor', 'Megahealth', 'Ring of Shadows', 'Pentagram of Protection', 'Quad Damage'},
    'Weapons': {'Double-Barreled Shotgun', 'Nailgun', 'Super Nailgun', 'Grenade Launcher', 'Rocket Launcher', 'Thunderbolt'},
}
