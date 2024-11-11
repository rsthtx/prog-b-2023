# Eksempel 2: Sum af listeelementer
# Viser hvordan rekursion kan arbejde med lister
def sum_list(lst):
    # Basistilfælde
    if len(lst) == 0:
        return 0
    # Rekursivt tilfælde
    return lst[0] + sum_list(lst[1:])


my_list = [5, 12, 7, 1, 17]

result = sum_list(my_list)

print(result)
