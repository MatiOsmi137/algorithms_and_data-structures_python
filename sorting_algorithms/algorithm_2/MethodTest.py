def Method1(n):
    if n == 0:
        return 1
    else:
        return n * Method1(n - 1)


def Method2(n):
    x = 1
    for i in range(1, n + 1):
        x *= i
    return x


print("Method1(5): " + str(Method1(5)))
print("Method2(5): " + str(Method2(5)))


def SortType(A):
    for j in range(0, len(A)):
        minpos = j
        for i in range(j + 1, len(A)):
            if A[i] < A[minpos]:
                minpos = i
        if minpos > j:
            intersave = A[minpos]
            A[minpos] = A[j]
            A[j] = intersave
        print(A)
    return A


def InsertionSort(arr):

    # Sortieralgorithmus hier implementieren!
    for j in range(0, len(arr)):
        key = arr[j]
        i = j-1
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key
        print(arr)
    return arr

A = [5, 2, 4, 3, 1]
SortType(A)

def is_stable(sorted_list, original_list):
    for i in range(1, len(sorted_list)):
        if sorted_list[i][0] == sorted_list[i - 1][0]:
            # If the keys are equal, check if their relative order is maintained
            if original_list.index(sorted_list[i]) < original_list.index(sorted_list[i - 1]):
                return "Nein"
    return "Ja"

# Test dataset
data = [(1, 'Ist'), (1, 'dieser'), (1, 'Algorythmus'), (1, 'stabil'), (1, '?')]

# Sort the dataset using the sorting algorithm
print('Ist Sortieralgorythmus 2 stabil?')
sorted_data1 = SortType(data)
print("Ist InsertionSort stabil?")
sorted_data2 = InsertionSort(data)

