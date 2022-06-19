from BaseClasses import Item
from .Locations import kill_descriptor, regular_monster_names, boss_monster_names
import typing

class GhostloreItem(Item):
	game: str = "Ghostlore"

# 10,133,000 - 10,133,194
offset = 10_13_3_000

boss_offset = offset + len(regular_monster_names)

shop_offset = boss_offset + len(boss_monster_names)

monster_item_table = {
	f"{regular_monster_names[i]} Loot": offset + i for i in range(0, len(regular_monster_names))
}

boss_item_table = {
	f"{boss_monster_names[i]} Boss Loot": boss_offset + i for i in range(0, len(boss_monster_names))
}



#TODO: come up with cool items to put in the shop
shop_item_table = {
	"Recipe 1": shop_offset + 0,
	"Recipe 2": shop_offset + 1,
	"Recipe 3": shop_offset + 2,
	"Recipe 4": shop_offset + 3,
	"Recipe 5": shop_offset + 4,
	"Recipe 6": shop_offset + 5,
	"Recipe 7": shop_offset + 6,
	"Recipe 8": shop_offset + 7,
	"Recipe 9": shop_offset + 8,
	"Recipe 10": shop_offset + 9,
	"Recipe 11": shop_offset + 10,
	"Recipe 12": shop_offset + 11,
	"Recipe 13": shop_offset + 12,
	"Recipe 14": shop_offset + 13,
	"Recipe 15": shop_offset + 14,
	"Recipe 16": shop_offset + 15,
	"Recipe 17": shop_offset + 16,
	"Recipe 18": shop_offset + 17,
	"Recipe 19": shop_offset + 18,
	"Recipe 20": shop_offset + 19
}

quest_item_offset = shop_offset + len(shop_item_table)

quest_item_table = {
	"Chthonite": quest_item_offset + 0,
	"Astralite": quest_item_offset + 1
}

item_table = {
	**monster_item_table,
	**boss_item_table,
	**shop_item_table,
	**quest_item_table
}