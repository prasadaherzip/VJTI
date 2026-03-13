import time
import random

# Global counters
comparisons = 0
swaps = 0

def recursive_insertion_sort(arr, n):
    global comparisons, swaps

    if n <= 1:
        return

    # Sort first n-1 elements
    recursive_insertion_sort(arr, n-1)

    last = arr[n-1]
    j = n-2

    # Insert last element at correct position
    while j >= 0:
        comparisons += 1
        if arr[j] > last:
            arr[j+1] = arr[j]
            swaps += 1
            j -= 1
        else:
            break

    arr[j+1] = last


def run_test_case(name, arr):
    global comparisons, swaps

    comparisons = 0
    swaps = 0

    arr_copy = arr.copy()

    start = time.perf_counter()
    recursive_insertion_sort(arr_copy, len(arr_copy))
    end = time.perf_counter()

    execution_time = end - start

    print(f"{name:<30} || {execution_time:<18.8f} || {comparisons:<18} || {swaps:<12}")


# Test cases
already_sorted = list(range(1, 26))

reverse_sorted = list(range(25, 0, -1))

random_order = [16, 1, 4, 2, 12, 9, 10, 3, 5, 24, 14, 20, 6, 23, 7, 25, 19, 18, 8, 22, 11, 17, 13, 15, 21]

nearly_sorted = [24, 25] + list(range(3, 24)) + [1, 2]

single_unsorted_end = list(range(2, 26)) + [1]

large_input1 = random.sample(range(1, 101), 60)

large_input2 = random.sample(range(1, 501), 250)


print("Recursive Insertion Sort:")
print("Input Type                     || Execution Time (s)  || Total Comparisons || Total Swaps")
print("--------------------------------------------------------------------------------------------")

run_test_case("Already Sorted", already_sorted)
run_test_case("Reverse Sorted", reverse_sorted)
run_test_case("Random Order", random_order)
run_test_case("Nearly Sorted", nearly_sorted)
run_test_case("Single Unsorted Element End", single_unsorted_end)
run_test_case("Large Input (>50)", large_input1)
run_test_case("Large Input (>200)", large_input2)