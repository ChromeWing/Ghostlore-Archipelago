
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
	('Rescued Master Ghosthunter', None, 'Seaport'),
	('Sail to Pulau Hijawan', None,'Pulau Hijawan'),
	('Kill Rafflesia', None, 'Pulau Kubor'),
	('Kill Hantu Raya', None, 'Kenchanaraya Ruins'),
	('Collect Chthonite', ["Chthonite"], 'Pulau Pasir Puaka'),
	('Kill all Jinns', None, 'Pulau Bakau'),
	('Kill Hantu Tinggi', None, 'Abandoned Old Hospital'),
	('Rescue little girl', None, 'Batu Sinaran'),
	('Collect Astralite', ["Chthonite", "Astralite"], 'Endgame')
]



