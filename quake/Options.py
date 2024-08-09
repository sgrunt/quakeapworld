from Options import PerGameCommonOptions, Choice, Toggle, DeathLink, DefaultOnToggle, StartInventoryPool
from dataclasses import dataclass


class Goal(Choice):
    """
    Choose the main goal.
    complete_all_levels: All levels of the selected episodes
    complete_end: Shub-Niggurath's Pit (END)
    """
    display_name = "Goal"
    option_complete_all_levels = 0
    option_complete_end = 1
    default = 0


class Skill(Choice):
    """
    Choose the skill option. Those match Quake's skill options.
    easy: less monsters or strength.
    medium: Default.
    hard: More monsters or strength.
    nightmare: Monsters attack more rapidly.
    """
    display_name = "Skill"
    option_easy = 0
    option_medium = 1
    option_hard = 2
    option_nightmare = 3
    default = 1


class RandomMonsters(Choice):
    """
    Choose how monsters are randomized.
    vanilla: No randomization
    shuffle: Monsters are shuffled within the level
    random_balanced: Monsters are completely randomized, but balanced based on existing ratio in the level. (Small monsters vs medium vs big)
    random_chaotic: Monsters are completely randomized, but balanced based on existing ratio in the entire game.    
    """
    display_name = "Random Monsters"
    option_vanilla = 0
    option_shuffle = 1
    option_random_balanced = 2
    option_random_chaotic = 3
    default = 1


class RandomPickups(Choice):
    """
    Choose how pickups are randomized.
    vanilla: No randomization
    shuffle: Pickups are shuffled within the level
    random_balanced: Pickups are completely randomized, but balanced based on existing ratio in the level. (Small pickups vs Big)
    """
    display_name = "Random Pickups"
    option_vanilla = 0
    option_shuffle = 1
    option_random_balanced = 2
    default = 1


class RandomMusic(Choice):
    """
    Level musics will be randomized.
    vanilla: No randomization
    shuffle_selected: Selected episodes' levels will be shuffled
    shuffle_game: All the music will be shuffled
    """
    display_name = "Random Music"
    option_vanilla = 0
    option_shuffle_selected = 1
    option_shuffle_game = 2
    default = 0


class ResetLevelOnDeath(DefaultOnToggle):
    """When dying, levels are reset and monsters respawned. But inventory and checks are kept.
    Turning this setting off is considered easy mode. Good for new players that don't know the levels well."""
    display_name="Reset Level on Death"


class Episode1(DefaultOnToggle):
    """Dimension of the Doomed.
    If none of the episodes are chosen, Episode 1 will be chosen by default."""
    display_name = "Episode 1"


class Episode2(DefaultOnToggle):
    """The Realm of Black Magic.
    If none of the episodes are chosen, Episode 1 will be chosen by default."""
    display_name = "Episode 2"


class Episode3(DefaultOnToggle):
    """The Netherworld.
    If none of the episodes are chosen, Episode 1 will be chosen by default."""
    display_name = "Episode 3"


class Episode4(DefaultOnToggle):
    """The Elder World.
    If none of the episodes are chosen, Episode 1 will be chosen by default."""
    display_name = "Episode 4"
    
    
class Episode5(DefaultOnToggle):
    """Shub-Niggurath's Pit.
    If none of the episodes are chosen, Episode 1 will be chosen by default.
    This level cannot be chosen by itself; if it is the only one enabled
    Episode 1 will also be enabled."""
    display_name = "Episode 5"


@dataclass
class QuakeOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    goal: Goal
    skill: Skill
    random_monsters: RandomMonsters
    random_pickups: RandomPickups
    random_music: RandomMusic
    death_link: DeathLink
    reset_level_on_death: ResetLevelOnDeath
    episode1: Episode1
    episode2: Episode2
    episode3: Episode3
    episode4: Episode4
    episode5: Episode5

