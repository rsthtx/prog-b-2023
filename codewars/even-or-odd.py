# Kata: https://www.codewars.com/kata/53da3dbb4a5168369a0000fe/train/python

def even_or_odd(number):
    if number % 2 == 0:
        return "even"
    
    return "odd"


# local testing
if __name__ == "__main__":
    for n in range(-5, 6):
        print(n, even_or_odd(n))


