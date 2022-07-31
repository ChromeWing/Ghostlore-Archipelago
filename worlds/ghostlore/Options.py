import typing
from Options import DeathLink, Option, DefaultOnToggle, Range, Choice


class Goal(Choice):
	"""Which goal must be achieved to trigger completion."""
	display_name = "Goal"
	option_complete_story = 0
	option_clear_hell_gate_1 = 1
	option_clear_hell_gate_3 = 2
	option_clear_hell_gate_10 = 3
	alias_hell_1 = 1
	alias_hell_3 = 2
	alias_hell_10 = 3
	default = 0

class MonsterWorkload(Choice):
	"""Which relative amount of monsters you need to defeat to complete a location check."""
	display_name = "Monster Workload"
	option_quick_playthrough = 0
	option_single_playthrough = 1
	option_some_grinding = 2
	option_grinding_required = 3
	default = 1

class KillQuestsPerMonster(Range):
	"""How many quests to kill monsters there are per non-boss type monster.  Multiplies with Monster Workload for longer/shorter runs."""
	display_name = "Kill Quests Per Monster"
	range_start = 3
	range_end = 10
	default = 5

class ItemLevelType(Choice):
	"""Whether the item level of loot dropped from receiving your items is determined by current character level, or by current check progression (recommended for async multiworlds)"""
	display_name = "Item Level Type"
	option_tied_to_character_level = 0
	option_tied_to_check_progression = 1
	default = 0

class BaseItemShopPrice(Range):
	"""The base item shop price (with a random multiplier applied) to determine the prices of all Link Bracelets in the Archipelago item shop."""
	display_name = "Base Item Shop Price"
	range_start = 0
	range_end = 3000
	default = 500

class ExperienceRate(Range):
	"""The percentage multiplier for the game's experience points gained by the player."""
	display_name = "Experience Rate % Multiplier"
	range_start = 100
	range_end = 300
	default = 100

ghostlore_options: typing.Dict[str, type(Option)] = {
	"goal": Goal,
	"monster_workload": MonsterWorkload,
	"kill_quests_per_monster": KillQuestsPerMonster,
	"item_level_type": ItemLevelType,
	"base_item_shop_price": BaseItemShopPrice,
	"experience_rate": ExperienceRate,
	"death_link": DeathLink
}
