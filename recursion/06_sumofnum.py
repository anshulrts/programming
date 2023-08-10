def sum(num):
    if (num < 10):
        return num;
    
    return num%10 + sum(int(num/10))

def start():
    num = 123450
    print(sum(num))

start()