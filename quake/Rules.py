from typing import TYPE_CHECKING
from worlds.generic.Rules import set_rule

if TYPE_CHECKING:
    from . import QuakeWorld


def set_episode1_rules(player, multiworld):
    set_rule(multiworld.get_entrance("Hub -> The Slipgate Complex (E1M1) Main", player), lambda state:
        state.has("The Slipgate Complex (E1M1)", player, 1))

    set_rule(multiworld.get_entrance("Hub -> Castle of the Damned (E1M2) Main", player), lambda state:
        state.has("Castle of the Damned (E1M2)", player, 1) and
        state.has("Double-Barreled Shotgun", player, 1))

    set_rule(multiworld.get_entrance("Castle of the Damned (E1M2) Main -> Castle of the Damned (E1M2) Silver", player), lambda state:
        state.has("Castle of the Damned (E1M2) - Silver Key", player, 1))

    set_rule(multiworld.get_entrance("Hub -> The Necropolis (E1M3) Main", player), lambda state:
        state.has("The Necropolis (E1M3)", player, 1) and
        state.has("Double-Barreled Shotgun", player, 1) and
        (state.has("Nailgun", player, 1) or
         state.has("Super Nailgun", player, 1)) and
        (state.has("Grenade Launcher", player, 1) or
         state.has("Rocket Launcher", player, 1)))

    set_rule(multiworld.get_entrance("The Necropolis (E1M3) Main -> The Necropolis (E1M3) Gold", player), lambda state:
        state.has("The Necropolis (E1M3) - Gold Key", player, 1))

    set_rule(multiworld.get_entrance("Hub -> The Grisly Grotto (E1M4) Main", player), lambda state:
        state.has("The Grisly Grotto (E1M4)", player, 1) and
        state.has("Double-Barreled Shotgun", player, 1) and
        state.has("Nailgun", player, 1) and
        state.has("Super Nailgun", player, 1) and
        (state.has("Grenade Launcher", player, 1) or
         state.has("Rocket Launcher", player, 1)))

    set_rule(multiworld.get_entrance("The Grisly Grotto (E1M4) Main -> The Grisly Grotto (E1M4) Silver", player), lambda state:
        state.has("The Grisly Grotto (E1M4) - Silver Key", player, 1))

    set_rule(multiworld.get_entrance("Hub -> Gloom Keep (E1M5) Main", player), lambda state:
        state.has("Gloom Keep (E1M5)", player, 1) and
        state.has("Double-Barreled Shotgun", player, 1) and
        state.has("Nailgun", player, 1) and
        state.has("Super Nailgun", player, 1) and
        state.has("Grenade Launcher", player, 1) and
        state.has("Rocket Launcher", player, 1))

    set_rule(multiworld.get_entrance("Gloom Keep (E1M5) Main -> Gloom Keep (E1M5) Silver", player), lambda state:
        state.has("Gloom Keep (E1M5) - Silver Key", player, 1))

    set_rule(multiworld.get_entrance("Gloom Keep (E1M5) Silver -> Gloom Keep (E1M5) Gold", player), lambda state:
        state.has("Gloom Keep (E1M5) - Gold Key", player, 1))

    set_rule(multiworld.get_entrance("Hub -> The Door to Chthon (E1M6) Main", player), lambda state:
        state.has("The Door to Chthon (E1M6)", player, 1) and
        state.has("Double-Barreled Shotgun", player, 1) and
        state.has("Nailgun", player, 1) and
        state.has("Super Nailgun", player, 1) and
        state.has("Grenade Launcher", player, 1) and
        state.has("Rocket Launcher", player, 1))

    set_rule(multiworld.get_entrance("The Door to Chthon (E1M6) Main -> The Door to Chthon (E1M6) Silver", player), lambda state:
        state.has("The Door to Chthon (E1M6) - Silver Runekey", player, 1))

    set_rule(multiworld.get_entrance("The Door to Chthon (E1M6) Main -> The Door to Chthon (E1M6) Gold", player), lambda state:
        state.has("The Door to Chthon (E1M6) - Gold Runekey", player, 1))

    set_rule(multiworld.get_entrance("Hub -> The House of Chthon (E1M7) Main", player), lambda state:
        state.has("The House of Chthon (E1M7)", player, 1))

    set_rule(multiworld.get_entrance("Hub -> Ziggurat Vertigo (E1M8) Main", player), lambda state:
        state.has("Ziggurat Vertigo (E1M8)", player, 1) and
        state.has("Double-Barreled Shotgun", player, 1) and
        state.has("Nailgun", player, 1) and
        state.has("Super Nailgun", player, 1) and
        state.has("Grenade Launcher", player, 1) and
        state.has("Rocket Launcher", player, 1))

    set_rule(multiworld.get_entrance("Ziggurat Vertigo (E1M8) Main -> Ziggurat Vertigo (E1M8) Silver", player), lambda state:
        state.has("Ziggurat Vertigo (E1M8) - Silver Runekey", player, 1))

def set_episode2_rules(player, multiworld):
    set_rule(multiworld.get_entrance("Hub -> The Installation (E2M1) Main", player), lambda state:
        state.has("The Installation (E2M1)", player, 1))

    set_rule(multiworld.get_entrance("The Installation (E2M1) Gold -> The Installation (E2M1) Silver", player), lambda state:
        state.has("The Installation (E2M1) - Silver Keycard", player, 1))

    set_rule(multiworld.get_entrance("The Installation (E2M1) Main -> The Installation (E2M1) Gold", player), lambda state:
        state.has("The Installation (E2M1) - Gold Keycard", player, 1))

    set_rule(multiworld.get_entrance("Hub -> The Ogre Citadel (E2M2) Main", player), lambda state:
        state.has("The Ogre Citadel (E2M2)", player, 1) and
        state.has("Double-Barreled Shotgun", player, 1) and
        (state.has("Nailgun", player, 1) or
         state.has("Super Nailgun", player, 1)) and
        (state.has("Grenade Launcher", player, 1) or
         state.has("Rocket Launcher", player, 1)))

    set_rule(multiworld.get_entrance("The Ogre Citadel (E2M2) Main -> The Ogre Citadel (E2M2) Gold", player), lambda state:
        state.has("The Ogre Citadel (E2M2) - Gold Key", player, 1))

    set_rule(multiworld.get_entrance("Hub -> The Crypt of Decay (E2M3) Main", player), lambda state:
        state.has("The Crypt of Decay (E2M3)", player, 1) and
        state.has("Double-Barreled Shotgun", player, 1) and
        state.has("Nailgun", player, 1) and
        state.has("Super Nailgun", player, 1) and
        (state.has("Grenade Launcher", player, 1) or
         state.has("Rocket Launcher", player, 1)))

    set_rule(multiworld.get_entrance("The Crypt of Decay (E2M3) Main -> The Crypt of Decay (E2M3) Gold", player), lambda state:
        state.has("The Crypt of Decay (E2M3) - Gold Key", player, 1))

    set_rule(multiworld.get_entrance("Hub -> The Ebon Fortress (E2M4) Main", player), lambda state:
        state.has("The Ebon Fortress (E2M4)", player, 1) and
        state.has("Double-Barreled Shotgun", player, 1) and
        state.has("Nailgun", player, 1) and
        state.has("Super Nailgun", player, 1) and
        state.has("Grenade Launcher", player, 1) and
        state.has("Rocket Launcher", player, 1))

    set_rule(multiworld.get_entrance("The Ebon Fortress (E2M4) Main -> The Ebon Fortress (E2M4) Silver", player), lambda state:
        state.has("The Ebon Fortress (E2M4) - Silver Key", player, 1))

    set_rule(multiworld.get_entrance("The Ebon Fortress (E2M4) Main -> The Ebon Fortress (E2M4) Gold", player), lambda state:
        state.has("The Ebon Fortress (E2M4) - Gold Key", player, 1))

    set_rule(multiworld.get_entrance("Hub -> The Wizard's Manse (E2M5) Main", player), lambda state:
        state.has("The Wizard's Manse (E2M5)", player, 1) and
        state.has("Double-Barreled Shotgun", player, 1) and
        state.has("Nailgun", player, 1) and
        state.has("Super Nailgun", player, 1) and
        state.has("Grenade Launcher", player, 1) and
        state.has("Rocket Launcher", player, 1) and
        state.has("Thunderbolt", player, 1))

    set_rule(multiworld.get_entrance("The Wizard's Manse (E2M5) Main -> The Wizard's Manse (E2M5) Gold", player), lambda state:
        state.has("The Wizard's Manse (E2M5) - Gold Key", player, 1))

    set_rule(multiworld.get_entrance("Hub -> The Dismal Oubliette (E2M6) Main", player), lambda state:
        state.has("The Dismal Oubliette (E2M6)", player, 1) and
        state.has("Double-Barreled Shotgun", player, 1) and
        state.has("Nailgun", player, 1) and
        state.has("Super Nailgun", player, 1) and
        state.has("Grenade Launcher", player, 1) and
        state.has("Rocket Launcher", player, 1) and
        state.has("Thunderbolt", player, 1))

    set_rule(multiworld.get_entrance("The Dismal Oubliette (E2M6) Main -> The Dismal Oubliette (E2M6) Gold", player), lambda state:
        state.has("The Dismal Oubliette (E2M6) - Gold Key", player, 1))

    set_rule(multiworld.get_entrance("Hub -> The Underearth (E2M7) Main", player), lambda state:
        state.has("The Underearth (E2M7)", player, 1) and
        state.has("Double-Barreled Shotgun", player, 1) and
        state.has("Nailgun", player, 1) and
        state.has("Super Nailgun", player, 1) and
        (state.has("Grenade Launcher", player, 1) or
         state.has("Rocket Launcher", player, 1)))

    set_rule(multiworld.get_entrance("The Underearth (E2M7) Main -> The Underearth (E2M7) Gold", player), lambda state:
        state.has("The Underearth (E2M7) - Gold Key", player, 1))

def set_episode3_rules(player, multiworld):
    set_rule(multiworld.get_entrance("Hub -> Termination Central (E3M1) Main", player), lambda state:
        state.has("Termination Central (E3M1)", player, 1))

    set_rule(multiworld.get_entrance("Termination Central (E3M1) Main -> Termination Central (E3M1) Gold", player), lambda state:
        state.has("Termination Central (E3M1) - Gold Keycard", player, 1))

    set_rule(multiworld.get_entrance("Hub -> The Vaults of Zin (E3M2) Main", player), lambda state:
        state.has("The Vaults of Zin (E3M2)", player, 1) and
        state.has("Double-Barreled Shotgun", player, 1) and
        (state.has("Nailgun", player, 1) or
         state.has("Super Nailgun", player, 1)) and
        (state.has("Grenade Launcher", player, 1) or
         state.has("Rocket Launcher", player, 1)))

    set_rule(multiworld.get_entrance("The Vaults of Zin (E3M2) Main -> The Vaults of Zin (E3M2) Silver", player), lambda state:
        state.has("The Vaults of Zin (E3M2) - Silver Runekey", player, 1))

    set_rule(multiworld.get_entrance("The Vaults of Zin (E3M2) Silver -> The Vaults of Zin (E3M2) Gold", player), lambda state:
        state.has("The Vaults of Zin (E3M2) - Gold Runekey", player, 1))

    set_rule(multiworld.get_entrance("Hub -> The Tomb of Terror (E3M3) Main", player), lambda state:
        state.has("The Tomb of Terror (E3M3)", player, 1) and
        state.has("Double-Barreled Shotgun", player, 1) and
        state.has("Nailgun", player, 1) and
        state.has("Super Nailgun", player, 1) and
        (state.has("Grenade Launcher", player, 1) or
         state.has("Rocket Launcher", player, 1)))

    set_rule(multiworld.get_entrance("The Tomb of Terror (E3M3) Main -> The Tomb of Terror (E3M3) Silver", player), lambda state:
        state.has("The Tomb of Terror (E3M3) - Silver Runekey", player, 1))

    set_rule(multiworld.get_entrance("Hub -> Satan's Dark Delight (E3M4) Main", player), lambda state:
        state.has("Satan's Dark Delight (E3M4)", player, 1) and
        state.has("Double-Barreled Shotgun", player, 1) and
        state.has("Nailgun", player, 1) and
        state.has("Super Nailgun", player, 1) and
        state.has("Grenade Launcher", player, 1) and
        state.has("Rocket Launcher", player, 1) and
        state.has("Thunderbolt", player, 1))

    set_rule(multiworld.get_entrance("Hub -> The Wind Tunnels (E3M5) Main", player), lambda state:
        state.has("The Wind Tunnels (E3M5)", player, 1) and
        state.has("Double-Barreled Shotgun", player, 1) and
        state.has("Nailgun", player, 1) and
        state.has("Super Nailgun", player, 1) and
        state.has("Grenade Launcher", player, 1) and
        state.has("Rocket Launcher", player, 1) and
        state.has("Thunderbolt", player, 1))

    set_rule(multiworld.get_entrance("Hub -> Chambers of Torment (E3M6) Main", player), lambda state:
        state.has("Chambers of Torment (E3M6)", player, 1) and
        state.has("Double-Barreled Shotgun", player, 1) and
        state.has("Nailgun", player, 1) and
        state.has("Super Nailgun", player, 1) and
        state.has("Grenade Launcher", player, 1) and
        state.has("Rocket Launcher", player, 1) and
        state.has("Thunderbolt", player, 1))

    set_rule(multiworld.get_entrance("Chambers of Torment (E3M6) Main -> Chambers of Torment (E3M6) Silver", player), lambda state:
        state.has("Chambers of Torment (E3M6) - Silver Runekey", player, 1))

    set_rule(multiworld.get_entrance("Chambers of Torment (E3M6) Silver -> Chambers of Torment (E3M6) Gold", player), lambda state:
        state.has("Chambers of Torment (E3M6) - Gold Runekey", player, 1))

    set_rule(multiworld.get_entrance("Hub -> The Haunted Halls (E3M7) Main", player), lambda state:
        state.has("The Haunted Halls (E3M7)", player, 1) and
        state.has("Double-Barreled Shotgun", player, 1) and
        state.has("Nailgun", player, 1) and
        state.has("Super Nailgun", player, 1) and
        state.has("Grenade Launcher", player, 1) and
        state.has("Rocket Launcher", player, 1) and
        state.has("Thunderbolt", player, 1))

def set_episode4_rules(player, multiworld):
    set_rule(multiworld.get_entrance("Hub -> The Sewage System (E4M1) Main", player), lambda state:
        state.has("The Sewage System (E4M1)", player, 1))

    set_rule(multiworld.get_entrance("The Sewage System (E4M1) Main -> The Sewage System (E4M1) Gold", player), lambda state:
        state.has("The Sewage System (E4M1) - Gold Keycard", player, 1))

    set_rule(multiworld.get_entrance("Hub -> The Tower of Despair (E4M2) Main", player), lambda state:
        state.has("The Tower of Despair (E4M2)", player, 1) and
        state.has("Double-Barreled Shotgun", player, 1) and
        (state.has("Nailgun", player, 1) or
         state.has("Super Nailgun", player, 1)))

    set_rule(multiworld.get_entrance("The Tower of Despair (E4M2) Main -> The Tower of Despair (E4M2) Silver", player), lambda state:
        state.has("The Tower of Despair (E4M2) - Silver Key", player, 1))

    set_rule(multiworld.get_entrance("Hub -> The Elder God Shrine (E4M3) Main", player), lambda state:
        state.has("The Elder God Shrine (E4M3)", player, 1) and
        state.has("Double-Barreled Shotgun", player, 1) and
        (state.has("Nailgun", player, 1) or
         state.has("Super Nailgun", player, 1)) and
        (state.has("Grenade Launcher", player, 1) or
         state.has("Rocket Launcher", player, 1)))

    set_rule(multiworld.get_entrance("The Elder God Shrine (E4M3) Main -> The Elder God Shrine (E4M3) Silver", player), lambda state:
        state.has("The Elder God Shrine (E4M3) - Silver Key", player, 1))

    set_rule(multiworld.get_entrance("The Elder God Shrine (E4M3) Main -> The Elder God Shrine (E4M3) Gold", player), lambda state:
        state.has("The Elder God Shrine (E4M3) - Gold Key", player, 1))

    set_rule(multiworld.get_entrance("Hub -> The Palace of Hate (E4M4) Main", player), lambda state:
        state.has("The Palace of Hate (E4M4)", player, 1) and
        state.has("Double-Barreled Shotgun", player, 1) and
        state.has("Nailgun", player, 1) and
        state.has("Super Nailgun", player, 1) and
        (state.has("Grenade Launcher", player, 1) or
         state.has("Rocket Launcher", player, 1)))

    set_rule(multiworld.get_entrance("The Palace of Hate (E4M4) Main -> The Palace of Hate (E4M4) Silver", player), lambda state:
        state.has("The Palace of Hate (E4M4) - Silver Key", player, 1))

    set_rule(multiworld.get_entrance("Hub -> Hell's Atrium (E4M5) Main", player), lambda state:
        state.has("Hell's Atrium (E4M5)", player, 1) and
        state.has("Double-Barreled Shotgun", player, 1) and
        state.has("Nailgun", player, 1) and
        state.has("Super Nailgun", player, 1) and
        (state.has("Grenade Launcher", player, 1) or
         state.has("Rocket Launcher", player, 1)) and
        state.has("Thunderbolt", player, 1))

    set_rule(multiworld.get_entrance("Hell's Atrium (E4M5) Main -> Hell's Atrium (E4M5) Silver", player), lambda state:
        state.has("Hell's Atrium (E4M5) - Silver Key", player, 1))

    set_rule(multiworld.get_entrance("Hell's Atrium (E4M5) Main -> Hell's Atrium (E4M5) Gold", player), lambda state:
        state.has("Hell's Atrium (E4M5) - Gold Key", player, 1))

    set_rule(multiworld.get_entrance("Hub -> The Pain Maze (E4M6) Main", player), lambda state:
        state.has("The Pain Maze (E4M6)", player, 1) and
        state.has("Double-Barreled Shotgun", player, 1) and
        state.has("Nailgun", player, 1) and
        state.has("Super Nailgun", player, 1) and
        state.has("Grenade Launcher", player, 1) and
        state.has("Rocket Launcher", player, 1) and
        state.has("Thunderbolt", player, 1))

    set_rule(multiworld.get_entrance("The Pain Maze (E4M6) Gold -> The Pain Maze (E4M6) Silver", player), lambda state:
        state.has("The Pain Maze (E4M6) - Silver Key", player, 1))

    set_rule(multiworld.get_entrance("The Pain Maze (E4M6) Main -> The Pain Maze (E4M6) Gold", player), lambda state:
        state.has("The Pain Maze (E4M6) - Gold Key", player, 1))

    set_rule(multiworld.get_entrance("Hub -> Azure Agony (E4M7) Main", player), lambda state:
        state.has("Azure Agony (E4M7)", player, 1) and
        state.has("Double-Barreled Shotgun", player, 1) and
        state.has("Nailgun", player, 1) and
        state.has("Super Nailgun", player, 1) and
        state.has("Grenade Launcher", player, 1) and
        state.has("Rocket Launcher", player, 1) and
        state.has("Thunderbolt", player, 1))

    set_rule(multiworld.get_entrance("Azure Agony (E4M7) Main -> Azure Agony (E4M7) Silver", player), lambda state:
        state.has("Azure Agony (E4M7) - Silver Key", player, 1))

    set_rule(multiworld.get_entrance("Hub -> The Nameless City (E4M8) Main", player), lambda state:
        state.has("The Nameless City (E4M8)", player, 1) and
        state.has("Double-Barreled Shotgun", player, 1) and
        state.has("Nailgun", player, 1) and
        state.has("Super Nailgun", player, 1) and
        (state.has("Grenade Launcher", player, 1) or
         state.has("Rocket Launcher", player, 1)) and
        state.has("Thunderbolt", player, 1))

    set_rule(multiworld.get_entrance("The Nameless City (E4M8) Main -> The Nameless City (E4M8) Silver", player), lambda state:
        state.has("The Nameless City (E4M8) - Silver Key", player, 1))

    set_rule(multiworld.get_entrance("The Nameless City (E4M8) Main -> The Nameless City (E4M8) Gold", player), lambda state:
        state.has("The Nameless City (E4M8) - Gold Key", player, 1))

def set_episode5_rules(player, multiworld):
    set_rule(multiworld.get_entrance("Hub -> Shub-Niggurath's Pit (END) Main", player), lambda state:
        state.has("Rune of Earth Magic", player, 1) and
        state.has("Rune of Black Magic", player, 1) and
        state.has("Rune of Hell Magic", player, 1) and
        state.has("Rune of Elder Magic", player, 1) and
        state.has("Double-Barreled Shotgun", player, 1) and
        state.has("Nailgun", player, 1) and
        state.has("Super Nailgun", player, 1) and
        state.has("Grenade Launcher", player, 1) and
        state.has("Rocket Launcher", player, 1) and
        state.has("Thunderbolt", player, 1))


def set_rules(quake_world: "QuakeWorld", included_episodes):
    player = quake_world.player
    multiworld = quake_world.multiworld

    if included_episodes[0]:
        set_episode1_rules(player, multiworld)
    if included_episodes[1]:
        set_episode2_rules(player, multiworld)
    if included_episodes[2]:
        set_episode3_rules(player, multiworld)
    if included_episodes[3]:
        set_episode4_rules(player, multiworld)
    if included_episodes[4]:
        set_episode5_rules(player, multiworld)
