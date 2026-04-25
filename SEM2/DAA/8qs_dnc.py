import random
import time

# Quick Sort with metrics
def quick_sort(arr):
    comparisons = 0
    swaps = 0

    def partition(a, low, high):
        nonlocal comparisons, swaps

        pivot_index = random.randint(low, high)
        a[pivot_index], a[high] = a[high], a[pivot_index]
        swaps += 1

        pivot = a[high]
        i = low - 1

        for j in range(low, high):
            comparisons += 1
            if a[j] < pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
                swaps += 1

        a[i+1], a[high] = a[high], a[i+1]
        swaps += 1

        return i + 1

    def qs(a, low, high):
        if low < high:
            pi = partition(a, low, high)
            qs(a, low, pi - 1)
            qs(a, pi + 1, high)

    qs(arr, 0, len(arr) - 1)
    return comparisons, swaps


def test_case(name, arr):
    arr_copy = arr.copy()

    start = time.time()
    comparisons, swaps = quick_sort(arr_copy)
    end = time.time()

    return (name, end - start, comparisons, swaps)


# Given Test Cases
already = list(range(1, 26))

reverse = list(range(25, 0, -1))

random_order = [16,1,4,2,12,9,10,3,5,24,14,20,6,23,7,25,19,18,8,22,11,17,13,15,21]

nearly = [24,25] + list(range(3,24)) + [1,2]

single_end = list(range(2,26)) + [1]

# Generated Inputs
large1 = [random.randint(1, 1000) for _ in range(60)]
large2 = [random.randint(1, 5000) for _ in range(250)]


cases = [
    ("Already Sorted", already),
    ("Reverse Sorted", reverse),
    ("Random Order", random_order),
    ("Nearly Sorted", nearly),
    ("Single Unsorted End", single_end),
    ("Large Input1", large1),
    ("Large Input2", large2)
]


# Output Format (as required)
print("Quick Sort:\n")
print("Input Type          ||   Execution time    ||   Total comparisons ||     Total swaps ||")
print("-"*90)

for name, arr in cases:
    result = test_case(name, arr)
    print(f"{result[0]:20} || {result[1]:.6f} sec        || {result[2]:18} || {result[3]:15} ||")