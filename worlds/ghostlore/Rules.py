from BaseClasses import MultiWorld
from ..AutoWorld import LogicMixin
from ..generic.Rules import set_rule

class GhostloreLogic(LogicMixin):
	def _ghostlore_shop_can_afford(self, player, price):
		approx_coin_received = 0
		for item in self.prog_items:
			if item[1] == player:
				if "Loot" in item[1]:
					approx_coin_received += 1
				elif "Riches" in item[1]:
					approx_coin_received += 5
		return approx_coin_received >= price

shop_costs = [
	5,
	5,
	5,
	15,
	5,
	5,
	5,
	5,
	5,
	5,
	5,
	5,
	5,
	5,
	5,
	5,
	5,
	5,
	5,
	5
]

def set_rules(world: MultiWorld, player):
	# Set shop rules
	for shop_index in range(0,20):
		set_rule(
			world.get_location(f"Shop {shop_index + 1}", player),
			lambda state: state._ghostlore_shop_can_afford(player, shop_costs[shop_index])
		)
