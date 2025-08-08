
def find_smallest(array):
    smallest_number = array[0]
    smallest_index = 0
    for index in range(1, len(array)):
        if array[index] < smallest_number:
            smallest_number = array[index]
            smallest_index = index
    
    return smallest_index


def selection_sort(array):
    new_array = []
    for index in range(len(array)):
        smallest = find_smallest(array)
        new_array.append(array.pop(smallest))
    return new_array

print(selection_sort([7, 4, 1, 2, 9, 8, 15, 20, 12]))    