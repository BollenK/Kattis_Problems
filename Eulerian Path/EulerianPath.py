import copy
class Graph():
    def __init__(self, nodes):
        self.nodes = nodes
    def add_edge(self, from_, to):
        self.nodes[from_].adjecent.add(to)
        self.nodes[to].adjecent.add(from_)
    def print_graph(self):
        for vertex in self.nodes:
            for adj in vertex.adjecent:
                print(adj.n)
    def is_eulerian(self):
        count = 0
        for vertex in self.nodes:
            if len(vertex.adjecent)%2!=0:
                count+=1
        return count==2 or count==len(self.nodes)
    def eulerian_path(self):
        path = []
        stack = []
        current = None
        if not self.is_eulerian():
            for vertex in self.nodes:
                if len(vertex.adjecent)%2==0:
                    current = vertex
                    break
        else:
            current = self.nodes[0]
        while len(current.adjecent)>0:
            if len(vertex.adjecent)==0:
                path.append(vertex.n)
            else:
                stack.append(vertex)
                to = list(vertex.adjecent)[0]
                vertex.adjecent.pop()
                print(self.nodes[to].adjecent)
                print(vertex.n)
                self.nodes[to].adjecent.remove(vertex.n)
                current = self.nodes[to]
        return path
class Node():
    def __init__(self, n):
        self.n = n
    adjecent = set()

def main():
    n, m = map(int, input().split(" "))
    while n != 0 and m != 0:
        graph = Graph([Node(n) for vertex in range(n)])
        for _ in range(m):
            from_, to = map(int, input().split(" "))
            graph.add_edge(from_, to)
        
        graph.print_graph()
        print(graph.eulerian_path())
        

if __name__ == "__main__":
    main()