'''
Travelling Salesman Problem

member1: <Andrii Bilyi>
member2: <Markus Viktoria>
member3: <Voitiv Zakhar>
member4: <Dmytro Malik>
member5: <Veronika Bahatyr-Zakharchenko>
'''
from typing import List
from itertools import permutations

def read_csv(file_name: str) -> List[List[int]]:
    """
    Read information about a graph from a CSV file.

    In the CSV file, each line describes a connection between two
    points in the graph. The structure of each line is: "point1 point2
    weight". Here, "point1" and "point2" are the connected points, and "weight"
    is the measure of the connection.

    Parameters:
    - file_name (str): The name of the CSV file containing the graph data.

    Returns:
    Dict{Dict{int}]: A dictionary of dictionaries representing the graph information.
    Each inner dictionary includes three pieces of information: the first point, the second point,
    and the measure of the connection.

    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as tmpfile:
    ...     _ = tmpfile.write('1,2,5\\n3,4,6\\n1,5,7')
    >>> read_csv(tmpfile.name)
    {1: {2: 5, 5: 7}, 2: {1: 5}, 3: {4: 6}, 4: {3: 6}, 5: {1: 7}}
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        town_dst={}
        file_data = [list(map(int, line.strip().split(','))) for line in file]
    for lst in file_data:
        for i in range(2):
            other_town_dst={}
            other_town_ind= 0 if i == 1 else 1

            # Creates a small dictionary
            other_town = lst[other_town_ind]
            other_town_dst[other_town]=lst[2]

            if lst[i] not in town_dst:
                # Creates a new key-value pair
                town_dst[lst[i]] = other_town_dst
            else:
                # Updates the existing key-value pair
                town_dst[lst[i]].update(other_town_dst)
    return town_dst

def calculate_length(graph: dict, path: list, min_length: int) -> tuple:
    '''
    Calculates the length of the current path
    If path does not exists or has the bigger length
    than the existing one, returns an infinity as the
    distance between towns

    :param graph dict: Connections between cities
    :param path list: A path through cities
    :param min_length int: A current minimal distaance through cities

    :return path, length tuple: A path and its length

    >>> calculate_length({1: {2: 10, 3: 15, 4: 20}, 2: {1: 10, 3: 35, 4: 25}, \
3: {1: 15, 2: 35, 4: 20}, 4: {1: 20, 3: 20, 2: 25}}, [1, 2, 3, 4, 1], float('inf'))
    ([1, 2, 3, 4, 1], 85)

    >>> calculate_length({1: {2: 10, 3: 15, 4: 20}, 2: {1: 10, 3: 35, 4: 25}, \
3: {1: 15, 2: 35, 4: 20}, 4: {1: 20, 3: 20, 2: 25}}, [1, 2, 4, 3, 1], 85)
    ([1, 2, 4, 3, 1], 70)
    '''
    length = 0

    # Checks if the way betweeen two vertexes exists
    try:
        for idx in range(len(path) - 1):
            length += graph[path[idx]][path[idx + 1]]

            # Checks if the current length is bigger than
            # minimal length
            if length > min_length:
                return path, float('inf')

        return path, length
    except KeyError:
        return path, float('inf')

def exact_algorithm(graph: dict) -> list:
    '''
    An algorithm to solve Travelling Salesman Problem(TSP)
    If the path does not exists, returns a message about it

    :param graph dict: Connections between cities

    :return final_path list: The smallest path through every town
    '''
  pass

def greedy_algorithm(graph: dict,
                    current_vertex: int = 1,
                    visited: set = None,
                    result: list = None) -> list:
    '''
    A greedy algorithm to solve TSP
    Works recursively and returns a possible path, if it
    exists

    :param graph list: Connection between cities
    :param current_vertex int: Starting point of every loop
    :param visited set:  A set of visited vertexes
    :param result list: A result path

    :return result list: A result path
    
    '''
pass

