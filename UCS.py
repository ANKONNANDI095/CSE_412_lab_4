def UCS(graph, start, goal):
    p_queue = [(0, start)]
    costs = {start: 0}
    parents = {start: None}

    while p_queue:
        p_queue.sort()
        crr_cost, crr_node = p_queue.pop(0)

        if crr_node == goal:
            path = []
            while crr_node is not None:
                path.append(crr_node)
                crr_node = parents[crr_node]
            return path[::-1], crr_cost

        for neighbor, weight in graph[crr_node]:
            new_cost = crr_cost + weight
            if neighbor not in costs or new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                parents[neighbor] = crr_node
                p_queue.append((new_cost, neighbor))

    return None, float("inf")

graph = {
    'A': [('B', 5), ('C', 2)],
    'B': [('D', 1), ('E', 4)],
    'C': [('F', 1), ('G', 7)],
    'F': [('H', 4), ('I', 5)],
    'G': []
}

start = 'A'
goal = 'D'
path, cost = UCS(graph, start, goal)
print("Path:", path)
print("Cost:", cost)
