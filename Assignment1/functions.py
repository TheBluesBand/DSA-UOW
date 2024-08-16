class StringPoolWithCount:
    def __init__(self):
        self.pool = []

    def addToPool(self, word):
        for i, (count, existing_word) in enumerate(self.pool):
            if existing_word == word:
                self.pool[i] = (count + 1, word)
                return

        self.pool.append((1, word))

    def modify_tuple(self, index, new_tuple):
        self.pool[index] = new_tuple

    def access_tuple(self, index):
        #print(self.pool[index])
        #print(self.pool)
        tuple = self.pool[index]

        return tuple

    def get_count(self, index):
        print(self.pool[index])
        return self.pool[index][1]


    def __str__(self):
        strings = [str(item) for item in self.pool]
        return "".join(strings)
    
    def __len__(self):
        return len(self.pool)
    

def MakeHeap(array: StringPoolWithCount):
    
    for i in range (len(array) // 2, -1, -1):
        SiftDown(array,len(array), i)

    HeapSort(array)


def SiftDown(array, n, index):
    largest = index
    left_child = 2 * index + 1
    right_child = 2 * index + 2

    if (left_child >= n):
        return

    if left_child < n and array.access_tuple(left_child)[0] > array.access_tuple(largest)[0]:
        largest = left_child
    elif left_child < n and array.access_tuple(left_child)[0] == array.access_tuple(largest)[0] and array.access_tuple(left_child)[1] > array.access_tuple(largest)[1]:
        largest = left_child

    if right_child < n and array.access_tuple(right_child)[0] > array.access_tuple(largest)[0]:
        largest = right_child
    elif right_child < n and array.access_tuple(right_child)[0] == array.access_tuple(largest)[0] and array.access_tuple(right_child)[1] > array.access_tuple(largest)[1]:
        largest = right_child

    if largest != index:
        temp = array.access_tuple(largest)
        array.modify_tuple(largest, array.access_tuple(index))
        array.modify_tuple(index, temp)
        SiftDown(array, n, largest)

def HeapSort(array):
    n = len(array)
    for i in range (n // 2, -1, -1):
        SiftDown(array,len(array), i)

    for i in range(n - 1, 0, -1):
        #(array[i], array[0]) = (array[0], array[i]) 
        temp = (array.access_tuple(i))
        array.modify_tuple(i, array.access_tuple(0))
        array.modify_tuple(0, temp)
        SiftDown(array, i, 0)