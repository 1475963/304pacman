## module for data processing to treat data

import board_properties as Config

"""
/*\ data process function /*\
Creates a dictionnary where tons of dictionnaries are stored to make graph-like representation of the map
Each node contains her neighbors with their distances
"""

def     get_dist_map(dist_map):
    data = dict()
    ymax = len(dist_map)
    xmax = len(dist_map[0])
    tmp = 0
    for y, line in enumerate(dist_map):
        for x, item in enumerate(line):
            if dist_map[y][x] != '1':
                tmp = str((xmax * y) + x)
                data[tmp] = dict()
                if y + 1 < ymax and dist_map[y + 1][x] != '1':
                    data[tmp].setdefault(str((xmax * (y + 1)) + x), 1)
                if y - 1 >= 0 and dist_map[y - 1][x] != '1':
                    data[tmp].setdefault(str((xmax * (y - 1)) + x), 1)
                if x + 1 < xmax and dist_map[y][x + 1] != '1':
                    data[tmp].setdefault(str((xmax * y) + (x + 1)), 1)
                if x - 1 >= 0 and dist_map[y][x - 1] != '1':
                    data[tmp].setdefault(str((xmax * y) + (x - 1)), 1)
    return data

"""
/*\ data process function /*\
Returns a tuple x,y where ghost location is stored
"""

def     get_ghost(fileMap):
    for y, line in enumerate(fileMap):
        for x, case in enumerate(line):
            if fileMap[y][x] == Config.ghost_rpz:
                return (y, x)

"""
/*\ data process function /*\
Returns a tuple x,y where pacman location is stored
"""

def     get_pacman(fileMap):
    for y, line in enumerate(fileMap):
        for x, case in enumerate(line):
            if fileMap[y][x] == Config.pacman_rpz:
                return (y, x)

"""
/*\ data process function /*\
Dijkstra algorithm implementation recurcively
Returns shortest path from one point to another in graph
"""

def     dijkstra_alg(graph, src, dest, path, distances, visited=[], predecessors={}):
    if src == dest:
        pred = dest
        while pred != None:
            path.append(pred)
            pred = predecessors.get(pred, None)
    else:
        if not visited:
            distances[src] = 0

        for neighbor in graph[src] :
            if neighbor not in visited:
                new_distance = distances[src] + graph[src][neighbor]
                if new_distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = src

        visited.append(src)

        unvisited = {}

        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k, float('inf'))

        dijkstra_alg(graph, min(unvisited, key=unvisited.get), dest, path, distances, visited, predecessors)
