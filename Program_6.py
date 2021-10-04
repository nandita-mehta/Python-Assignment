def divisibility(x):

    for i in range(0, x+1):
        if i % 5 == 0 or i % 7 == 0:
            yield i


n = int(input("Enter the number:"))
for i in divisibility(n):
    print(i, end=", ")
