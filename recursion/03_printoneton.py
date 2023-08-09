def printoneton(n):
    if (n == 0):
        return
    printoneton(n-1)
    print(n, end=' ')

def start():
    prompt = "Enter Number : "
    n = int(input(prompt))
    printoneton(n)

if __name__ == '__main__':
    start()