import time
import random


class RecursiveSelectionSort:

    def __init__(self):
        self.comparisons = 0
        self.swaps = 0

    def recursive_selection_sort(self, arr, n, index=0):
        if index >= n - 1:
            return

        min_index = index

        for j in range(index + 1, n):
            self.comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != index:
            arr[index], arr[min_index] = arr[min_index], arr[index]
            self.swaps += 1

        self.recursive_selection_sort(arr, n, index + 1)

    def run_test(self, input_type, arr):
        self.comparisons = 0
        self.swaps = 0

        arr_copy = arr.copy()

        start_time = time.perf_counter()
        self.recursive_selection_sort(arr_copy, len(arr_copy))
        end_time = time.perf_counter()

        execution_time = end_time - start_time

        print(f"{input_type:<35} {execution_time:<20.6f} {self.comparisons:<20} {self.swaps:<20}")


# Object creation
sorter = RecursiveSelectionSort()

print(f"{'Input Type':<35} {'Execution Time':<20} {'Comparisons':<20} {'Swaps':<20}")
print("-" * 95)

# Already Sorted
sorter.run_test("Already Sorted", list(range(1, 26)))

# Reverse Sorted
sorter.run_test("Reverse Sorted", list(range(25, 0, -1)))

# Random Order
sorter.run_test("Random Order",
                [16, 1, 4, 2, 12, 9, 10, 3, 5, 24, 14, 20, 6, 23, 7, 25, 19, 18, 8, 22, 11, 17, 13, 15, 21])

# Nearly Sorted
sorter.run_test("Nearly Sorted",
                [24, 25, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 1, 2])

# Single Unsorted Element at End
sorter.run_test("Single Unsorted End",
                list(range(2, 26)) + [1])

# Large Input 1 (>50)
large_input1 = random.sample(range(1, 500), 60)
sorter.run_test("Large Input (>50)", large_input1)

# Large Input 2 (>200)
large_input2 = random.sample(range(1, 1000), 250)
sorter.run_test("Large Input (>200)", large_input2)