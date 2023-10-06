from collections import defaultdict

def maxDetonatedBombs(bombs):
    def distance(b1, b2):
        return ((b1[0] - b2[0]) ** 2 + (b1[1] - b2[1]) ** 2)**.5

    def dfs(node, visited, graph):
        print("function recurs: cur node = " + str(node))
        visited.add(node)
        count = 1
        for neighbor in graph[node]:
            if neighbor not in visited:
                count += dfs(neighbor, visited, graph)
        print("function returns: count = " + str(count) + "; node = " + str(node))       
        return count

    n = len(bombs)
    graph = defaultdict(list)

    for i in range(n):
        for j in range(i + 1, n):
            if distance(bombs[i], bombs[j]) <= bombs[i][2]:
                graph[i].append(j)
            if distance(bombs[i], bombs[j]) <= bombs[j][2]:
                graph[j].append(i)
    print(graph)

    maxDetonated = 0

    for i in range(n):
        visited = set()
        maxDetonated = max(maxDetonated, dfs(i, visited, graph))

    return maxDetonated



print(maxDetonatedBombs([[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]))