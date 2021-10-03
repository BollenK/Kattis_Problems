if __name__ == "__main__":
    for _ in range(int(input())):
        x = int(input())
        print(f"{x} is even") if x % 2 == 0 else print(f"{x} is odd")