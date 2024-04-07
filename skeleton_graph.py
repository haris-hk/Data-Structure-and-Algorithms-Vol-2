import csv

# Function to create a flight network from a CSV file
def create_flight_network(filename: str, option: int):
    
    with open(filename) as f:

        lines = f.readlines()
    
    input = []
    
    for line in lines:
       
        line = line.strip()
        
        tokens = line.split(',')
        input.append(tokens)
    # Initialize an empty list to store the lists in the input
    listinlst = []
    # Initialize an empty list to store the nodes
    nodelst = []
    for values in input:
        listinlst.append(values)
    for h in range(1, len(listinlst)):
        v = listinlst[h]
        if v[0] not in nodelst:
            nodelst.append(v[0])
    graph = {}
    # For each node in the list of nodes
    for val in nodelst:
        # Add the node to the graph with an empty list of connections
        graph[val] = []
    if option == 1:
        # For each node in the graph
        for key in graph:
            # For each list in the list of lists
            for i in listinlst:
                if key == i[0]:
                    # Add a connection from the node to the second element of the list with the third element of the list as the weight
                    graph[key].append((i[1],int(i[2])))
    elif option == 2:
        # For each node in the graph
        for key in graph:
            for i in listinlst:
                if key == i[0]:
                    # Add a connection from the node to the second element of the list with the fourth element of the list as the weight
                    graph[key].append((i[1],int(i[3])))

    # Return the graph
    return graph


def get_flight_connections(graph: dict, city: str, option: str) -> list:
    lst = [] 
    if city not in graph:
        print('this particular city not accessed by the flight network')
        return lst
    if option == "i":
        for key in graph:
            if key != city:
                for flight in graph[key]:
                    if flight[0] == city:
                        # Add the city to the list of connections
                        lst.append(key)
    elif option == 'o':
        for cities in graph[city]:
            lst.append(cities[0])

    return lst

# Function to get the number of flight connections from a city
def get_number_of_flight_connections(graph: dict, city: str, option: str) -> int:

    return len(get_flight_connections(graph, city, option))

# Function to get the flight details from an origin to a destination
def get_flight_details(graph: dict, origin: str, destination: str) -> int:
    for key in graph:
        if key == origin:
            for city in graph[origin] :
                if city[0] == destination:
                    return city[1]
            return -1
    return None

# Function to add a flight to the graph
def add_flight(graph: dict, origin: str, destination: str, weight: int):
    # If either the origin or destination is not in the graph, print a message and return the graph
    if destination not in graph or origin not in graph:
        print("the particular city not accessed by the flight network")
        return graph
    if destination in graph:    
        for key in graph:
            if key == origin:
                for city in range(len(graph[origin])):
                    if graph[origin][city][0] == destination:
                        graph[origin][city] = (destination, weight)
                        return graph
                    
    # If no flight to the destination is found, add a new flight to the destination with the given weight
    graph[origin].append((destination, weight))
    return graph

# Function to add an airport to the graph
def add_airport(graph: dict, city: str, destination: str, weight: int):
    if city not in graph:
        graph[city] = [(destination, weight)]
    else:
        print("the airport already exists")
    # Return the updated graph
    return graph
            

# Function to get secondary flights from a given city
def get_secondary_flights(graph: dict, city: str):
    # Initialize an empty list to store the secondary cities
    nlst = []
    if city not in graph:
        return None
    lst = graph[city]
    for cities in lst:
        # Add the outbound connections to the list of secondary cities
        # Use list comprehension to get the cities and check if they are not already in the list
        nlst = nlst + [key[0] for key in graph[cities[0]] if key[0] not in nlst]    
    # Return the list of secondary cities
    return nlst

# Function to count the common airports between two cities
def counting_common_airports(graph: dict, cityA: str, cityB: str) -> int:
    lst1 = get_flight_connections(graph, cityA, "o")
    lst2 = get_flight_connections(graph, cityB, "o")
    count = 0
    for cities in lst1:
        for city in lst2:
            # If the cities are the same, increment the counter
            if cities == city:
                count += 1
    return count  


# Function to remove a flight from the graph
def remove_flight(graph, origin, destination):
    lst = []
    if origin not in graph or destination not in graph:
        print('the particular city not accessed by the flight network')
        return graph
    # Get the flights from the origin
    hold = graph[origin]
    for key in hold:
        # If the destination of the flight is not the destination to be removed, add it to the list
        if key[0] != destination:
            print(key)
            lst.append(key)
    graph[origin] = lst
    # Update the flights to the origin in the graph
    graph[destination] = [flight for flight in graph[destination] if flight[0] != origin]
    return graph


# Function to remove an airport from the graph
def remove_airport(graph, city):
    if city not in graph:
        print('the particular city not accessed by the flight network')
        return graph
    for edges in graph:
        graph[edges] = [j for j in graph[edges] if j[0] != city] 
    del graph[city]
    return graph


def DFS_all_routes(graph, origin, destination, route, all_routes):
    city = origin
    route = route + [city]
    
    if city == destination:
        # Add the complete route to the list of all routes
        all_routes.append(route)
    else:
        for neighbor in graph[city]:
            # If the neighbor has not been visited
            if neighbor[0] not in route:
                # Recursively call the function with the neighbor as the new origin
                DFS_all_routes(graph, neighbor[0], destination, route, all_routes)
        
    return all_routes

# Function to find all routes from an origin to a destination
def find_all_routes(graph: dict, origin: str, destination: str):
    lst = []
    all= []
    if destination not in graph or origin not in graph:
        return None
    routes = DFS_all_routes(graph, origin, destination, lst, all)
    # If there is only one route that is to and from the city, set routes to an empty list
    if len(routes) == 1 and len(routes[0]) == 1:
        routes = []

    return routes


def DFS_layovers(graph: dict, origin: str, destination: str,  route: list, layovers_lst: list):
    pass

# Function to find the number of layovers from an origin to a destination
def find_number_of_layovers(graph: dict, origin: str, destination: str):
    dlst = []
    flst = []
    if destination not in graph or origin not in graph:
        return None
    lst = DFS_all_routes(graph, origin, destination, dlst, flst)
    print (lst)
    num_of_layovers = []
    for route in lst:
        # If the route only contains immidiate connection, append 0 to the list of layovers
        if len(route) == 2:
            num_of_layovers.append(0)
        # If there is only one route that is to and from the city, return an empty list
        elif len(route) == 1:
            return []
        # Otherwise, append the number of layovers (length of the route minus 2 to make sure the origin and destination do not count as layovers) to the list of layovers
        else:
            num_of_layovers.append(len(route)-2)
    return sorted(num_of_layovers)





G = create_flight_network('flight_network.csv', 1)
print(find_all_routes(G, "Dubai", "Seattle"))