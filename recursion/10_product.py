def product(x, y):
    if (y == 1):
        return x
    return x + product(x, y-1)

def start():
    x = 5
    y = 6
    print(product(x, y))

start()