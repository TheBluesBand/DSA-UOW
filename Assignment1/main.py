#read in a text file
import os
import string
from functions import StringPoolWithCount, MakeHeap

#try:
    #Create string pool
string_pool = StringPoolWithCount()

#Get file input through a prompt
input_file_name = input("Hello! Please input the file you want to read from: ")
#print(input_file_name)

#Try and open it
file_path = os.path.join(os.path.dirname(__file__), input_file_name)
file = open(file_path, 'r')

#Array to contain all inital words
words = []

#Loop through file and add elements to the stack
with file as f:
    for line in f:

        #Rewrite to not use .strip().lower().split() and iterate through them as char array
        line_temp = line.strip().lower().split()
        
        temp_string = ""
        for x in line_temp:
            for char in x:
                if char not in string.punctuation:
                    temp_string = temp_string + char
            #words.append(temp_string)
            string_pool.addToPool(temp_string)
            temp_string = ""

print()
MakeHeap(string_pool)

#print(string_pool)
i = 1
while i < 5:
    print(string_pool[-i])
    i += 1

#Close the file
file.close()
    
#except:
#    print("Invalid file name.\n")



#Display the words in a reverse order using a stack