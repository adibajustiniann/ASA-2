MAX_N = 1000

# Create an adjacency matrix to represent the graph
graph = [[0] * (MAX_N + 1) for _ in range(MAX_N + 1)]

# Create a list to keep track of visited nodes
visited = [False] * (MAX_N + 1)

# Initialize the traversal count to zero
traversal_count = 0

# Define the DFS function to traverse the graph
def DFS(current_node, n, virus_node):
    global traversal_count
    visited[current_node] = True
    traversal_count += 1

    # If the current node is the virus node, print the traversal count
    if current_node == virus_node:
        print(f"{traversal_count} node traversed, computer {virus_node} is dangerous")
        return
        
    # Traverse the adjacent nodes
    for i in range(1, n + 1):
        if graph[current_node][i] and not visited[i]:
            DFS(i, n, virus_node)

# Define the main function
if __name__ == "__main__":
    n = int(input())

    # Find the virus node and build the graph
    virus_node = 0
    for i in range(1, n + 1):
        parent, virus = map(int, input().split())
        if virus == 0:
            virus_node = i
        graph[parent][i] = 1
        #graph[i][virus] = 0