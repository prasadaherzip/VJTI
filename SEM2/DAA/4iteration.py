import time
import random

def selection_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)

    start = time.perf_counter()

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1

    end = time.perf_counter()

    execution_time = end - start
    return execution_time, comparisons, swaps


def run_test(name, arr):
    arr_copy = arr.copy()
    time_taken, comparisons, swaps = selection_sort(arr_copy)

    print(name, "||", time_taken, "||", comparisons, "||", swaps)


print("\nIterative Selection Sort:")
print(f"{'Input Type':<35} {'Execution Time':<20} {'Total Comparisons':<20} {'Total Swaps':<15}")
print("-"*95)

def run_test(name, arr):
    arr_copy = arr.copy()
    time_taken, comparisons, swaps = selection_sort(arr_copy)

    print(f"{name:<35} {time_taken:<20.8f} {comparisons:<20} {swaps:<15}")


already_sorted = list(range(1,26))

reverse_sorted = list(range(25,0,-1))

random_order = [16,1,4,2,12,9,10,3,5,24,14,20,6,23,7,25,19,18,8,22,11,17,13,15,21]

nearly_sorted = [24,25,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,1,2]

single_unsorted = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,1]

large_input1 = random.sample(range(1,101),60)

large_input2 = random.sample(range(1,401),250)

run_test("Already Sorted", already_sorted)
run_test("Reverse Sorted", reverse_sorted)
run_test("Random Order", random_order)
run_test("Nearly Sorted", nearly_sorted)
run_test("Single Unsorted Element at End", single_unsorted)
run_test("Large Input1 (>50)", large_input1)
run_test("Large Input2 (>200)", large_input2)