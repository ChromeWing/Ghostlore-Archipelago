
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
	('Endgame',[]),
]

ghostlore_connections = [
	('New Adventure', None, 'Starting Zone'),
	('Rescued Master Ghosthunter', lambda player,state:state.has_group("Loot",player,2), 'Seaport'),
	('Sail to Pulau Hijawan', None,'Pulau Hijawan'),
	('Kill Rafflesia', lambda player,state:state.has_group("Loot",player,5), 'Pulau Kubor'),
	('Kill Hantu Raya', lambda player,state:state.has_group("Loot",player,8), 'Kenchanaraya Ruins'),
	('Collect Chthonite', lambda player,state:state.has_group("Loot",player,10) and state.has("Chthonite", player), 'Pulau Pasir Puaka'),
	('Kill all Jinns', lambda player,state:state.has_group("Loot",player,14), 'Pulau Bakau'),
	('Kill Hantu Tinggi', lambda player,state:state.has_group("Loot",player,16), 'Abandoned Old Hospital'),
	('Rescue little girl', lambda player,state:state.has_group("Loot",player,18), 'Batu Sinaran'),
	('Collect Astralite', lambda player,state:state.has_group("Loot",player,18) and state.has("Astralite",player), 'Endgame')
]



