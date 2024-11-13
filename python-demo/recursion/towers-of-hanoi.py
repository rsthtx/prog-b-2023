def move(source, destination):
    print(f"Flyt fra tårn: {source} til {destination}!")

def hanoi(n, source, helper, destination):
    if n == 0:
        pass
    else:
        hanoi(n-1, source, destination, helper)
        move(source,destination)
        hanoi(n-1, helper, source ,destination)

hanoi(3, "Lineal", "Saks", "Blyantspidser")