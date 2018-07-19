from collections import defaultdict

# Basic Tree structure
class Node:
    def __init__(self):
        # default dictionary to store graph
        # key : Node , values : NeighbouringNodes
        self.graph = defaultdict(list)

    # since graph is bidirectional, add as neighbour both ways (both sources)
    def add_edge(self, u: int, v: int):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, source: int):

        dfs_traverse = []

        # keep track of nodes traversed already
        is_visited = [False] * len(self.graph)
        print(is_visited)

        # Queue used for keeping track of next node to be travelled - start with Source
        stack = [source]

        # mark source as visited (as its already added to queue_
        is_visited[source] = True

        curr_node = source
        while len(stack) > 0:
            # print(dfs_traverse,stack)
            dfs_traverse.append(curr_node)

            # flag to see if next neighbour is found
            flag_found_next = False

            # find next element to put into stack
            while not flag_found_next and len(stack) > 0:

                # find next element (neighbour)
                for neighbour_node in self.graph[curr_node]:
                    if not is_visited[neighbour_node]:
                        # make visited True as they join queue
                        is_visited[neighbour_node] = True
                        stack.append(neighbour_node)
                        curr_node = neighbour_node
                        flag_found_next = True
                        break

                # pop stack
                if not flag_found_next and len(stack):
                    # remove last element
                    curr_node = stack.pop()
                    # print("POP : ",curr_node,stack)

        return dfs_traverse

def run_dfs(node: Node, source: int):
    return node.dfs(source)

# main
if __name__ == "__main__":
    """
        Constructing below graph
                   0
                 /   \
                1     2
               /  \  /
              3 --- 4
               \   /
                 5
                 
    
    Output :
    Depth First Search traversal
     0 1 3 4 2 5
    """

    node = Node()
    node.add_edge(0, 1)
    node.add_edge(0, 2)
    node.add_edge(1, 3)
    node.add_edge(1, 4)
    node.add_edge(2, 4)
    node.add_edge(3, 4)
    node.add_edge(3, 5)
    node.add_edge(4, 5)

    dfs_traverse = run_dfs(node, 0)

    print("Depth First Search traversal")
    #print(' '.join(str(ele) for ele in dfs_traverse))