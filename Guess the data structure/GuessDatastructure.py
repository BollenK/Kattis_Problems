import heapq, sys
def throwin(q,s,h,x, results):
    if results[0]:
        q.append(x)
    if results[1]:
        s.append(x)
    if results[2]:
        heapq.heappush(h, -x)
    return (q,s ,h )
def printstructures(l):
    for j in l:
        if j[0] and j[1] or j[0] and j[2] or j[1] and j[2]:
            print("not sure")
        elif not j[0] and not j[1] and not j[2]:
            print("impossible")
        elif j[0]:
            print("queue")
        elif j[1]:
            print("stack")
        else:
            print("priority queue")
def main():
    results_global = []
    stackops = []
    current = []
    while True:
        try:
            line = input()
            if len(line) == 1:
                if len(current) != 0:
                    stackops.append(current)
                current = []
            else:
                current.append(tuple(map(int, line.split(" "))))
        except EOFError:
            break
    stackops.append(current)
    for op in stackops:
        q,s,h = [],[],[]
        heapq._heapify_max(h)
        results = [True, True, True]
        for i in range(len(op)):
            o, x = op[i]
            if o == 1:
                q,s,h = throwin(q,s,h,x, results)
            else:
                if len(q) == 0 or q[0] != x:
                    results[0] = False
                else:
                    q.pop(0)
                if len(s) == 0 or s[-1] != x:
                    results[1] = False
                else:
                    s.pop()
                if len(h) == 0 or h[0] != -x :
                    results[2] = False
                else:
                    heapq.heappop(h)
            if i == len(op)-1:
                results_global.append(results)
    printstructures(results_global)
if __name__ == "__main__":
    main()