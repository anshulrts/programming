def Convert(list, curr, multiple):
    if (len(list) == 1):
        return multiple * list[0]
    
    curr = multiple * int(list[-1])
    return curr + Convert(list[:-1], curr, multiple*10)

def start():
    list = [0, 2, 3, 4, 5]
    print(Convert(list, 0, 1))

if __name__ == '__main__':
    start()