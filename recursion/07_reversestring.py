def reverse(s):
    if (len(s) == 1):
        return s
    ch = str(s[0])
    return reverse(s[1:]) + ch

def start():
    s = "abcdef"
    print(reverse(s))

start()