BIG_NUMBER = 9999
STAMINA_COST = {'F': 2, 'M': 3}


def maybe_update(field1, field2, maze, time_taken, n, m, k, updated_places):
    i1, j1 = field1
    i2, j2 = field2
    if not (0 <= i2 < n and 0 <= j2 < m):
        # Out of bounds
        return
    field = maze[i2][j2]
    if field == '#':
        # Can not walk on river
        return
    days_taken, stamina_taken = time_taken[i1][j1]
    stamina_to_move = STAMINA_COST.get(field, 1)
    if stamina_taken > k:
        return
    stamina_taken += stamina_to_move
    if k < stamina_taken:
        days_taken += 1
        stamina_taken = stamina_to_move
    new_time_taken = (days_taken, stamina_taken)
    if new_time_taken < time_taken[i2][j2]:
        time_taken[i2][j2] = new_time_taken
        updated_places.add((i2, j2))


def main():
    # Read input
    n, m, k = map(int, input().split())
    maze = []
    for i in range(n):
        line = input()
        maze.append(line)

    # Create map of how long it takes to get somewhere, each field has (days_spend, stamina_spent)
    time_taken = []
    for i in range(n):
        time_taken.append([(BIG_NUMBER, BIG_NUMBER) for j in range(m)])

    # Look for the start and mark it as (0, 0), also look for the gold
    updated_fields = set()
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 'S':
                time_taken[i][j] = (1, 0)
                updated_fields.add((i, j))
            elif maze[i][j] == 'G':
                gold_at = (i, j)

    # BFS to propagate time_taken
    while updated_fields:
        i, j = updated_fields.pop()
        maybe_update((i, j), (i + 1, j), maze,
                     time_taken, n, m, k, updated_fields)
        maybe_update((i, j), (i - 1, j), maze,
                     time_taken, n, m, k, updated_fields)
        maybe_update((i, j), (i, j + 1), maze,
                     time_taken, n, m, k, updated_fields)
        maybe_update((i, j), (i, j - 1), maze,
                     time_taken, n, m, k, updated_fields)

    # Print days taken to get to the gold
    i, j = gold_at
    days_taken = time_taken[i][j][0]
    print(-1 if days_taken == BIG_NUMBER else days_taken)


if __name__ == '__main__':
    main()