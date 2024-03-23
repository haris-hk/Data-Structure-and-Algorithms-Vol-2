import csv

def addVertices(G: dict, vertices: list):
    pass

def addEdges(G: dict, edges: list):
    pass

def create_flight_network(filename: str, option: int):
    pass

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

