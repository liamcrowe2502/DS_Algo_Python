"""
Inserting Elements in an Array at the End
"""
def insert(arr, element):
    arr.append(element)

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    key = 6

    print("Before inserting: ")
    print(arr)

    insert(arr, key)
    print("After inserting: ")
    print(arr)

"""
Inserting Elements in an Array at any Position:
"""
def insertElementsAnyPos(arr, n, x, pos):
    for i in range(n - 1, pos - 1, -1):
        arr[i+1] = arr[i]

    arr[pos] = x


if __name__ == '__main__':
    arr = [11, 34, 26, 78, 34]
    n = 4

    print("Before insertion : ")
    for i in range(0, n):
        print(arr[i], end=' ')

    print("\n")

    x = 10
    pos = 2

    insertElementsAnyPos(arr, n, x, pos)
    n += 1

    print("After insertion : ")
    for i in range(0, n):
        print(arr[i], end=' ')

"""
Inserting Elements in a Sorted Array
"""
def insertSorted(arr, n, key, capacity):

    # Cannot insert more elements if n is
    # already more than or equal to capacity
    if (n >= capacity):
        return n

    i = n - 1
    while i >= 0 and arr[i] > key:
        arr[i + 1] = arr[i]
        i -= 1

    arr[i + 1] = key

    return (n + 1)


# Driver Code
if __name__ == "__main__":
    arr = [12, 16, 20, 40, 50, 70]

    for i in range(20):
        arr.append(0)

    capacity = len(arr)
    n = 6
    key = 26

    print("Before Insertion: ", end=" ")
    for i in range(n):
        print(arr[i], end=" ")

    # Function call
    n = insertSorted(arr, n, key, capacity)

    print("\nAfter Insertion: ", end=" ")
    for i in range(n):
        print(arr[i], end=" ")