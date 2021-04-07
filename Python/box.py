n = int(input('Width? '))
m = int(input('Height? '))
for row in range(m):
    for col in range(n):
        print('*' if row in(0,m-1) or col in(0,n-1) else ' ', end=' ')
    print()