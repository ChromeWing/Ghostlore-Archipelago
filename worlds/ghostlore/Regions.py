
from BaseClasses import Region, RegionType
from worlds.ghostlore.Locations import GhostloreLocation, get_locations_for_region


ghostlore_regions = [
	('Menu', ['New Adventure']),
	('Starting Zone', ['Rescued Master Ghosthunter']),
	('Seaport', ['Sail to Pulau Hijawan']),
	('Pulau Hijawan', ['Kill Rafflesia']),
	('Pulau Kubor', ['Kill Hantu Raya']),
	('Kenchanaraya Ruins', ['Collect Chthonite']),
	('Pulau Pasir Puaka', ['Kill all Jinns']),
	('Pulau Bakau', ['Kill Hantu Tinggi']),
	('Abandoned Old Hospital', ['Rescue little girl']),
	('Batu Sinaran', ['Collect Astralite']),
	('Seaport Underground', ['Clear Enemy Waves']),
	('The Spirit World', ['Defeat Zenith']),
	('Endgame',[]),
]

ghostlore_connections = [
	('New Adventure', None, 'Starting Zone'),
	('Rescued Master Ghosthunter', lambda player,state:state.has_group("Loot",player,2), 'Seaport'),
	('Sail to Pulau Hijawan', None,'Pulau Hijawan'),
	('Kill Rafflesia', lambda player,state:state.has_group("Loot",player,5), 'Pulau Kubor'),
	('Kill Hantu Raya', lambda player,state:state.has_group("Loot",player,8), 'Kenchanaraya Ruins'),
	('Collect Chthonite', lambda player,state:state.has_group("Loot",player,13) and state.has("Chthonite", player), 'Pulau Pasir Puaka'),
	('Kill all Jinns', lambda player,state:state.has_group("Loot",player,17), 'Pulau Bakau'),
	('Kill Hantu Tinggi', lambda player,state:state.has_group("Loot",player,21), 'Abandoned Old Hospital'),
	('Rescue little girl', lambda player,state:state.has_group("Loot",player,28), 'Batu Sinaran'),
	('Collect Astralite', lambda player,state:state.has_group("Loot",player,36) and state.has("Astralite",player), 'Seaport Underground'),
	('Clear Enemy Waves', lambda player,state:state.has_group("Loot",player,40), 'The Spirit World'),
	('Defeat Zenith', lambda player,state:state.has_group("Loot",player,45), 'Endgame')
]



