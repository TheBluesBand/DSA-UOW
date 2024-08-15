import math

def MakeHeap(array):
    for i in range (len(array) // 2, -1, -1):
        SiftDown(array, i)

    #print(array)

def SiftDown(array, index):
    parent = index
    left_child = 2 * index + 1
    right_child = 2 * index + 2
    if (left_child >= len(array)):
        return
    
    if (right_child < len(array) and array[left_child] < array[right_child]):
        left_child = left_child + 1

    if (array[parent] < array[left_child]):
        array[parent], array[left_child] = array[left_child], array[parent]

        SiftDown(array, left_child)



def print_heap(heap):
    """Prints a heap in a level-order traversal format."""
    height = int(math.log2(len(heap))) + 1
    for level in range(height):
        start_index = 2**level - 1
        end_index = min(2**(level + 1) - 1, len(heap))
        level_str = " ".join(str(heap[i]) for i in range(start_index, end_index))
        print(level_str.center(2**(height + 1) - 1))
    