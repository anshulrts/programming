def dtob(n):
    if (n == 0):
        return
    val = n%2
    n = n//2
    dtob(n)
    print(val, end="")

def start():
    n = 294
    dtob(n)

start()