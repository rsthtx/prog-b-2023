# def hello():
#     print('Howdy!')
#     print('Howdy!!!')
#     print('Hello there.')


# hello()
# hello()
# hello()

def hello(name, lastname = "" ):
    full_name = name
    if lastname:
        full_name += " " + lastname
    print('Hello, ' + full_name)

hello('Alice')
hello('Bob')
hello('Jens','Hansen')