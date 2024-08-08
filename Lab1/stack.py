#read in a text file
import os


loop = True

while(loop):
    try:
        #input_file_name = input("Hello! Please input the file you want to read from: ")
        #print('\n')
        #print(input_file_name)
        file_path = os.path.join(os.path.dirname(__file__), 'Ex1.txt')
        file = open(file_path, 'r')
        stack = []
        #print(len(stack))
        with file as f:
            for line in f:
                new_word = []
                for char in line:
                    if ((char != '\n') or (char != ' ')):
                        #print(char)
                        #Replace this += with a hand written function
                        new_word += char
                        print(new_word)
                    else:
                        stack.insert(len(stack), new_word)
                        print(new_word)
                        new_word = []
        file.close()

        #print(stack)
        #print(file.read())
        #while (len(stack) > 0):
        #    print(stack[-1])
        #    stack.pop()
        #print(stack)
        loop = False



        
    except:
        print("Invalid file name. Please try again\n")



#Display the words in a reverse order using a stack