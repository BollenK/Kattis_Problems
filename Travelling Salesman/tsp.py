import sys as sys

def dist(p1, p2):
    return abs((p2[1] - p1[1]) / (p2[0] - p1[0])) if (p2[0] - p1[0]) != 0 else 0
def minKey(n, key, mstSet):
        # Initialize min value
    min = sys.maxsize
    min_index = None
    for v in range(n):
        if key[v] < min and mstSet[v] == False:
            min = key[v]
            min_index = v

    return min_index
def primMST(n, graph):
 
    # Key values used to pick minimum weight edge in cut
    key = [sys.maxsize] * n
    parent = [None] * n # Array to store constructed MST
    # Make key 0 so that this vertex is picked as first vertex
    key[0] = 0
    mstSet = [False] * n
    print(mstSet)
    parent[0] = -1 # First node is always the root of

    for _ in range(n):

        # Pick the minimum distance vertex from
        # the set of vertices not yet processed.
        # u is always equal to src in first iteration
        u = minKey(n, key, mstSet)

        # Put the minimum distance vertex in
        # the shortest path tree
        print(u)
        mstSet[u] = True

        # Update dist value of the adjacent vertices
        # of the picked vertex only if the current
        # distance is greater than new distance and
        # the vertex in not in the shortest path tree
        for v in range(n):

            # graph[u][v] is non zero only for adjacent vertices of m
            # mstSet[v] is false for vertices not yet included in MST
            # Update the key only if graph[u][v] is smaller than key[v]
            if graph[u][v] > 0 and mstSet[v] == False and key[v] > graph[u][v]:
                    key[v] = graph[u][v]
                    parent[v] = u
    return parent
def main():

    n = int(input())
    V = [*range(1, n + 1)]

    l = [tuple(map(lambda p: float(p), input().split(" ") )) for n in range(n)]
    G = [[dist(l[i], l[j]) if j!=n else 0 for j in range(n) ] for i in range(n)]
    # print(G) 
    # return

    mst = primMST(n, G)
    print(mst)
    # While loop for efficiency
    for i in range(n):
        print(mst[i], "-", i, "\t", G[i][ mst[i] ])


    # print(G)




if __name__ == "__main__":
    main()