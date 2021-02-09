array = [1, 5, 2, 6, 3, 9, 7, 8]
#array   0, 1, 2, 3, 4, 5, 6, 7

def sort(x):
    for i in range(0, len(x)):
        min = i
        for j in range(i+1, len(x)):
            if x[min] > x[j]:
                min = j
        x[i], x[min] = x[min], x[i]
        print(i)
    return x

l = sort(array)
print(l)
