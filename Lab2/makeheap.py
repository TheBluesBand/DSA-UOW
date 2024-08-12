def makeheap(array):
    length = len(array)
    for index in range(length // 2,0, -1):
        siftdown(array, index, length)

def siftdown(array, index, length):
    if array[index] is not None:
        largest = index
        left = 2 * index
        right = 2*index + 1
        if left <= length and array[left] > array[largest]:
            largest = left
        if right <= length and array[right] > array[largest]:
            largest = right

        if largest != index:
            array[index], array[largest] = array[largest], array[index]
            siftdown(array, largest, length)