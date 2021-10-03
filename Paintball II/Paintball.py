def main():
    playfieldsize = 10
    field = [ [ f"({x}, {y})" for x in range(playfieldsize)] for y in reversed(range(playfieldsize))]
    for row in field:
        for cell in row:
            print(cell, end="")
        print()
if __name__ == "__main__":
    main()