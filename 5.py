import re
from pathlib import Path


def create_map(dest_range_start, source_range_start, length, valid_sources):
    dest_range_start = int(dest_range_start)
    source_range_start = int(source_range_start)
    length = int(length)
    source = range(source_range_start, source_range_start+length)
    dest = range(dest_range_start, dest_range_start+length)
    valid_sources = [int(s) for s in valid_sources] if not isinstance(valid_sources[0], range) else valid_sources
    print(f'Things to iterate through: {len(valid_sources)}')
    for s in valid_sources:
        if isinstance(s, range):
            print(f'Iterating range (size {len(s)})')
            for r in s:
                if r in source:
                    index = source.index(r)
                    yield str(r), str(dest[index])
        else:
            if s in source:
                index = source.index(s)
                yield str(r), str(dest[index])
    print('Entire map Yielded')


def input_map_to_list(i):
    return [l for l in i.split(':')[1].split('\n') if l]


def find_seed_id(parameter, parameter_id, seed_database):
    for k, v in seed_database.items():
        if v.get(parameter) == parameter_id:
            return k


def fill_rest(seed_database, param, previous_param=None):
    for k, s in seed_database.items():
        if s.get(param) is None:
            s[param] = k if previous_param is None else s[previous_param]


def main():
    with open(Path.cwd() / 'inputs' / '5.txt', 'r') as f:
        puzzle_input = f.read()

    seeds, seed_soil, soil_fertilizer, fertilizer_water, water_light, light_temp, temp_humid, humid_loc = puzzle_input.split('\n\n')

    # PART 1
    # seed_database = {s: {} for s in seeds.split(':')[1].split(' ') if s}

    # PART 2
    # Actually f it this is too slow approach, part 1 might still work if uncommented
    # but I don't really care at this point.
    seed_database = {}
    seed_ids = []
    seed_pairs = re.findall(r'(\d+ \d+)', seeds)
    for pair in seed_pairs:
        print('Processing a seed pair')
        start, length = pair.split(' ')
        seed_ids.append(range(int(start), int(start)+int(length)))
        # pair_db_part = {str(s): dict() for s in range(int(start), int(start)+int(length))}
        # seed_database.update(pair_db_part)

    print('All seed numbers found')
    seed_soil = input_map_to_list(seed_soil)
    soil_fertilizer = input_map_to_list(soil_fertilizer)
    fertilizer_water = input_map_to_list(fertilizer_water)
    water_light = input_map_to_list(water_light)
    light_temp = input_map_to_list(light_temp)
    temp_humid = input_map_to_list(temp_humid)
    humid_loc = input_map_to_list(humid_loc)
    for l in seed_soil:
        print(f'Seed soil line: {l}')
        for seed, soil in create_map(*l.split(' '), seed_ids):
            seed_database[seed] = {'soil': soil}
    print('Filling rest of soils')
    fill_rest(seed_database, 'soil')
    print('Soil done')
    for l in soil_fertilizer:
        for soil, fertilizer in create_map(*l.split(' '), [f['soil'] for f in seed_database.values() if 'soil' in f]):
            seed_database[find_seed_id('soil', soil, seed_database)].update({'fertilizer': fertilizer})
    print('Filling rest of fertilizers')
    fill_rest(seed_database, 'fertilizer', 'soil')
    print('Fertilizer done')
    for l in fertilizer_water:
        for fertilizer, water in create_map(*l.split(' '), [f['fertilizer'] for f in seed_database.values() if 'fertilizer' in f]):
            seed_database[find_seed_id('fertilizer', fertilizer, seed_database)].update({'water': water})
    fill_rest(seed_database, 'water', 'fertilizer')
    print('Water done')
    for l in water_light:
        for water, light in create_map(*l.split(' '), [f['water'] for f in seed_database.values() if 'water' in f]):
            seed_database[find_seed_id('water', water, seed_database)].update({'light': light})
    fill_rest(seed_database, 'light', 'water')
    print('Light done')
    for l in light_temp:
        for light, temp in create_map(*l.split(' '), [f['light'] for f in seed_database.values() if 'light' in f]):
            seed_database[find_seed_id('light', light, seed_database)].update({'temp': temp})
    fill_rest(seed_database, 'temp', 'light')
    print('Temp done')
    for l in temp_humid:
        for temp, humid in create_map(*l.split(' '), [f['temp'] for f in seed_database.values() if 'temp' in f]):
            seed_database[find_seed_id('temp', temp, seed_database)].update({'humid': humid})
    fill_rest(seed_database, 'humid', 'temp')
    print('Humid done')
    for l in humid_loc:
        for humid, loc in create_map(*l.split(' '), [f['humid'] for f in seed_database.values() if 'humid' in f]):
            seed_database[find_seed_id('humid', humid, seed_database)].update({'loc': loc})
    fill_rest(seed_database, 'loc', 'humid')
    print('Loc done')

    print(seed_database)
    closest = 1000000000000000000000000000000000
    for s in seed_database.values():
        if int(s.get('loc', closest)) < closest:
            closest = int(s['loc'])
    print(closest)


if __name__ == '__main__':
    main()
