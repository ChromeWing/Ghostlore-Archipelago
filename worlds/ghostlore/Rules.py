from BaseClasses import MultiWorld
from ..AutoWorld import LogicMixin
from ..generic.Rules import set_rule

class GhostloreLogic(LogicMixin):
	def _ghostlore_shop_can_afford(self, player, price):
		return (self.count_group("Loot", player) + self.count("1000 Coins", player) * 2) >= price

shop_costs = [
	5,
	6,
	4,
	20,
	7,
	6.5,
	5.5,
	1,
	8,
	4.4,
	3.5,
	5.6,
	13,
	8.8,
	7.7,
	4.1,
	6.2,
	9.3,
	10,
	3
]

def set_rules(world: MultiWorld, player):
	# Set shop rules
	for shop_index in range(0,20):
		set_rule(
			world.get_location(f"Link Bracelet #{shop_index + 1}", player),
			lambda state: state._ghostlore_shop_can_afford(player, shop_costs[shop_index])
		)
