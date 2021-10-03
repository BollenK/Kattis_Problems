from collections import defaultdict
from itertools import groupby
from sys import setrecursionlimit
setrecursionlimit(2048)
def main():
    t = int(input())
    for _ in range(t):
        word_count = int(input())
        G = create_graph(word_count)
        if len(G[0])==0:
            print("***")
        elif is_eulerian_digraph(*G) and is_connected_digraph(*G):
            start=find_start_node(*G)
            path=list(reversed(DFS_path(G[0], G[1], start, [],{vertex: False for vertex in G[0]})))
            print('.'.join(path))
        else:
            print("***")
        
def create_graph(word_count):
    V = []
    for _ in range(word_count):
        try:
            inp = input()
            V.append(inp)
        except:
            pass
    E = defaultdict(list)

    for node in V:
        for other_node in V:
            if node is not other_node and list(node)[-1] == list(other_node)[0]: # last letter of node equals first letter of other node
                E[node].append(other_node)
    return (V,E)
def is_eulerian_digraph(V, E):
    even=0
    amount_in_out_one=0
    amount_out_in_one=0
    for vertex in V:
        incoming = [other_vertex for other_vertex in V if vertex in E[other_vertex]]
        if (len(E[vertex]) - len(incoming))==1:
            amount_out_in_one+=1
        elif len(incoming) - len(E[vertex])==1:
            amount_in_out_one+=1
        elif len(incoming)==len(E[vertex]):
            even+=1
    return is_connected_digraph(V, E) and amount_in_out_one<=1 and amount_out_in_one<=1 and amount_in_out_one+amount_out_in_one+even==len(V)
def is_connected_digraph(V, E):
    try:
        visited = DFS(V, E, V[0], {vertex:False for vertex in V})
    except:
        return False
    for key in visited.keys():
        if not visited[key]:
            return False
    return True
def DFS(V, E, current, visited):
    visited[current] = True
    for neighbour in E[current]:
        if not visited[neighbour]:
            DFS(V, E, neighbour, visited)
    return visited
def DFS_path(V, E, current, path, visited):

    visited[current]=True
    for neighbour in E[current]:
        if not visited[neighbour]:
            DFS_path(V, E, neighbour, path, visited)
    path.append(current)
    return path
def find_start_node(V, E):
    start=None
    if len(V)==1:
        return V[0]
    for vertex in V:
        incoming = [other_vertex for other_vertex in V if vertex in E[other_vertex]]
        if len(E[vertex]) - len(incoming)==1:
            return vertex
        if len(E[vertex])==1:
            start=vertex
    return start


if __name__ == "__main__":
    main()