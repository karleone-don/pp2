
def gen(n):
    for i in range(1, n+1):
        yield i ** 2

num = int(input())
a = gen(num)
for i in range(num):
    print(next(a))
