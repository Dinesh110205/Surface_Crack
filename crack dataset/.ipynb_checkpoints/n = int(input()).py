n = int(input())
m = int(input())
a = []

if n > 0 and m > 0:
    for i in range(n):
        row = []
        for j in range(m):
            element = int(input())
            row.append(element)
            
        a.append(row)

    for i in range(n):
        for j in range(m):
            print(a[i][j], end=" ")
        print()
else:
    print("Row size and column size cannot be negative")


