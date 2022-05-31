from BaseClasses import Location


class GhostloreLocation(Location):
    game: str = "Ghostlore"


# 10,133,000 - 10,133,194
offset = 10_13_3_000


shop_size = 20

kill_descriptor = [
    "Kill",
    "Slay",
    "Wipe Out",
    "Destroy",
    "Slaughter",
    "Vanquish",
    "Execute",
    "Annihilate",
    "Obliterate",
    "Exterminate"
]

regular_monster_names = [
    "Ahool",
    "Babi Ngepet",
    "E-Gui",
    "Gui-Kia",
    "Hantu Raya",
    "Hantu Tinggi",
    "Jenglot",
    "Jiang-Shi",
    "Komodo Wizard",
    "Salamancer",
    "Orang Minyak",
    "Penanggal",
    "Pocong",
    "Pontianak Tree",
    "Preta",
    "Rakshasa",
    "Toyol"
]

boss_monster_names = [
    "Mogui Summoner",
    "Rafflesia",
    "Ice Jinn",
    "Thunder Jinn",
    "Fire Jinn"
]

kill_quests = {
    f"{kill_descriptor[j]} {regular_monster_names[i]}": offset + i * 10+ j for i in range(0, len(regular_monster_names)) for j in range(0, 10)
}

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
