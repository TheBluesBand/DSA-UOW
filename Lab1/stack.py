#read in a text file
import os
from jakeStack import *

loop = True

while(loop):
    try:
        #Get file input through a prompt
        input_file_name = input("Hello! Please input the file you want to read from: ")
        #print(input_file_name)

        #Try and open it
        file_path = os.path.join(os.path.dirname(__file__), 'Ex1.txt')
        file = open(file_path, 'r')


        #Create my stack
        stack = JakeStack()

        #Loop through file and add elements to the stack
        with file as f:
            for line in f:
                new_word = []
                words = line.split()

                for x in words:
                    stack.Push(x)

        #Close the file
        file.close()

        while(stack.isEmpty()):
            print(stack.Top(), end=" ")
            stack.Pop()

        loop = False

        #stack.exercise()

        
    except:
        print("Invalid file name. Please try again\n")



#Display the words in a reverse order using a stack