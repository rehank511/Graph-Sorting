
def read_matrix(filename):
    matrix = []
    file = open(filename, "r")
    for line in file:
        row = list(line.strip())
        for i in range(len(row)):
            row[i] = int(row[i])
        matrix.append(row)
    return matrix


def source_find():
    global source, graph, nosource, temp
    source = 0
    nosource = len(graph[0])
    for i in range(len(graph[0])):
        count = 0
        for j in range(len(graph)):
            if graph[j][i] == 0:
                count += 1
            if count == len(graph):
                source = i
                nosource -= 1
                break
        if count == len(graph):
            break
    if nosource == len(graph[0]):
        return nosource
    else:
        temp = source_remove()


def source_remove():
    global source, graph, nosource
    for i in range(len(graph[0])):
        graph[source][i] = 0
    graph[source][source] = 1
    return source


def main():
    global source, graph, nosource, temp
    nosource = 0
    graph = read_matrix("graphs/graph3.txt")
    # To try other graphs just change the name of graph1 to graph2 or graph3
    temp1 = []
    while nosource < len(graph[0]):
        source_find()
        temp1.append(temp)
    if (len(temp1) - 1) == len(graph[0]):
        print(temp1[:-1])
    else:
        print("Sorting not possible - Graph needs to be acyclic for sorting")


if __name__ == '__main__':
    main()
