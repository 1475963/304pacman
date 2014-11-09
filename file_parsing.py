## module with file parsing functions to extract and treat some data

import board_properties as Config

"""
/*\ file parsing function /*\
Creates a dictonnary for mandatory part
"""

def     get_map(fileName):
    data = []
    try:
        fileStream = open(fileName, 'r')
        for y, line in enumerate(fileStream):
            line = line.rstrip('\n')
            if is_valid_entry(line, y) == False:
                print("bad map")
                return None
            data.append([])
            for item in line:
                data[y].append(item)
    except IOError:
        print("the precised file doesn't exist in current directory")
        return None
    if test_last(data) == False:
        print("bad map")
        return None
    return data

"""
/*\ file parsing function /*\
Checks if line is correct
"""

def     is_valid_entry(line, y):
    if line.startswith(Config.wall_rpz) == False:
        return False
    if line.endswith(Config.wall_rpz) == False:
        return False
    for char in line:
        if char != Config.ghost_rpz and char != Config.pacman_rpz and char != Config.wall_rpz and char != Config.space_rpz:
            return False
    if y == 0:
        for char in line:
            if char != Config.wall_rpz:
                return False
    return True

"""
/*\ file parsing function /*\
Checks if last line is correct
"""

def     test_last(data):
    line = data[len(data) - 1]
    for char in line:
        if char != Config.wall_rpz:
            return False
    return True
