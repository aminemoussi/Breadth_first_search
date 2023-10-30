import collections
import time

def breadth_first_s(graph, root):
    visited = set()              #bunch of unordered and unduplicated elements
    queue = collections.deque([root])
    while queue:
        vertex = queue.popleft()
        visited.add(vertex)
        for i in graph[vertex]:
            if i not in visited:
                queue.append(i)
    print("Queue has been emptied, the graph has been ran through.")
    time.sleep(1.5)
    print("Your Breadth first search path is: ",visited)

graph = {              #key value list, keys must be unique
    0: [1, 2, 3],
    1: [],
    2: [],
    3: [4, 5],
    4: [],
    5: []

}

breadth_first_s(graph, 0)