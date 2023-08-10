def prime(n, i):
    if (i == 1):
        return True
    elif (n%i == 0):
        return False
    return prime(n, i-1)

def start():
    n = 10
    print(prime(n, int(n/2)+1))

start()