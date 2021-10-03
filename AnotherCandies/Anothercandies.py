def is_divisible(n):
    total = 0
    for __ in range(n):
        total += int(input())%n
    return total%n == 0
def main():
    cases = int(input())
    for _ in range(cases):
        input()
        n = int(input())
        print("YES") if is_divisible(n) else print("NO")
if __name__ == "__main__":
    main()