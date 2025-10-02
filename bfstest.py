
G = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


def BFS(graph, start_node):
    """
    Performs a Breadth-First Search on the given graph starting from start_node.
    """
    queue = [start_node]
    visited = set([start_node])
    
    print(f"Starting BFS from node: {start_node}")
    
    while queue:
        
        node = queue.pop(0)
        print(node)
        
        
        for neighbor in graph[node]:
           
            if neighbor not in visited:
                
                visited.add(neighbor)
                
                queue.append(neighbor)


if __name__ == "__main__":
   
    start_node = 'A'
    
    
    BFS(G, start_node)