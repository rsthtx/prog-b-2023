def move(source, destination):
    print(f"Flyt fra tårn: {source} til {destination}!")

def hanoi(n, source, helper, destination):
    spaces = "  ---  "+" "*(n+1)*2
    print(f"{spaces}call: hanoi({n}, {source}, {helper}, {destination})")
    if n == 0:
        print(f"Do nothing")
        pass
    else:
        hanoi(n-1, source, destination, helper)
        move(source,destination)
        hanoi(n-1, helper, source ,destination)

    print(f"{spaces}return: hanoi({n}, {source}, {helper}, {destination})")

hanoi(3, "A", "B", "C")