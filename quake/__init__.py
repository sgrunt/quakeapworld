import functools
import logging
from typing import Any, Dict, List

from BaseClasses import Entrance, CollectionState, Item, Location, MultiWorld, Region, Tutorial
from worlds.AutoWorld import WebWorld, World
from . import Items, Locations, Maps, Regions, Rules
from .Options import QuakeOptions

logger = logging.getLogger("Quake")

class QuakeLocation(Location):
    game: str = "Quake"


class QuakeItem(Item):
    game: str = "Quake"


class QuakeWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Quake randomizer connected to an Archipelago Multiworld",
        "English",
        "setup_en.md",
        "setup/en",
        ["sgrunt"]
    )]
    theme = "dirt"


class QuakeWorld(World):
    """
    Quake from 1996.
    """
    options_dataclass = QuakeOptions
    options: QuakeOptions
    game = "Quake"
    web = QuakeWeb()
    required_client_version = (0, 5, 0)

    item_name_to_id = {data["name"]: item_id for item_id, data in Items.item_table.items()}
    item_name_groups = Items.item_name_groups

    location_name_to_id = {data["name"]: loc_id for loc_id, data in Locations.location_table.items()}
    location_name_groups = Locations.location_name_groups

    starting_level_for_episode: List[str] = [
        "The Slipgate Complex (E1M1)",
        "The Installation (E2M1)",
        "Termination Central (E3M1)",
        "The Sewage System (E4M1)"
    ]

    boss_level_for_episodes: List[str] = [
        "Shub-Niggurath's Pit (END)",
    ]

    items_ratio: Dict[str, float] = {
        "Quad Damage": 61,
        "Megahealth": 48,
        "Yellow Armor": 42,
        "Green Armor": 38,
        "Ring of Shadows": 23,
        "Pentagram of Protection": 23,
        "Red Armor": 22,
        "25 Health": 15,
        "Large Box of Shells": 13,
        "Large Box of Nails": 13,
        "Large Box of Rockets": 13,
        "Large Box of Cells": 10
    }

    item_ratio_total: float = sum(items_ratio.values())

    def __init__(self, multiworld: MultiWorld, player: int):
        self.included_episodes = [1, 1, 1, 1, 1]
        self.location_count = 0

        super().__init__(multiworld, player)

    def get_episode_count(self):
        return functools.reduce(lambda count, episode: count + episode, self.included_episodes)

    def generate_early(self):
        # Cache which episodes are included
        self.included_episodes[0] = self.options.episode1.value
        self.included_episodes[1] = self.options.episode2.value
        self.included_episodes[2] = self.options.episode3.value
        self.included_episodes[3] = self.options.episode4.value
        self.included_episodes[4] = self.options.episode5.value

        # If no episodes selected or only END selected, select Episode 1
        if (self.get_episode_count() == 0) or (self.get_episode_count() == 1 and self.included_episodes[4]):
            self.included_episodes[0] = 1

    def create_regions(self):
        # Main regions
        menu_region = Region("Menu", self.player, self.multiworld)
        hub_region = Region("Hub", self.player, self.multiworld)
        self.multiworld.regions += [menu_region, hub_region]
        menu_region.add_exits(["Hub"])

        # Create regions and locations
        main_regions = []
        connections = []
        for region_dict in Regions.regions:
            if not self.included_episodes[region_dict["episode"] - 1]:
                continue

            region_name = region_dict["name"]
            if region_dict["connects_to_hub"]:
                main_regions.append(region_name)

            region = Region(region_name, self.player, self.multiworld)
            region.add_locations({
                loc["name"]: loc_id
                for loc_id, loc in Locations.location_table.items()
                if loc["region"] == region_name and self.included_episodes[loc["episode"] - 1]
            }, QuakeLocation)

            self.multiworld.regions.append(region)

            for connection_dict in region_dict["connections"]:
                connections.append((region, connection_dict["target"]))
        
        # Connect main regions to Hub
        hub_region.add_exits(main_regions)

        # Do the other connections between regions (They are not all both ways)
        for connection in connections:
            source = connection[0]
            target = self.multiworld.get_region(connection[1], self.player)

            entrance = Entrance(self.player, f"{source.name} -> {target.name}", source)
            source.exits.append(entrance)
            entrance.connect(target)

        # Sum locations for items creation
        self.location_count = len(self.multiworld.get_locations(self.player))

    def completion_rule(self, state: CollectionState):
        goal_levels = Maps.map_names
        if self.options.goal.value:
            goal_levels = self.boss_level_for_episodes

        for map_name in goal_levels:
            if map_name + " - Exit" not in self.location_name_to_id:
                continue
            
            # Exit location names are in form: Hangar (E1M1) - Exit
            loc = Locations.location_table[self.location_name_to_id[map_name + " - Exit"]]
            if not self.included_episodes[loc["episode"] - 1]:
                continue

            # Map complete item names are in form: Hangar (E1M1) - Complete
            if not state.has(map_name + " - Complete", self.player, 1):
                return False
            
        return True

    def set_rules(self):
        Rules.set_rules(self, self.included_episodes)
        self.multiworld.completion_condition[self.player] = lambda state: self.completion_rule(state)

    def create_item(self, name: str) -> QuakeItem:
        item_id: int = self.item_name_to_id[name]
        return QuakeItem(name, Items.item_table[item_id]["classification"], item_id, self.player)

    def create_items(self):
        itempool: List[QuakeItem] = []

        # Items
        for item_id, item in Items.item_table.items():
            if item["classname"] == "exit":
                continue # We'll fill it manually later

            if item["episode"] != -1 and not self.included_episodes[item["episode"] - 1]:
                continue

            count = item["count"] if item["name"] not in self.starting_level_for_episode else item["count"] - 1
            itempool += [self.create_item(item["name"]) for _ in range(count)]

        # Place end level items in locked locations
        for map_name in Maps.map_names:
            loc_name = map_name + " - Exit"
            item_name = map_name + " - Complete"

            if loc_name not in self.location_name_to_id:
                continue

            if item_name not in self.item_name_to_id:
                continue

            loc = Locations.location_table[self.location_name_to_id[loc_name]]
            if not self.included_episodes[loc["episode"] - 1]:
                continue

            self.multiworld.get_location(loc_name, self.player).place_locked_item(self.create_item(item_name))
            self.location_count -= 1

        # Give starting levels right away
        for i in range(len(self.included_episodes)):
            if self.included_episodes[i] and i != 4: # END is locked by runes
                self.multiworld.push_precollected(self.create_item(self.starting_level_for_episode[i]))

        # Fill the rest starting with powerups, then fillers
        locs_to_fill = self.location_count - len(itempool)
        self.create_ratioed_items("Quad Damage", itempool, locs_to_fill)
        self.create_ratioed_items("Megahealth", itempool, locs_to_fill)
        self.create_ratioed_items("Yellow Armor", itempool, locs_to_fill)
        self.create_ratioed_items("Green Armor", itempool, locs_to_fill)
        self.create_ratioed_items("Ring of Shadows", itempool, locs_to_fill)
        self.create_ratioed_items("Pentagram of Protection", itempool, locs_to_fill)
        self.create_ratioed_items("Red Armor", itempool, locs_to_fill)

        while len(itempool) < self.location_count:
            itempool.append(self.create_item(self.get_filler_item_name()))

        # add itempool to multiworld
        self.multiworld.itempool += itempool

    def get_filler_item_name(self):
        return self.multiworld.random.choice([
            "25 Health",
            "Large Box of Shells",
            "Large Box of Nails",
            "Large Box of Rockets",
            "Large Box of Cells"
        ])

    def create_ratioed_items(self, item_name: str, itempool: List[QuakeItem], ratioed_pool_size: float):
        remaining_loc = self.location_count - len(itempool)

        count = min(remaining_loc, max(1, int(round(self.items_ratio[item_name] * ratioed_pool_size / self.item_ratio_total))))
        if count == 0:
            logger.warning("Warning, no ", item_name, " will be placed.")
            return

        for i in range(count):
            itempool.append(self.create_item(item_name))

    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data = self.options.as_dict("goal", "skill", "random_monsters", "random_pickups", "random_music", "death_link", "reset_level_on_death", "episode1", "episode2", "episode3", "episode4", "episode5")

        return slot_data
