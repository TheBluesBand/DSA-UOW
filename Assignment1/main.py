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
                if char not in string.punctuation and char.isalpha():
                    temp_string = temp_string + char
            #words.append(temp_string)
            string_pool.addToPool(temp_string)
            temp_string = ""

#print()
MakeHeap(string_pool)

#print(string_pool)
i = 1
print("The first 10 words sorted alphabetically within frequency:")
while i < 11:
    print("The word: " + str(string_pool.access_tuple(-i)[1]) + " occurs " + str(string_pool.access_tuple(-i)[0]) + " times.")
    i += 1


i = 0
print("\nThe last 10 words sorted alphabetically within frequency:")
while i < 10:
    print("The word: " + str(string_pool.access_tuple(i)[1]) + " occurs " + str(string_pool.access_tuple(i)[0]) + " times.")
    i += 1


print('\nThe unique words sorted alphabetically:')
while i < len(string_pool):
    if (string_pool.access_tuple(i)[0] == 1):
        print("The word: " + str(string_pool.access_tuple(i)[1]) + " occurs " + str(string_pool.access_tuple(i)[0]) + " times.")

    i += 1

#Close the file
file.close()
    
#except:
#    print("Invalid file name.\n")



#Display the words in a reverse order using a stack