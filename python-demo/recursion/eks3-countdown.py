# Eksempel 3: Nedtælling
# Et visuelt eksempel der er let at forstå
def count_down(n):
    # Basistilfælde
    if n <= 0:
        print("Lift off!")
        return
    # Rekursivt tilfælde
    print(n)
    count_down(n - 1)

count_down(7)