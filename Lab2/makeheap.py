import math

def MakeHeap(array):
    for i in range (len(array) // 2, -1, -1):
        SiftDown(array, len(array), i)

    for i in range(len(array) - 1, 0, -1):
        array[i], array[0] = array[0], array[i]  # swap
        SiftDown(array, i, 0)

    print(array)

def SiftDown(array, len, index):
    largest = index
    left_child = 2 * index + 1
    right_child = 2 * index + 2

    if left_child < len and array[left_child] > array[largest]:
        largest = left_child

    if right_child < len and array[right_child] > array[largest]:
        largest = right_child

    if largest != index:
        array[index], array[largest] = array[largest], array[index]
        SiftDown(array, len, largest)

def HeapSort(array):
    n = len(array)
    
    for i in range(n - 1, 0, -1):
        (array[i], array[0]) = (array[0], array[i]) 

    SiftDown(array, i, 0)



def print_heap(heap):
    """Prints a heap in a level-order traversal format."""
    height = int(math.log2(len(heap))) + 1
    for level in range(height):
        start_index = 2**level - 1
        end_index = min(2**(level + 1) - 1, len(heap))
        level_str = " ".join(str(heap[i]) for i in range(start_index, end_index))
        print(level_str.center(2**(height + 1) - 1))
    