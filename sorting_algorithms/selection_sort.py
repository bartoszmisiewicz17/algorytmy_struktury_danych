import random

def generate_random_array(size, lower_bound=0, upper_bound=100):
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]

def print_array(arr):
    print("Array:", arr)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range (i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def print_sorted_array(arr):
    print("Sorted Array:", arr)

if __name__ == "__main__":
    arr = generate_random_array(25)
    print_array(arr)
    selection_sort(arr)
    print_sorted_array(arr)
