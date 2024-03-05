from typing import Dict, Tuple

from adapters import data_saving, poke_info

_legendaries = [
    'rayquaza',
    'kyurem',
    'giratina-altered',
    'lugia',
    'articuno',
]

_starters = {
    1: ['bulbasaur', 'charmander', 'squirtle'],
    2: ['chikorita', 'cyndaquil', 'totodile'],
    3: ['treecko', 'torchic', 'mudkip'],
    4: ['turtwig', 'chimchar', 'piplup'],
    5: ['snivy', 'tepig', 'oshawott'],
}


def collect_legendaries(*args) -> Dict[str, Tuple[str]]:
    legendaries_data = {}

    for legendary_name in _legendaries:
        legendaries_data[legendary_name] = poke_info.types(legendary_name)
    
    data_saving.save(legendaries_data)
    return legendaries_data


def collect_starter_from_generation(generation_number: str, *args) -> Dict[str, Tuple[str]]:
    starters_data = {}

    try:
        generation_starters = _starters.get(int(generation_number), None)

        if not generation_starters:
            return {}
        
        for starter_name in generation_starters:
            starters_data[starter_name] = poke_info.types(starter_name)

        data_saving.save(starters_data)
        return starters_data
    
    except:
        return {}