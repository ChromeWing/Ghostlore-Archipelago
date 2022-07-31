from functools import partial
import string
from BaseClasses import Entrance, ItemClassification, Region, RegionType, Tutorial


from BaseClasses import Item, Tutorial
from worlds.ghostlore.Regions import ghostlore_regions, ghostlore_connections
from .Items import item_table, GhostloreItem
from .Locations import get_locations_for_region, location_table, regular_monster_names, boss_monster_names, shop_size, chest_count, GhostloreLocation
from .Options import Goal, ghostlore_options
from .Rules import set_rules
from ..AutoWorld import World, WebWorld



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
	
	item_name_to_id = item_table
	location_name_to_id = location_table

	data_version = 0

	forced_auto_forfeit = False

	def generate_basic(self):
		kill_quests = self.world.kill_quests_per_monster[self.player].value
		itempool = []
		
		# Monster loot
		for monster in regular_monster_names:
			itempool += [f"{monster} Loot"] * kill_quests

		# Boss loot
		for boss in boss_monster_names:
			itempool += [f"{boss} Boss Loot"]



		self.item_name_groups["Loot"] = set(itempool[:])

		# Shop items
		for i in range(0,shop_size):
			itempool += [f"Recipe {i+1}"]

		# Quest items
		for i in ["Chthonite", "Astralite"]:
			itempool += [i]

		for i in range(0, chest_count):
			itempool += ["1000 Coins"]


		itempool = list(map(lambda name: self.create_item(name), itempool))

		print(itempool)
		self.world.itempool += itempool

		self.world.get_location("End of story", self.player).place_locked_item(self.create_goal_event("Victory"))
		self.world.get_location("Hell Gate 1", self.player).place_locked_item(self.create_goal_event("Hell Gate 1 cleared"))
		self.world.get_location("Hell Gate 3", self.player).place_locked_item(self.create_goal_event("Hell Gate 3 cleared"))
		self.world.get_location("Hell Gate 10", self.player).place_locked_item(self.create_goal_event("Hell Gate 10 cleared"))

		if self.goal == 0:
			self.world.completion_condition[self.player] = lambda state: state.has("Victory", self.player)
			pass
		elif self.goal == 1:
			self.world.completion_condition[self.player] = lambda state: state.has("Hell Gate 1 cleared", self.player)
		elif self.goal == 2:
			self.world.completion_condition[self.player] = lambda state: state.has("Hell Gate 3 cleared", self.player)
		elif self.goal == 3:
			self.world.completion_condition[self.player] = lambda state: state.has("Hell Gate 10 cleared", self.player)

		



	def set_rules(self):
		set_rules(self.world, self.player)

	def generate_early(self):
		self.goal = self.world.goal[self.player].value
		self.monster_workload = self.world.monster_workload[self.player].value
		self.kill_quests_per_monster = self.world.kill_quests_per_monster[self.player].value
		self.item_level_type = self.world.item_level_type[self.player].value
		self.base_item_shop_price = self.world.base_item_shop_price[self.player].value
		self.experience_rate = self.world.experience_rate[self.player].value
		self.death_link = self.world.death_link[self.player].value

	def create_regions(self):
		for(reg, exits) in ghostlore_regions:
			region = Region(reg, RegionType.Generic, f"Something first found from {reg}",self.player,self.world)
			for i in get_locations_for_region(reg,self.kill_quests_per_monster):
				region.locations += [GhostloreLocation(self.player, i, location_table[i], region)]
			for e in exits:
				region.exits += [Entrance(self.player, e, region)]
			self.world.regions.append(region)
		for(exit, requirements, dest) in ghostlore_connections:
			connection = self.world.get_entrance(exit, self.player)
			if requirements:
				connection.access_rule = partial((lambda req,state:req(self.player, state)), requirements)
			connection.connect(self.world.get_region(dest,self.player))
		print("done creating regions")
		

	def create_item(self, name: str) -> Item:
		item_id = item_table[name]
		item = GhostloreItem(name, ItemClassification.filler, item_id, self.player)
		if self._is_progression(name):
			item.classification = ItemClassification.progression
		return item

	def create_goal_event(self, name: str) -> Item:
		event = GhostloreItem(name, True, None, self.player)
		event.type = "Victory"
		return event
		
	def _is_progression(self, name: str):
		return "Loot" in name or name in ["Chthonite", "Astralite"]
	
	def fill_slot_data(self):
		return {
			"goal": self.world.goal[self.player].value,
			"monster_workload": self.world.monster_workload[self.player].value,
			"kill_quests_per_monster": self.world.kill_quests_per_monster[self.player].value,
			"item_level_type": self.world.item_level_type[self.player].value,
			"base_item_shop_price": self.world.base_item_shop_price[self.player].value,
			"experience_rate": self.world.experience_rate[self.player].value,
			"death_link": self.world.death_link[self.player].value
		}
		

