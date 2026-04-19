import random

def generate_random_array(size, lower_bound=0, upper_bound=100):
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]


def print_array(arr):
    print("Array:", arr)


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = key


def print_sorted_array(arr):
    print("Sorted Array:", arr)


if __name__ == '__main__':
    arr = generate_random_array(25)
    print_array(arr)
    selection_sort(arr)
    print_sorted_array(arr)
