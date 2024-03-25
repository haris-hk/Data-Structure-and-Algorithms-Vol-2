import csv

def addVertices(G: dict, vertices: list):
    for val in vertices:
        G[val] = []
    return

def addEdges(G: dict, edges: list):
        for key in G:
            for i in range(len(edges)):
                for j in range(2):
                    if edges[i][0] == key:
                        G[key].append(edges[i][1])
                    

def create_flight_network(filename: str, option: int):
    with open (filename) as f:
        lines = f. readlines ()
    input = []
    for line in lines :
        line = line . strip () # remove leading and trailing spaces
        tokens = line . split () # split the line into tokens
        input . append (tokens[0]) # add the first token to the input list
    listinlst = []
    nodelst = []
    for values in input:
        words = values.split(',')
        listinlst.append(words)
    for h in range(1, len(listinlst)):
        v = listinlst[h]
        if v[0] not in nodelst:
            nodelst.append(v[0])
    graph = {}
    for val in nodelst:
        graph[val] = []
    for key in graph:
        for i in listinlst:
            if key == i[0]:
                graph[key].append((i[1],i[2]))
            
    print(graph)
    return 


def get_flight_connections(graph: dict, city: str, option: str) -> list:
    pass

def get_number_of_flight_connections(graph: dict, 
                                     city: str, 
                                     option: str) -> int:
    pass

def get_flight_details(graph: dict, origin: str, destination: str) -> int:
    pass

def add_flight(graph: dict, origin: str, destination: str, weight: int):
    pass

def add_airport(graph: dict, city: str, destination: str, weight: int):
    pass

def get_secondary_flights(graph: dict, city: str):
    pass

def counting_common_airports(graph: dict, cityA: str, cityB: str) -> int:
    pass

def remove_flight(graph: dict, origin: str, destination: str):
    pass

def remove_airport(graph: dict, city: str):
    pass

def DFS_all_routes(graph: dict,
                    origin: str, 
                    destination: str,
                    route: list, 
                    all_routes: list):
    pass

def find_all_routes(graph: dict, origin: str, destination: str):
    pass

def DFS_layovers(graph: dict, origin: str, destination: str, 
                 route: list, 
                 layovers_lst: list):
    pass

def find_number_of_layovers(graph: dict, origin: str, destination: str):
    pass

print(create_flight_network('flight_network.csv', 1))