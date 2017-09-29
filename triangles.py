def triangles(max):
    n = 1
    L = [1]
    while n <= max:
        yield L
        L = [1] + [L[n] + L[n + 1] for n in range(len(L) - 1)] + [1]
        n = n + 1
    return 'done'

for i in triangles(5):
    print(i)
