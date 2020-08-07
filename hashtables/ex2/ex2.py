#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # Instantiate an empty cache and route list
    cache = {}
    route = []

    """
    Create a cache where the key is the source and value is the 
    destination.
    """ 

    for ticket in tickets:
        # if ticket.source == "NONE":
        #     route.append(ticket.destination)
        if ticket.source not in cache:
            cache[ticket.source] = ticket.destination


    # Appending starting city to route (where cache key is "NONE")
    route.append(cache["NONE"])

    # Keep appending destination cities until route[-1] == "NONE"
    while route[-1] != "NONE":
        route.append(cache[route[-1]])

    return route

