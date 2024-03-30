import csv
                    
def create_flight_network(filename: str, option: int):
    with open (filename) as f:
        lines = f. readlines ()
    input = []
    for line in lines :
        line = line . strip () # remove leading and trailing spaces
        tokens = line . split (',') # split the line into tokens
        input . append (tokens) # add the first token to the input list
    listinlst = []
    nodelst = []
    for values in input:
        listinlst.append(values)
    # print("\n lisinlst")
    # print()
    # print(listinlst)
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
                    graph[key].append((i[1],int(i[2])))
    elif option == 2:
        for key in graph:
            for i in listinlst:
                if key == i[0]:
                    graph[key].append((i[1],int(i[3])))
            
 
    return graph


def get_flight_connections(graph: dict, city: str, option: str) -> list:
    lst = [] 
    if city not in graph:
        print('this particular city not accessed by the flight network')
        return lst
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
                
            return -1
        
    return None


def add_flight(graph: dict, origin: str, destination: str, weight: int):
    for key in graph:
        if key == origin:
            for city in range(len(graph[origin])) :
                if graph[origin][city][0] == destination:
                    graph[origin][city] = (destination, weight)
                    
                    return graph
                else:
                    graph[origin].append((destination, weight))
                    return graph
        
    print ("the particular city not accessed by the flight network")
    

def add_airport(graph: dict, city: str, destination: str, weight: int):
    if city not in graph:
        graph[city] = [(destination, weight)]
    else:
        print("the airport already exists")
    return graph
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
        print('the particular city not accessed by the flight network')
    hold = graph[origin]
    for key in hold:
        if key[0] != destination:
            lst.append(key)
    graph[origin] = lst
    return graph


def remove_airport(graph: dict, city: str):
    if city not in graph:
        print('the particular city not accessed by the flight network')
        return graph

    for edges in graph:
            graph[edges] = [j for j in graph[edges] if j[0] != city] 
    del graph[city]

    return graph


def DFS_all_routes(graph: dict, origin: str, destination: str, route: list, all_routes: list):
    city = origin
    route = route + [city]  # Append the current city to the route
    
    if city == destination:  # If we reached the destination
        all_routes.append(route)  # Add the complete route to all_routes
    else:
        for neighbor in graph[city]:  # Iterate through neighbors of the current city
            if neighbor[0] not in route:  # Check if neighbor is not already visited
                DFS_all_routes(graph, neighbor[0], destination, route, all_routes)  # Recursive call with the neighbor
    
    return all_routes

def find_all_routes(graph: dict, origin: str, destination: str):
    lst = []
    all= []
    routes = DFS_all_routes(graph, origin, destination, lst, all)
    if len(routes) == 1 and len(routes[0]) == 1:
        routes = []
    return routes

def DFS_layovers(graph: dict, origin: str, destination: str,  route: list, layovers_lst: list):
    pass

def find_number_of_layovers(graph: dict, origin: str, destination: str):
    lst = find_all_routes(graph, origin, destination)
    num_of_layovers = []
    for route in lst:
        if len(route) <= 2:
            num_of_layovers.append(0)
        else:
            num_of_layovers.append(len(route))
    
    return sorted(num_of_layovers)



# print()
# print(graph)
# print()
# print(find_number_of_layovers(graph, "Dubai", "Chicago"))
# print(remove_flight(graph, "Dubai", "Seattle"))
# print(find_all_routes(graph, "Dubai", "Chicago"))
# print(remove_airport(graph, 'Dubai'))
# G2 = create_flight_network('flight_network.csv', 2)
# add_airport(G2, "Barcelona", "Mexico City", 5930)
# dist = get_flight_details(G2, "Dubai", "Seattle")
# print(dist)
G1 = create_flight_network('flight_network.csv', 1)
print("G1")
print(G1)
print()
G2 = create_flight_network('flight_network.csv', 2)
print("G2")
print()
print(G2)
print()
print(add_flight(G1, "Dubai", "Vancouver", 950))
print()
print(add_flight(G1, "Toronto", "Los Angeles", 330))
print()
print(add_flight(G2, "Toronto", "Los Angeles", 2183))