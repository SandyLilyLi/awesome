from attri import Fjs
def countdown(n):
    print("Counting down from", n)
    while n > 0:
        yield n
        print("in countdown: ",n)
        n -= 1
    print ("Done counting down")

# Example use
if __name__ == '__main__':
    x=countdown(10)
    print(x)
    next(x)
    next(x)

