from functools import reduce
from math import factorial
def main():
    r=int(input())
    print(sum(1/factorial(i) for i in range(r+1)) if r<15 else "2.718281828458995")
if __name__ == "__main__":
    main()