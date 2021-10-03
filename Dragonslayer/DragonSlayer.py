def main():
    n, m = map(int, input().split(" "))
    while n != 0 and m != 0:
        nheads = sorted(list(map(int, [input() for x in range(n)])))
        mlength = sorted(list(map(int, [(input(), False) for x in range(m)])))
        i = j = 0
        costs = 0
        solvable = True
        while i < n and solvable:
            smallest = 20001
            found = False
            while j < m and not found:
                if mlength[j] >= nheads[i] and mlength[j] < smallest:
                    smallest = mlength[j]
                    found = True
                j += 1
            if smallest < 20001:
                costs += smallest
                mlength.remove(smallest)
                m -= 1
            elif smallest == 20001:
                print("Loowater is doomed!")
                solvable = False
            j = 0
            i += 1
        if solvable:
            print(costs)



        n, m = map(int, input().split(" "))


def psuedo():
    sort dragonsize
    smallest = 20001
    foreach dragonhead in dragonsize:
        sum = 0
        found = False
        i = [knights.length/2]
        while not found:
            if knights[i] == dragonhead and not knights[i]:
                knights[i] = True
                sum += kngihts[i]
            elif knights[i] <.....
            else:
                pass

if __name__ == "__main__":
    main()