import string
from BaseClasses import Tutorial


from BaseClasses import Item, MultiWorld, Tutorial
from .Items import item_table, GhostloreItem
from .Locations import location_table, regular_monster_names, boss_monster_names, shop_size, GhostloreLocation
from .Options import ghostlore_options
from .Rules import set_rules
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
	topology_present: False
	
	web = GhostloreWeb()
	
	options = ghostlore_options
	
	item_name_to_id: item_table
	location_name_to_id: location_table

	forced_auto_forfeit: False

	def generate_basic(self):
		regular_monster_count = len(regular_monster_names)
		boss_monster_count = len(boss_monster_names)
		kill_quests = self.world.kill_quests_per_monster[self.player].value
		itempool = []
		
		# Monster loot
		for monster in regular_monster_names:
			itempool += [f"{monster} Loot"] * kill_quests

		# Boss loot
		for boss in boss_monster_names:
			itempool += [f"{boss} Boss Loot"]

		# Shop items
		for i in range(0,shop_size):
			itempool += [f"Shop {i+1}"]

		itempool = list(map(lambda name: self.create_item(name), itempool))
		self.world.itempool += itempool

	def set_rules(self):
		set_rules(self.world, self.player)

	def create_regions(self):
		# TODO: create the regions of the world
		pass
	
	def fill_slot_data(self):
		return {
			"goal": self.goal,
			"monster_workload": self.monster_workload,
			"kill_quests_per_monster": self.kill_quests_per_monster,
			"item_level_type": self.item_level_type,
			"base_item_shop_price": self.base_item_shop_price,
			"death_link": self.death_link
		}
		

