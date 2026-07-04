from typing import List


def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    # append the elements of arr2 to the end of arr1 -> return the list
    for num in arr2:
        arr1.append(num)

    return arr1


def pop_n(arr: List[int], n: int) -> List[int]:
    # remove the last n elements from the list and return the resulting list

    # if n > len(list) -> return []
    if n > len(arr):
        return []

    for num in range(n):
        arr.pop()
    
    return arr


def insert_at(arr: List[int], index: int, element: int) -> List[int]:
    # insert the element at the specified index in the list -> return the list

    # if the index is index is out of bounds, insert at the end of the list
    if index > len(arr):
        arr.insert(len(arr), element)
    else:
        arr.insert(index, element)
    
    return arr


# do not modify below this line
print(append_elements([1, 2, 3], [4, 5, 6]))
print(append_elements([4, 3], [4, 5, 3]))

print(pop_n([1, 2, 3, 4, 5], 2))
print(pop_n([1, 2, 3, 4, 5], 6))
print(pop_n([1, 2, 3, 4, 5], 5))

print(insert_at([1, 2, 3, 4, 5], 2, 6))
print(insert_at([1, 2, 3, 4], 6, 5))
