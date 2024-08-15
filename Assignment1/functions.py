class StringPoolWithCount:
    def __init__(self):
        self.pool = []

    def addToPool(self, word):
        for i, (count, existing_word) in enumerate(self.pool):
            if existing_word == word:
                self.pool[i] = (count + 1, word)
                return

        self.pool.append((1, word))


    def __str__(self):
        print(self.pool)

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
