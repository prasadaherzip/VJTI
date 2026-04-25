import time
import random

def insertion_sort(arr):
    comparisons = 0
    swaps = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Compare and shift
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                swaps += 1
                j -= 1
            else:
                break

        arr[j + 1] = key

    return comparisons, swaps


def test_case(arr):
    arr_copy = arr.copy()
    start = time.perf_counter()
    comparisons, swaps = insertion_sort(arr_copy)
    end = time.perf_counter()
∑w
    return (end - start), comparisons, swaps


# Test Inputs
test_cases = {
    "Already Sorted": list(range(1, 26)),
    "Reverse Sorted": list(range(25, 0, -1)),
    "Random Order": [16,1,4,2,12,9,10,3,5,24,14,20,6,23,7,25,19,18,8,22,11,17,13,15,21],
    "Nearly Sorted": [24,25,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,1,2],
    "Single Unsorted End": list(range(2, 26)) + [1],
    "Large Input1 (>50)": random.sample(range(1, 101), 60),
    "Large Input2 (>200)": random.sample(range(1, 1000), 250)
}

# Run Tests
print("Iterative Insertion Sort Results:\n")
print("Input Type || Execution Time || Comparisons || Swaps")
print("-"*65)

for name, arr in test_cases.items():
    time_taken, comp, swaps = test_case(arr)
    print(f"{name:20} || {time_taken:.6f} sec || {comp:10} || {swaps:10}")