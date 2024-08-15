#read in a text file
import os
from makeheap import MakeHeap, print_heap

try:
    #Get file input through a prompt
    input_file_name = input("Hello! Please input the file you want to read from: ")
    #print(input_file_name)

    #Try and open it
    file_path = os.path.join(os.path.dirname(__file__), input_file_name)
    file = open(file_path, 'r')


    #Create my heap
    heap = [None] * 97
    index = 0

    #Loop through file and add elements to the stack
    with file as f:
        for line in f:
            heap[index] = int(line.strip())
            index += 1

    #Close the file
    #print(heap)
    file.close()
    
    

    MakeHeap(heap)
    #print(heap)

    i = 0
    while (i < 5):
        print(heap[i])
        i = i + 1

    #print_heap(heap)
    
except:
    print("Invalid file name.\n")



#Display the words in a reverse order using a stack