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
    if option == 1:
        for key in graph:
            for i in listinlst:
                if key == i[0]:
                    graph[key].append((i[1],i[2]))
    elif option == 2:
        for key in graph:
            for i in listinlst:
                if key == i[0]:
                    graph[key].append((i[1],i[3]))
            
 
    return graph


def get_flight_connections(graph: dict, city: str, option: str) -> list:
    lst = [] 
    if option == "i":
        for key in graph: #! incoming flights
            if key != city:
                for flight in graph[key]:
                    if flight[0] == city:
                        lst.append(key)
    elif option == 'o': #! outgoing flights
        for cities in graph[city]:
            lst.append(cities[0])
                        
    return lst

def get_number_of_flight_connections(graph: dict, city: str, option: str) -> int:
    return len(get_flight_connections(graph, city, option))

def get_flight_details(graph: dict, origin: str, destination: str) -> int:
    for key in graph:
        if key == origin:
            for city in graph[origin] :
                if city[0] == destination:
                    return city[1]
                else:
                    return -1
        
    return None


def add_flight(graph: dict, origin: str, destination: str, weight: int):
    for key in graph:
        if key == origin:
            for city in range(len(graph[origin])) :
                if graph[origin][city][0] == destination:
                    graph[origin][city] = (destination, weight)
                    
                    return
                else:
                    graph[origin].append((destination, weight))
                    return
        
    print ("the particular city not accessed by the flight network")
    

def add_airport(graph: dict, city: str, destination: str, weight: int):
    if city not in graph:
        graph[city] = [(destination, weight)]
    else:
        print("this airport already exists.")

def get_secondary_flights(graph: dict, city: str):
    flst = []
    lst = get_flight_connections(graph, city, 'i')
    for cities in lst:
        nlst = get_flight_connections(graph, cities, 'i')
        for key in nlst:
            if key not in flst:
                if key != city:
                    flst.append(key)
        
    return flst



def counting_common_airports(graph: dict, cityA: str, cityB: str) -> int:
    lst1 = get_flight_connections(graph, cityA, "o")
    lst2 = get_flight_connections(graph, cityB, "o")
    count = 0
    for cities in lst1:
        for city in lst2:
            if cities == city:
                count += 1
    return count 


def remove_flight(graph: dict, origin: str, destination: str):
    lst = []
    if origin not in graph or destination not in graph:
        print('this particular city not accessed by the flight network')
    hold = graph[origin]
    for key in hold:
        if key[0] != destination:
            lst.append(key)
    graph[origin] = lst
    return graph


def remove_airport(graph: dict, city: str):
    if city not in graph:
        print('this particular city not accessed by the flight network')


    for edges in graph:
            graph[edges] = [j for j in graph[edges] if j[0] != city]
    # for cities in graph:
    #     for flight in range(len(graph[cities])):
    #         if graph[cities][flight] == city:
    #             pop(graph[cities][flight])
    
    del graph[city]

    return graph


def DFS_all_routes(graph: dict, origin: str, destination: str, route: list, all_routes: list):
    pass

def find_all_routes(graph: dict, origin: str, destination: str):
    pass

def DFS_layovers(graph: dict, origin: str, destination: str,  route: list, layovers_lst: list):
    pass

def find_number_of_layovers(graph: dict, origin: str, destination: str):
    pass

get_flight_connections(create_flight_network('flight_network.csv', 2), 'Dubai', "o")
graph = create_flight_network('flight_network.csv', 2)
print()

#print(graph)

print()

print(remove_airport(graph, 'Dubai'))