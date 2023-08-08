def fact(n):
    if n == 1:
        return 1;

    return n * fact(n-1);

def start():
    n = 6;
    print(f"Factorial is : {fact(n)}");

if __name__ == '__main__':
    start();