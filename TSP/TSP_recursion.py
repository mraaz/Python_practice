"""Problem as defined here: https://www.youtube.com/watch?v=JE0JE8ce1V0 """

distance  = float('inf')
bestpath = []

def FindDistance(start, end, matrix):


    distance = 0

    x = matrix[start]
    if end == 'A':
        distance+= x[0]
    elif end == 'B':
        distance+= x[1]
    elif end == 'C':
        distance+= x[2]
    elif end == 'D':
        distance+= x[3]

    return distance

def GetSmallestPath(mydistance, cur_path):
    global distance
    global bestpath

    if mydistance < distance:
        distance = mydistance
        bestpath = cur_path
    return

def main():
    start_node = 'A'
    all_cities = []


    cities_matrix = {'A': [0,20,42,25],
                     'B': [20,0,30,34],
                     'C': [42,30,0,10],
                     'D': [25,34,10,0]
                     }

    for x in cities_matrix:
        all_cities.append(x)

    def loopthru_cities(node):
        leaf = True
        for city in all_cities:
            if not node and city != start_node:
                continue
            if city not in node:
                new_path = node[:]
                new_path.append(city)
                loopthru_cities(new_path)
                leaf = False

        if leaf:
            calDistance = 0

            node.append(start_node)

            for x in range(len(node)-1):
                calDistance += FindDistance(node[x],
                                            node[x + 1], cities_matrix)
            GetSmallestPath(calDistance, node)

        return


    loopthru_cities([])

    print(distance)
    print(bestpath)

if __name__ == "__main__":
    main()