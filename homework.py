def even(start, n):
    count = []

    for i in range(start, start+n*2):
            if i % 2 == 0:
                count.append(i)
    return [count]

start = int(input("Enter the number where the even should start from:  "))
n = int(input("Enter the number of times you want to show the even numbers: "))
print(even(start, n))
