def AddElem(arr, n):
    if n == 1:
        return arr[0]
    
    return arr[n-1] + AddElem(arr[0:n-1] ,n-1)

def start():
    ls = [1, 2, 3, 4, 5]
    print(f'Sum is {AddElem(ls, len(ls))}')
    #print(AddElem.__annotations__)

if __name__ == '__main__':
    start();