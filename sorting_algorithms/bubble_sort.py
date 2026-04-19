import random

def generate_random_array(size, lower_bound=0, upper_bound=100):
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]

def print_array(arr):
    print("Array:", arr)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1, 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

def print_sorted_array(arr):
    print("Sorted Array:", arr)

if __name__ == "__main__":
    arr = generate_random_array(25)
    print_array(arr)
    bubble_sort(arr)
    print_sorted_array(arr)
