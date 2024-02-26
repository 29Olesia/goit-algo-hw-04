import timeit
import random
from prettytable import PrettyTable
import matplotlib.pyplot as plt

def insertion_sort(lst_):
    lst = lst_[:]
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def test_algorithm(algorithm, data):
    stmt = f"{algorithm}({data.copy()})"
    time = timeit.timeit(stmt, number=10, globals=globals())
    return time

def print_results(label, small, medium, large):
    table = PrettyTable()
    table.field_names = ["Algorithm", "Small", "Medium", "Large"]
    table.add_row([label, f"{small:.8f}", f"{medium:.8f}", f"{large:.8f}"])
    print(table)

# Generate larger test data
data_small = [random.randint(0, 1_000) for _ in range(100)]
data_medium = [random.randint(0, 10_000) for _ in range(1_000)]
data_large = [random.randint(0, 100_000) for _ in range(10_000)]

# Test the sorting time for each algorithm on different data sizes
insertion_sort_time_small = test_algorithm("insertion_sort", data_small)
insertion_sort_time_medium = test_algorithm("insertion_sort", data_medium)
insertion_sort_time_large = test_algorithm("insertion_sort", data_large)

merge_sort_time_small = test_algorithm("merge_sort", data_small)
merge_sort_time_medium = test_algorithm("merge_sort", data_medium)
merge_sort_time_large = test_algorithm("merge_sort", data_large)

sorted_time_small = test_algorithm("sorted", data_small)
sorted_time_medium = test_algorithm("sorted", data_medium)
sorted_time_large = test_algorithm("sorted", data_large)

list_sort_time_small = test_algorithm("sorted", data_small)
list_sort_time_medium = test_algorithm("sorted", data_medium)
list_sort_time_large = test_algorithm("sorted", data_large)

# Display the results in a formatted way
print_results("Insertion Sort", insertion_sort_time_small, insertion_sort_time_medium, insertion_sort_time_large)
print_results("Merge Sort", merge_sort_time_small, merge_sort_time_medium, merge_sort_time_large)
print_results("Sorted", sorted_time_small, sorted_time_medium, sorted_time_large)
print_results("List Sort", list_sort_time_small, list_sort_time_medium, list_sort_time_large)

# Create and display bar charts
labels = ["Insertion Sort", "Merge Sort", "Sorted", "List Sort"]
small_data = [insertion_sort_time_small, merge_sort_time_small, sorted_time_small, list_sort_time_small]
medium_data = [insertion_sort_time_medium, merge_sort_time_medium, sorted_time_medium, list_sort_time_medium]
large_data = [insertion_sort_time_large, merge_sort_time_large, sorted_time_large, list_sort_time_large]

# Bar chart for small dataset
plt.figure(figsize=(10, 5))
plt.bar(labels, small_data, color='blue', alpha=0.7)
plt.title("Sorting Algorithm Performance - Small Dataset")
plt.xlabel("Algorithm")
plt.ylabel("Time (seconds)")
plt.show()

# Bar chart for medium dataset
plt.figure(figsize=(10, 5))
plt.bar(labels, medium_data, color='green', alpha=0.7)
plt.title("Sorting Algorithm Performance - Medium Dataset")
plt.xlabel("Algorithm")
plt.ylabel("Time (seconds)")
plt.show()

# Bar chart for large dataset
plt.figure(figsize=(10, 5))
plt.bar(labels, large_data, color='red', alpha=0.7)
plt.title("Sorting Algorithm Performance - Large Dataset")
plt.xlabel("Algorithm")
plt.ylabel("Time (seconds)")
plt.show()
