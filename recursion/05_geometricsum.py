def sum(curr, n):
    if (curr == n):
        return 1/pow(3,curr)
    return 1/pow(3, curr) + sum(curr+1, n)


def start():
    n = 7
    print(sum(0, n))


if __name__ == '__main__':
    start()