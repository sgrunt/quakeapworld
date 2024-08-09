# Quake Randomizer Setup

## Required Software

- [Quake (e.g. Steam version)](https://store.steampowered.com/app/2280/Quake_1993/)
- APQuake (release TBD)

## Optional Software

- [ArchipelagoTextClient](https://github.com/ArchipelagoMW/Archipelago/releases)
- [Archipelago Universal Tracker](https://github.com/FarisTheAncient/Archipelago/releases)

## Installing APQuake
1. Download APQuake and extract it.
2. Copy `ID1/PAK0.PAK` and `ID1/PAK1.PAK` from your game's installation directory into an `ID1` directory of the new folder.
   You can find the folder in Steam by finding the game in your library,
   right-clicking it and choosing **Manage -> Browse Local Files**.

## Joining a MultiWorld Game

`apquake.exe` needs to be run from the command line. Pass it an `-apserver` argument with your Archipelago server URL and port and an `-applayer` argument with your player name. You should be connected and 

To continue a game, follow the same connection steps.
Connecting with a different seed won't erase your progress in other seeds.

## Archipelago Universal Tracker

We recommend having the Archipelago Universal Tracker open on the side to keep track of what items you receive and send and what locations are available to you.
While APQuake will print Archipelago messages briefly and those will remain on the console afterwards, these don't persist across game restarts.

### Hinting

To hint from in-game, use the chat (Default key: 'T'). Hinting from Quake can be difficult because names are rather long and contain special characters. For example:
```
!hint The Necropolis (E1M3) - Gold key
```
The game has a hint helper implemented, where you can simply type this:
```
!hint e1m3 gold
```
For this to work, include the map short name (`E1M1`), followed by one of the keywords: `gold`, `silver`.

## Auto-Tracking

APQuake has a functional map tracker integrated into the level select screen.
It tells you which levels you have unlocked, which keys you have for each level, which levels have been completed,
and how many of the checks you have completed in each level.

