import csv

# Function to create a flight network from a CSV file
def create_flight_network(filename: str, option: int):
    # Open the file
    with open(filename) as f:
        # Read all lines from the file
        lines = f.readlines()
    # Initialize an empty list to store the input
    input = []
    # For each line in the file
    for line in lines:
        # Remove leading and trailing spaces
        line = line.strip()
        # Split the line into tokens using comma as the delimiter
        tokens = line.split(',')
        # Add the tokens to the input list
        input.append(tokens)
    # Initialize an empty list to store the lists in the input
    listinlst = []
    # Initialize an empty list to store the nodes
    nodelst = []
    # For each list in the input
    for values in input:
        # Add the list to the list of lists
        listinlst.append(values)
    # For each list in the list of lists
    for h in range(1, len(listinlst)):
        # Get the first element of the list
        v = listinlst[h]
        # If the element is not already in the list of nodes
        if v[0] not in nodelst:
            # Add the element to the list of nodes
            nodelst.append(v[0])
    # Initialize an empty dictionary to represent the graph
    graph = {}
    # For each node in the list of nodes
    for val in nodelst:
        # Add the node to the graph with an empty list of connections
        graph[val] = []
    # If the option is 1
    if option == 1:
        # For each node in the graph
        for key in graph:
            # For each list in the list of lists
            for i in listinlst:
                # If the node is the first element of the list
                if key == i[0]:
                    # Add a connection from the node to the second element of the list with the third element of the list as the weight
                    graph[key].append((i[1],int(i[2])))
    # If the option is 2
    elif option == 2:
        # For each node in the graph
        for key in graph:
            # For each list in the list of lists
            for i in listinlst:
                # If the node is the first element of the list
                if key == i[0]:
                    # Add a connection from the node to the second element of the list with the fourth element of the list as the weight
                    graph[key].append((i[1],int(i[3])))

    # Return the graph
    return graph


def get_flight_connections(graph: dict, city: str, option: str) -> list:
    # Initialize an empty list to store the connections
    lst = [] 
    # If the city is not in the graph, print a message and return the empty list
    if city not in graph:
        print('this particular city not accessed by the flight network')
        return lst
    # If the option is "i" (incoming flights)
    if option == "i":
        # For each city in the graph
        for key in graph:
            # If the city is not the city of interest
            if key != city:
                # For each flight from the city
                for flight in graph[key]:
                    # If the destination of the flight is the city of interest
                    if flight[0] == city:
                        # Add the city to the list of connections
                        lst.append(key)
    # If the option is 'o' (outgoing flights)
    elif option == 'o':
        # For each flight from the city of interest
        for cities in graph[city]:
            # Add the destination of the flight to the list of connections
            lst.append(cities[0])

    # Return the list of connections                    
    return lst

# Function to get the number of flight connections from a city
def get_number_of_flight_connections(graph: dict, city: str, option: str) -> int:
    # Return the number of flight connections from the city (the length of the list of connections)
    return len(get_flight_connections(graph, city, option))

# Function to get the flight details from an origin to a destination
def get_flight_details(graph: dict, origin: str, destination: str) -> int:
    # For each city in the graph
    for key in graph:
        # If the city is the origin
        if key == origin:
            # For each flight from the origin
            for city in graph[origin] :
                # If the destination of the flight is the destination
                if city[0] == destination:
                    # Return the weight of the flight
                    return city[1]
            # If no flight to the destination is found, return -1
            return -1
    # If the origin is not in the graph, return None
    return None

# Function to add a flight to the graph
def add_flight(graph: dict, origin: str, destination: str, weight: int):
    # If either the origin or destination is not in the graph, print a message and return the graph
    if destination not in graph or origin not in graph:
        print("the particular city not accessed by the flight network")
        return graph
    # If the destination is in the graph
    if destination in graph:    
        # For each city in the graph
        for key in graph:
            # If the city is the origin
            if key == origin:
                # For each flight from the origin
                for city in range(len(graph[origin])) :
                    # If the destination of the flight is the destination
                    if graph[origin][city][0] == destination:
                        # Update the weight of the flight and return the graph
                        graph[origin][city] = (destination, weight)
                        return graph
    # If no flight to the destination is found, add a new flight to the destination with the given weight
    graph[origin].append((destination, weight))
    # Return the updated graph
    return graph

# Function to add an airport to the graph
def add_airport(graph: dict, city: str, destination: str, weight: int):
    # If the city is not in the graph, add it with a flight to the destination with the given weight
    if city not in graph:
        graph[city] = [(destination, weight)]
    # If the city is already in the graph, print a message
    else:
        print("the airport already exists")
    # Return the updated graph
    return graph
            

# Function to get secondary flights from a given city
def get_secondary_flights(graph: dict, city: str):
    # Initialize an empty list to store the secondary cities
    nlst = []
    # If the city is not in the graph, return None
    if city not in graph:
        return None
    # Get the immediate connections from the city
    lst = graph[city]
    # For each immediate connection
    for cities in lst:
        # Add the outbound connections to the list of secondary cities
        # Use list comprehension to get the cities and check if they are not already in the list
        nlst = nlst + [key[0] for key in graph[cities[0]] if key[0] not in nlst]    
    # Return the list of secondary cities
    return nlst

# Function to count the common airports between two cities
def counting_common_airports(graph: dict, cityA: str, cityB: str) -> int:
    # Get the outbound connections from cityA
    lst1 = get_flight_connections(graph, cityA, "o")
    # Get the outbound connections from cityB
    lst2 = get_flight_connections(graph, cityB, "o")
    # Initialize a counter to count the common airports
    count = 0
    # For each city in the outbound connections of cityA
    for cities in lst1:
        # For each city in the outbound connections of cityB
        for city in lst2:
            # If the cities are the same, increment the counter
            if cities == city:
                count += 1
    # Return the count of common airports
    return count  


# Function to remove a flight from the graph
def remove_flight(graph, origin, destination):
    # Initialize an empty list to store the remaining flights
    lst = []
    # If either the origin or destination is not in the graph, print a message and return the graph
    if origin not in graph or destination not in graph:
        print('the particular city not accessed by the flight network')
        return graph
    # Get the flights from the origin
    hold = graph[origin]
    # For each flight from the origin
    for key in hold:
        # If the destination of the flight is not the destination to be removed, add it to the list
        if key[0] != destination:
            print(key)
            lst.append(key)
    # Update the flights from the origin in the graph
    graph[origin] = lst
    # Update the flights to the origin in the graph
    graph[destination] = [flight for flight in graph[destination] if flight[0] != origin]
    # Return the updated graph
    return graph


# Function to remove an airport from the graph
def remove_airport(graph, city):
    # If the city is not in the graph, print a message and return the graph
    if city not in graph:
        print('the particular city not accessed by the flight network')
        return graph
    # For each city in the graph
    for edges in graph:
        # Remove the flights to the city to be removed
        graph[edges] = [j for j in graph[edges] if j[0] != city] 
    # Remove the city from the graph
    del graph[city]
    # Return the updated graph
    return graph

# Function to find all routes from an origin to a destination using depth-first search
def DFS_all_routes(graph, origin, destination, route, all_routes):
    # Append the current city to the route
    city = origin
    route = route + [city]
    
    # If the current city is the destination
    if city == destination:
        # Add the complete route to the list of all routes
        all_routes.append(route)
    else:
        # For each neighbor of the current city
        for neighbor in graph[city]:
            # If the neighbor has not been visited
            if neighbor[0] not in route:
                # Recursively call the function with the neighbor as the new origin
                DFS_all_routes(graph, neighbor[0], destination, route, all_routes)
    
    # Return the list of all routes
    return all_routes

# Function to find all routes from an origin to a destination
def find_all_routes(graph: dict, origin: str, destination: str):
    # Initialize empty lists for the route and all routes
    lst = []
    all= []
    # If either the origin or destination is not in the graph, return None
    if destination not in graph or origin not in graph:
        return None
    # Call the DFS_all_routes function to find all routes from the origin to the destination
    routes = DFS_all_routes(graph, origin, destination, lst, all)
    # If there is only one route and it only contains one city, set routes to an empty list
    if len(routes) == 1 and len(routes[0]) == 1:
        routes = []
    # Return the list of all routes
    return routes


def DFS_layovers(graph: dict, origin: str, destination: str,  route: list, layovers_lst: list):
    pass

# Function to find the number of layovers from an origin to a destination
def find_number_of_layovers(graph: dict, origin: str, destination: str):
    # Initialize empty lists for the route and all routes
    dlst = []
    flst = []
    # If either the origin or destination is not in the graph, return None
    if destination not in graph or origin not in graph:
        return None
    # Call the DFS_all_routes function to find all routes from the origin to the destination
    lst = DFS_all_routes(graph, origin, destination, dlst, flst)
    # Print the list of all routes for debugging
    print (lst)
    # Initialize an empty list for the number of layovers
    num_of_layovers = []
    # For each route in the list of all routes
    for route in lst:
        # If the route only contains two cities, append 0 to the list of layovers
        if len(route) == 2:
            num_of_layovers.append(0)
        # If the route only contains one city, return an empty list
        elif len(route) == 1:
            return []
        # Otherwise, append the number of layovers (length of the route minus 2 to make sure the origin and destination do not count as layovers) to the list of layovers
        else:
            num_of_layovers.append(len(route)-2)
    # Return the list of layovers sorted in ascending order
    return sorted(num_of_layovers)





