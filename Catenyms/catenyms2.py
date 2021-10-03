# Idea: Create vertex forall letters in the input. Add a directed edge (a,b) <=> the last letter of a is the first letter of b. 
offet=97
from collections import defaultdict
def solve():
    n=int(input())
    graph=[[[] for x in range(26)] for y in range(26)]
    G = create_graph(n)
    print(G)
    if len(G[0])==0:
        print("***")
    elif is_eulerian_digraph(*G) and is_connected_digraph(*G):
        start=find_start_node(*G)
        path=list(reversed(DFS_path(G[0], G[1], start, [],{vertex: False for vertex in G[0]}, [])))
        print('.'.join(path))
    else:
        print("***")
        # graph[ord(word[0])-offet][ord(word[len(word)-1])-offet].append(word)
def create_graph(word_count):
    V = []
    E = defaultdict(list)
    for _ in range(word_count):
        try:
            inp = input()
            if not inp[0] in V:
                V.append(inp[0])
            if not inp[len(inp)-1] in V:
                V.append(inp[len(inp)-1])
            E[inp[0]].append((inp[len(inp)-1], inp)) #Edge is of form: (other_node, word)
        except:
            pass
    return (V,E)
def is_eulerian_digraph(V, E):
    even=0
    amount_in_out_one=0
    amount_out_in_one=0
    for vertex in V:
        incoming = [other_vertex for other_vertex in V if vertex in list(map(lambda t: t[0],E[other_vertex]))]
        if (len(E[vertex]) - len(incoming))==1:
            amount_out_in_one+=1
        elif len(incoming) - len(E[vertex])==1:
            amount_in_out_one+=1
        elif len(incoming)==len(E[vertex]):
            even+=1
    return is_connected_digraph(V, E) and amount_in_out_one<=1 and amount_out_in_one<=1 and amount_in_out_one+amount_out_in_one+even==len(V)
def DFS(V, E, current, visited):
    visited[current] = True
    for neighbour in sorted(list(map(lambda t: t[0],E[current])),key=lambda t: t[0]):
        print(neighbour)
        if not visited[neighbour]:
            DFS(V, E, neighbour, visited)
    return visited
def DFS_path(V, E, current, path, visited, word):

    visited[current]=True
    # for neighbour in list(map(lambda t: t[0],E[current])):
    for neighbour in E[current]:
        if not visited[neighbour[0]]:
            DFS_path(V, E, neighbour, path, visited, word)
    path.append(current)
    word.append(neighbour[1])
    return path
def is_connected_digraph(V, E):
    try:
        visited = DFS(V, E, V[0], {vertex:False for vertex in V})
    except:
        return False
    for key in visited.keys():
        if not visited[key]:
            return False
    return True
def find_start_node(V, E):
    start=None
    if len(V)==1:
        return V[0]
    for vertex in V:s
        incoming = [other_vertex for other_vertex in V if vertex in E[other_vertex]]
        if len(E[vertex]) - len(incoming)==1:
            return vertex
        if len(E[vertex])==1:
            start=vertex
    return start
    # Check even number of ndoes
if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
