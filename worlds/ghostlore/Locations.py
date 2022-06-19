from BaseClasses import Location


class GhostloreLocation(Location):
    game: str = "Ghostlore"


# 10,133,000 - 10,133,194
offset = 10_13_3_000


shop_size = 20

kill_descriptor = [
    'Kill',
    'Slay',
    'Wipe Out',
    'Destroy',
    'Slaughter',
    'Vanquish',
    'Execute',
    'Annihilate',
    'Obliterate',
    'Exterminate'
]

monster_prime_location = {
	'Ahool': 'RRRR',
    'Babi Ngepet': 'RRRR',
    'E-Gui': 'RRRR',
    'Gui-Kia': 'RRRR',
    'Hantu Raya': 'RRRR',
    'Hantu Tinggi': 'RRRR',
    'Jenglot': 'RRRR',
    'Jiang-Shi': 'RRRR',
    'Komodo Wizard': 'RRRR',
    'Salamancer': 'RRRR',
    'Orang Minyak': 'RRRR',
    'Penanggal': 'RRRR',
    'Pocong': 'RRRR',
    'Pontianak Tree': 'RRRR',
    'Preta': 'RRRR',
    'Rakshasa': 'RRRR',
    'Toyol': 'RRRR'
}

boss_prime_location = {
	'Mogui Summoner': 'RRRR',
    'Rafflesia': 'RRRR',
    'Ice Jinn': 'RRRR',
    'Thunder Jinn': 'RRRR',
    'Fire Jinn': 'RRRR',
	'Hantu Tinggi': 'RRRR'
}


regular_monster_names = []
boss_monster_names = []

for m in monster_prime_location.keys():
	regular_monster_names.append(m)

for b in boss_prime_location.keys():
	boss_monster_names.append(b)


def get_locations_for_monster(monster: str):
	quests = []
	for i in range(0, len(kill_descriptor)):
		quests.append(f"{kill_descriptor[i]} {monster}")
	return quests

def get_locations_for_region(region: str):
	quests = []
	for m in monster_prime_location.keys():
		if monster_prime_location[m] == region:
			quests.append(m)
	for b in boss_prime_location.keys():
		if boss_prime_location[b] == region:
			quests.append(b)
	if region == "Seaport":
		for s in link_bracelets.keys():
			quests.append(s)
	return quests


kill_quests = {}

for i in range(0, len(regular_monster_names)):
	quests = get_locations_for_monster(regular_monster_names[i])
	for j in range(0, len(quests)):
		kill_quests[quests[j]] = offset + i * len(kill_descriptor) + j




boss_offset = offset + (len(regular_monster_names)) * 10

boss_quests = {
    f"Defeat {boss_monster_names[i]}": boss_offset + i for i in range(0, len(boss_monster_names))
}

shop_offset = boss_offset + len(boss_monster_names)

# Item shop
link_bracelets = {
    f"Link Bracelet #{i + 1}": shop_offset + i for i in range(0, shop_size)
}

location_table = {
    **kill_quests,
    **boss_quests,
    **link_bracelets
}
