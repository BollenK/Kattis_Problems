# Change set to list and use ordered to get in lexicographical order.
class Graph():
    E = {}
    V = []
    def __init__(self):
        pass
    def addedge(self, n_from , n_to, val):
        if not n_from in self.E:
            self.E[n_from] = {}
        if not n_to in self.E[n_from]:
            self.E[n_from][n_to] = []
        self.E[n_from][n_to].append(val)
def main():
    G = Graph()
    
    for i in range(int(input())):
        word=input()
        G.addedge(word[0], word[len(word) -1], word)
    print(G.E)
    if is_semi_eulerian_digraph(G.E.keys(), G.E):
        start=find_start_node(G.E.keys(), G.E)
        edges = []
        for vertex in G.E:
            for adj in G.E[vertex]:
                for connected_by in G.E[vertex][adj]:
                    edges.append(connected_by)
        path=list(reversed(DFS_path(G.E.keys(), G.E, start, [],{edge: False for edge in edges })))
        print(path)
        catenym=[]
        for i in range(len(path) -1):
            to_put = sorted(G.E[path[i]][path[i+1]])[0]
            G.E[path[i]][path[i+1]].remove(to_put)
            # G.E[path[i]][path[i+1]].remove(to_put)
            catenym.append(to_put)
        print(".".join(catenym))
    else:
        print("***")
def find_start_node(V, E):
    start=None
    if len(V)==1:
        return V[0]
    for vertex in V:
        incoming = [E[other_vertex][vertex] for other_vertex in V if vertex in E[other_vertex]]
        if len(E[vertex]) - len(incoming)==1:
            return vertex
        if len(E[vertex])==1:
            start=vertex
    return start
def is_connected_digraph(V, E):
    try:
        visited = DFS(V, E, list(V)[0], {vertex:False for vertex in V})
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
    # visited[current]=True
    print("now at " + current)
    for neighbour in E[current]:
        for arc_to_neighbour in E[current][neighbour]:
            if not visited[arc_to_neighbour]:
                print("Going to neighbour" + neighbour + " with arc:" + arc_to_neighbour)
                visited[arc_to_neighbour] = True
                DFS_path(V, E, neighbour, path, visited)
    path.append(current)
    return path
def is_semi_eulerian_digraph(V, E):
    even=0
    amount_in_out_one=0
    amount_out_in_one=0
    for vertex in V:
        incoming = [item for sublist in [E[other_vertex][vertex] for other_vertex in V if vertex in E[other_vertex]] for item in sublist] 
        outgoing = [item for sublist in [E[vertex][item] for sublist in E[vertex] for item in sublist] for item in sublist]  
        print()
        print(vertex)
        print(incoming)
        print(outgoing)

        if len(outgoing) > len(incoming) and (len(outgoing) - len(incoming))==1:
            print("first if:"  + vertex)
            amount_out_in_one+=1
        elif len(incoming) > len(outgoing) and (len(incoming) - len(outgoing))==1:
            print("second if:  " + vertex)
            amount_in_out_one+=1
        elif len(incoming)==len(outgoing):
            even+=1
    print(is_connected_digraph(V, E))
    print(amount_in_out_one)
    print(amount_out_in_one)

    return is_connected_digraph(V, E) and amount_in_out_one<=1 and amount_out_in_one<=1 and amount_in_out_one+amount_out_in_one+even==len(V)

if __name__ == "__main__":
    for _ in range(int(input())):
        main()



