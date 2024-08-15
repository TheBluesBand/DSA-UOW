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

    def access_first_element(self, index):
        return self.pool[index]

    def get_count(self, index):
        return self.pool[index][0]


    def __str__(self):
        strings = [str(item) for item in self.pool]
        return "".join(strings)
    
    def __len__(self):
        return len(self.pool)
    

def MakeHeap(array: StringPoolWithCount):
    for i in range (len(array) // 2, -1, -1):
        SiftDown(array, i)


def SiftDown(array, index):
    parent = index
    left_child = 2 * index + 1
    right_child = 2 * index + 2

    if (left_child >= len(array)):
        return
    
    if (right_child < len(array) and array.access_first_element(left_child) < array.access_first_element(right_child)):
        left_child = left_child + 1

    
    if (array.access_first_element(parent) < array.access_first_element(left_child)):
        temp = array.access_first_element(parent)
        array.modify_tuple(parent, array.access_first_element(left_child))
        array.modify_tuple(left_child, temp)
        SiftDown(array, left_child)