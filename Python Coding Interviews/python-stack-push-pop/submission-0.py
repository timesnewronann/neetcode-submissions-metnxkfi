from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    reverse_list = []

    while len(arr) > 0:
        popped_item = arr.pop()
        reverse_list.append(popped_item)

    return reverse_list


# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
