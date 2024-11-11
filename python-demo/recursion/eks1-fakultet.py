# Eksempel 1: Fakultet
# Et klassisk og intuitivt eksempel på rekursion
def fakultet(n):
    # Basistilfælde
    if n == 0 or n == 1:
        return 1
    # Rekursivt tilfælde
    return n * fakultet(n - 1)


# Kørsel
result = fakultet(4)
print(result)