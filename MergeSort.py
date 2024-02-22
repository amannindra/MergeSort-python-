import random

numbers_to_sort1 = []
numbers_to_sort2 = []


def get_unique_random_numbers(range_start, range_end, count):
    number = []
    if count > (range_end - range_start + 1):
        raise ValueError(
            "Count is larger than the range of unique numbers available.")

    numbers_given = set()
    while len(numbers_given) < count:
        num = random.randint(range_start, range_end)
        if num not in numbers_given:
            numbers_given.add(num)
            number.append(num)
    return number
# hi


start = 1
end = 100
count = 30

numbers_to_sort1 = get_unique_random_numbers(start, end, count)
numbers_to_sort2 = get_unique_random_numbers(start, end, count)


def merge(array):
    if len(array) > 1:
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]
        merge(left)
        merge(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    return array


def merge2d(array1, array2):
    return merge(array1 + array2)


print(merge(numbers_to_sort1))
print(merge2d(numbers_to_sort1, numbers_to_sort2))
