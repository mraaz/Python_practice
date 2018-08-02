from collections import defaultdict
import heapq

class Graph:
    def __init__(self):
        self.nodes = set() # set object
        self.edges = defaultdict(list)
        self.distances = {}

    def add_nodes(self, value):
        for i in value:
            self.nodes.add(i) # add element into set

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node) # dict to neighbour nodes
        self.distances[(from_node, to_node)] = distance # dict for distance
        self.distances[(to_node, from_node)] = distance

def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}
    heap = []

    entry = [0, initial]
    heapq.heappush(heap, entry)

    nodes = set(graph.nodes)

    while nodes:

        if not heap:
            break #If there are still nodes, we can't reach them from the initial node so bail

        min_entry = heapq.heappop(heap)
        min_node = min_entry[1]

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node
                entry = [weight, edge]
                heapq.heappush(heap, entry)

    return visited, path

def findshortestPath(graph, initial, destination):
    visited = {initial: 0}
    path = {}
    heap = []

    entry = [0, initial]
    heapq.heappush(heap, entry)

    nodes = set(graph.nodes)

    while nodes:

        if not heap:
            break #If there are still nodes, we can't reach them from the initial node so bail

        min_entry = heapq.heappop(heap)
        min_node = min_entry[1]

        if min_node == destination:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node
                entry = [weight, edge]
                heapq.heappush(heap, entry)

    total_weight = 0
    myPath = []
    myPath.append(initial)
    for key, value in path.items():
        if key != destination:
            myPath.append(key)
        else:
            break

    journey = []
    journey.append(destination)
    while destination != initial:
        for edge in graph.edges[destination]:
            if edge in myPath:
                total_weight += graph.distances[(destination, edge)]
                journey.append(edge)
                destination = edge
                break

    journey.reverse()
    print ("Total distance is %s" % total_weight)
    print ("Path is: ")
    return journey #visited, path


if __name__ == "__main__":
    g = Graph()
    g.add_nodes([i+1 for i in range(8)])
    g.add_edge(1, 2, 4)
    g.add_edge(1, 3, 1)
    g.add_edge(2, 4, 3)
    g.add_edge(2, 5, 7)
    g.add_edge(4, 8, 3)
    g.add_edge(5, 8, 4)
    g.add_edge(3, 6, 3)
    g.add_edge(3, 7, 2)
    g.add_edge(6, 7, 1)
    print ("nodes:", g.nodes)
    print ("edges:", g.edges)
    print ("distances: ", g.distances)

    print ("-" * 25)
    source_node = 1
    destination_node = 6
    print ("Source node:", source_node)
    print ("Destination node:", destination_node)
    print (findshortestPath(g, source_node, destination_node)) # return with visited and path
    #print (dijkstra(g, source_node)) # return with visited and path