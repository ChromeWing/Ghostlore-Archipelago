from BaseClasses import Location


class GhostloreLocation(Location):
    game: str = "Ghostlore"


# 10,133,000 - 10,133,194
offset = 10_13_3_000


shop_size = 20

chest_count = 50

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
	'Ahool': 'Kenchanaraya Ruins',
    'Babi Ngepet': 'Pulau Hijawan',
    'E-Gui': 'Starting Zone',
    'Gui-Kia': 'Starting Zone',
    'Jenglot': 'Pulau Hijawan',
    'Jiang-Shi': 'Starting Zone',
    'Komodo Wizard': 'Kenchanaraya Ruins',
	'Monitor Wizard': 'Pulau Pasir Puaka',
    'Orang Minyak': 'Pulau Pasir Puaka',
    'Penanggal': 'Pulau Bakau',
    'Pocong': 'Pulau Hijawan',
    'Pontianak Tree': 'Pulau Kubor',
    'Preta': 'Kenchanaraya Ruins',
    'Rakshasa': 'Kenchanaraya Ruins',
    'Salamancer': 'Pulau Bakau',
    'Toyol': 'Pulau Pasir Puaka',
	'Stone Guardian': 'Kenchanaraya Ruins',
	'Ectoplasm': 'Abandoned Old Hospital',
	'Burning Ectoplasm': 'Abandoned Old Hospital',
	'Chilling Ectoplasm': 'Abandoned Old Hospital',
	'Shocking Ectoplasm': 'Abandoned Old Hospital',
	'Toxic Ectoplasm': 'Abandoned Old Hospital',
	'Frigid Spirit Orb': 'Abandoned Old Hospital',
	'Tempestous Spirit Orb': 'Abandoned Old Hospital',
	'Vile Spirit Orb': 'Abandoned Old Hospital',
	'Infernal Spirit Orb': 'Abandoned Old Hospital',
	'Nu-Gui': 'Abandoned Old Hospital',
	'Aphotic Lurker': 'Seaport Underground',
	'Croc Lord': 'Seaport Underground'

}

#TODO: re-add Hantu Tinggi once they get fixed in the game.
boss_prime_location = {
	'Mogui Summoner': 'Starting Zone',
    'Rafflesia': 'Pulau Hijawan',
	'Hantu Raya': 'Pulau Kubor',
	'Ice Jinn': 'Pulau Pasir Puaka',
	'Thunder Jinn': 'Pulau Pasir Puaka',
	'Fire Jinn': 'Pulau Pasir Puaka',
	'Hantu Tinggi': 'Pulau Bakau'
}

chest_region_split = { #add up to chest_count
	'Pulau Hijawan': [0,5],
	'Pulau Kubor': [5,10],
	'Kenchanaraya Ruins': [10,25],
	'Pulau Pasir Puaka': [25,31],
	'Pulau Bakau': [31,38],
	'Abandoned Old Hospital': [38,40],
	'Batu Sinaran': [40,50]
}


regular_monster_names = []
boss_monster_names = []

for m in monster_prime_location.keys():
	regular_monster_names.append(m)

for b in boss_prime_location.keys():
	boss_monster_names.append(b)


def get_locations_for_monster(monster: str, kill_quest_count):
	quests = []
	for i in range(0, min(len(kill_descriptor), kill_quest_count)):
		quests.append(f"{kill_descriptor[i]} {monster}")
	return quests

def get_locations_for_boss(boss: str):
	quests = []
	quests.append(f"Defeat {boss}")
	return quests

def get_locations_for_region(region: str, kill_quest_count):
	quests = []
	if region in chest_region_split:
		for c in range(chest_region_split[region][0],chest_region_split[region][1]):
			quests.append(f"Treasure Chest #{c + 1}")
	for m in monster_prime_location.keys():
		if monster_prime_location[m] == region:
			quests += get_locations_for_monster(m, kill_quest_count)
	for b in boss_prime_location.keys():
		if boss_prime_location[b] == region:
			quests += get_locations_for_boss(b)
	if region == "Seaport":
		for s in link_bracelets.keys():
			quests.append(s)
	if region == "Kenchanaraya Ruins":
		quests.append("Chthonite Chest")
	if region == "Batu Sinaran":
		quests.append("Astralite Chest")
	if region == "Endgame":
		for v in goal_locations:
			quests.append(v)
	return quests


kill_quests = {}

for i in range(0, len(regular_monster_names)):
	quests = get_locations_for_monster(regular_monster_names[i], len(kill_descriptor))
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

chest_offset = shop_offset + len(link_bracelets)

chest_locations = {
	f"Treasure Chest #{i + 1}": chest_offset + i for i in range(0, chest_count)
}

itemquest_offset = chest_offset + chest_count

itemquest_locations = {
	"Chthonite Chest": itemquest_offset + 0,
	"Astralite Chest": itemquest_offset + 1
}


goal_locations = {
	"End of story": None,
	"Hell Gate 1": None,
	"Hell Gate 3": None,
	"Hell Gate 10": None
}

location_table = {
    **kill_quests,
    **boss_quests,
    **link_bracelets,
	**chest_locations,
	**itemquest_locations,
	**goal_locations
}

print(location_table)
