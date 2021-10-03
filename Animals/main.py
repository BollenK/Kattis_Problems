def main():
    fw=input()
    animals_match=[]
    count={x:0 for x in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']}

    n = int(input())
    i =1
    while i<=n:
        na = input()
        count[na[0]]+=1
        if na[0] == fw[len(fw)-1]:
            animals_match.append(na)
        i+=1
    if len(animals_match)==0:
        print("?")
        return
    else:
        counter = 0
        while counter < len(animals_match):
            if (not count[animals_match[counter][len(animals_match[counter]) - 1]]) or animals_match[counter][0] == animals_match[counter][len(animals_match[counter]) - 1] and count[animals_match[counter][0]] == 1:
                print(animals_match[counter] + "!")
                return
            counter+=1

    print(animals_match[0])
if __name__ == "__main__":
    main()