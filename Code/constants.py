status_allowed = ['par', 'psn', 'frz', 'slp', 'tox', 'brn', "fnt"]
volatile_status_allowed = ['followme', 'charge', 'octolock', 'substitute', 'syrupbomb', 'grudge', 'disable', 'dragoncheer', 'endure', 'helpinghand', 'snatch', 'powertrick', 'ragepowder', 'laserfocus', 'flinch', 'sparklingaria', 'healblock', 'confusion', 'focusenergy', 'defensecurl', 'ingrain', 'minimize', 'obstruct', 'embargo', 'magiccoat', 'bide', 'gastroacid', 'maxguard', 'tarshot', 'leechseed', 'stockpile', 'smackdown', 'spikyshield', 'magnetrise', 'torment', 'kingsshield', 'partiallytrapped', 'saltcure', 'silktrap', 'aquaring', 'electrify', 'attract', 'burningbulwark', 'banefulbunker', 'destinybond', 'miracleeye', 'protect', 'foresight', 'powder', 'noretreat', 'spotlight', 'taunt', 'encore', 'nightmare', 'yawn', 'imprison', 'curse', 'telekinesis', 'powershift']

type_advantages = {
    'Normal': {'Rock': 0.5, 'Ghost': 0},
    'Fire': {'Fire': 0.5, 'Water': 0.5, 'Grass': 2, 'Ice': 2, 'Bug': 2, 'Rock': 0.5, 'Dragon': 0.5},
    'Water': {'Fire': 2, 'Water': 0.5, 'Grass': 0.5, 'Ground': 2, 'Rock': 2, 'Dragon': 0.5},
    'Electric': {'Water': 2, 'Electric': 0.5, 'Grass': 0.5, 'Ground': 0, 'Flying': 2, 'Dragon': 0.5},
    'Grass': {'Fire': 0.5, 'Water': 2, 'Grass': 0.5, 'Poison': 0.5, 'Ground': 2, 'Flying': 0.5, 'Bug': 0.5, 'Rock': 2, 'Dragon': 0.5},
    'Ice': {'Fire': 0.5, 'Water': 0.5, 'Grass': 2, 'Ice': 0.5, 'Ground': 2, 'Flying': 2, 'Dragon': 2},
    'Fighting': {'Normal': 2, 'Ice': 2, 'Poison': 0.5, 'Flying': 0.5, 'Psychic': 0.5, 'Bug': 0.5, 'Rock': 2, 'Ghost': 0, 'Dark': 2, 'Steel': 2, 'Fairy': 0.5},
    'Poison': {'Grass': 2, 'Poison': 0.5, 'Ground': 0.5, 'Rock': 0.5, 'Ghost': 0.5, 'Steel': 0},
    'Ground': {'Fire': 2, 'Electric': 2, 'Grass': 0.5, 'Poison': 2, 'Flying': 0, 'Bug': 0.5, 'Rock': 2, 'Steel': 2},
    'Flying': {'Electric': 0.5, 'Grass': 2, 'Fighting': 2, 'Bug': 2, 'Rock': 0.5, 'Steel': 0.5},
    'Psychic': {'Fighting': 2, 'Poison': 2, 'Psychic': 0.5, 'Dark': 0, 'Steel': 0.5},
    'Bug': {'Fire': 0.5, 'Grass': 2, 'Fighting': 0.5, 'Poison': 0.5, 'Flying': 0.5, 'Psychic': 2, 'Ghost': 0.5, 'Dark': 2, 'Steel': 0.5, 'Fairy': 0.5},
    'Rock': {'Fire': 2, 'Ice': 2, 'Fighting': 0.5, 'Ground': 0.5, 'Flying': 2, 'Bug': 2, 'Steel': 0.5},
    'Ghost': {'Normal': 0, 'Psychic': 2, 'Ghost': 2, 'Dark': 0.5},
    'Dragon': {'Dragon': 2},
    'Dark': {'Fighting': 0.5, 'Psychic': 2, 'Ghost': 2, 'Dark': 0.5, 'Fairy': 0.5},
    'Steel': {'Fire': 0.5, 'Water': 0.5, 'Electric': 0.5, 'Ice': 2, 'Rock': 2, 'Steel': 0.5, 'Fairy': 2},
    'Fairy': {'Fire': 0.5, 'Fighting': 0.5, 'Poison': 2, 'Dragon': 2, 'Dark': 2, 'Steel': 0.5}
}