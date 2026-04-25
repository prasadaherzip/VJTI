import time
import random

class MergeSort:

    def __init__(self):
        self.comparisons = 0
        self.swaps = 0   # interpreted as element moves/assignments

    def merge(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            self.comparisons += 1
            if left[i] <= right[j]:
                result.append(left[i])
                self.swaps += 1
                i += 1
            else:
                result.append(right[j])
                self.swaps += 1
                j += 1

        while i < len(left):
            result.append(left[i])
            self.swaps += 1
            i += 1

        while j < len(right):
            result.append(right[j])
            self.swaps += 1
            j += 1

        return result

    def sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.sort(arr[:mid])
        right = self.sort(arr[mid:])
        return self.merge(left, right)

    def run(self, arr):
        self.comparisons = 0
        self.swaps = 0

        start = time.perf_counter()
        sorted_arr = self.sort(arr)
        end = time.perf_counter()

        return sorted_arr, (end - start), self.comparisons, self.swaps


# -------- Test Driver --------

def test_case(name, arr):
    ms = MergeSort()
    _, t, c, s = ms.run(arr)
    return name, t, c, s


# Given Inputs
already = list(range(1, 26))
reverse = list(range(25, 0, -1))
random_order = [16,1,4,2,12,9,10,3,5,24,14,20,6,23,7,25,19,18,8,22,11,17,13,15,21]
nearly = [24,25] + list(range(3,24)) + [1,2]
single_end = list(range(2,26)) + [1]

large1 = random.sample(range(1,101), 100)
large2 = random.sample(range(1,401), 300)

cases = [
    ("Already Sorted", already),
    ("Reverse Sorted", reverse),
    ("Random Order", random_order),
    ("Nearly Sorted", nearly),
    ("Single Unsorted End", single_end),
    ("Large Input1", large1),
    ("Large Input2", large2)
]

print("Merge Sort Results:\n")
print("Input Type || Execution Time || Comparisons || Swaps")
print("-"*60)

for name, arr in cases:
    result = test_case(name, arr)
    print(f"{result[0]:20} {result[1]:.6f} sec   {result[2]:10}   {result[3]:10}")