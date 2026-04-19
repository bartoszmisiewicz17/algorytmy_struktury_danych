import random

def generate_random_array(size, lower_bound=0, upper_bound=100):
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]


def print_array(arr):
    print("Array:", arr)


def merging_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merging_sort(arr[:mid])
    right_half = merging_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def print_sorted_array(arr):
    print("Sorted Array:", arr)

if __name__ == '__main__':
    arr = generate_random_array(25)
    print_array(arr)
    sorted_arr = merging_sort(arr)
    print_sorted_array(sorted_arr)
