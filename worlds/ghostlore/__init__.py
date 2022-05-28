import string
from BaseClasses import Tutorial

from worlds.AutoWorld import WebWorld, World



client_version = 1

class GhostloreWeb(WebWorld):
	tutorials = [Tutorial(
		"Ghostlore Setup Tutorial",
		"A guide to setting up Ghostlore for connecting to Archipelago multiworld games.",
		"English",
		"setup_en.md",
		"setup/en",
		["ChromeWing"]
	)]

class GhostloreWorld(World):
	"""
	 Explore an 'Eastpunk' land in this beautiful Southeast-Asian folklore themed Action RPG.  Inspired by classic ARPG's like Diablo 2 and Titan Quest, Ghostlore features a deep character customization system with a multi-classing system, food crafting system, and a glyph system for powering up to take down tough foes.
	"""

	game: str = "Ghostlore"
	options = ghostlore_options
	