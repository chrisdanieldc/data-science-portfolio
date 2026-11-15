"""
Sorting Algorithms Implementation
Demonstrates various sorting techniques for priority-based processing systems
Use Case: Medical scheduling, resource allocation, task prioritization
"""

## Insertion Sort
def insertionSort(ainstance):
    """
    Insertion Sort: Builds sorted array one item at a time
    Time Complexity: O(n^2)
    """
    for index in range(1, len(ainstance)):
        currentvalue = ainstance[index]
        position = index

        while position > 0 and ainstance[position-1] > currentvalue:
            ainstance[position] = ainstance[position-1]
            position = position - 1

        ainstance[position] = currentvalue


## Merge Sort
def mergeSort(alist):
    """
    Merge Sort: Divide and conquer algorithm
    Time Complexity: O(n log n)
    """
    print("Splitting ", alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1
    print("Merging ", alist)


## Quick Sort
def quickSort(alist):
    """
    Quick Sort: Efficient divide and conquer algorithm
    Time Complexity: O(n log n) average, O(n^2) worst case
    """
    quickSortHelper(alist, 0, len(alist)-1)


def quickSortHelper(alist, first, last):
    """Helper function for recursive quick sort"""
    if first < last:
        splitpoint = partition(alist, first, last)
        quickSortHelper(alist, first, splitpoint-1)
        quickSortHelper(alist, splitpoint+1, last)


def partition(alist, first, last):
    """Partition function for quick sort"""
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


## Selection Sort
def selectionSort(alist):
    """
    Selection Sort: Finds minimum element and places it at the beginning
    Time Complexity: O(n^2)
    """
    for fillslot in range(len(alist)-1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


## Shell Sort
def shellSort(alist):
    """
    Shell Sort: Generalized insertion sort with gap sequences
    Time Complexity: O(n^(3/2))
    """
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)

        print("After increments of size", sublistcount,
              "The list is", alist)

        sublistcount = sublistcount // 2


def gapInsertionSort(alist, start, gap):
    """Helper function for shell sort - insertion sort with gap"""
    for i in range(start + gap, len(alist), gap):
        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue


## Bubble Sort
def bubbleSort(alist):
    """
    Bubble Sort: Repeatedly swaps adjacent elements if in wrong order
    Time Complexity: O(n^2)
    """
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


# Demo and Testing
if __name__ == "__main__":
    print("=== Sorting Algorithms Demo ===\n")

    # Insertion Sort Demo
    print("1. Insertion Sort:")
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insertionSort(alist)
    print(f"Sorted: {alist}\n")

    # Merge Sort Demo
    print("2. Merge Sort:")
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    mergeSort(alist)
    print(f"Sorted: {alist}\n")

    # Quick Sort Demo
    print("3. Quick Sort:")
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quickSort(alist)
    print(f"Sorted: {alist}\n")

    # Selection Sort Demo
    print("4. Selection Sort:")
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    selectionSort(alist)
    print(f"Sorted: {alist}\n")

    # Shell Sort Demo
    print("5. Shell Sort:")
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    shellSort(alist)
    print(f"Sorted: {alist}\n")

    # Bubble Sort Demo
    print("6. Bubble Sort:")
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubbleSort(alist)
    print(f"Sorted: {alist}\n")
