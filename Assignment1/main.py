#read in a text file
import os
import string
from functions import StringPoolWithCount, MakeHeap

try:
    #Create string pool
    string_pool = StringPoolWithCount()

    #Get file input through a prompt (Step 1)
    input_file_name = input("Hello! Please input the file you want to read from: ")

    #Try and open it
    file_path = os.path.join(os.path.dirname(__file__), input_file_name)
    file = open(file_path, 'r', encoding="utf-8")

    #Loop through file and add elements to the string pool (Step 2)
    with file as f:
        for line in f:

            #I talked to Dr Xueqiao Liu in the Thursday tutorial and she said this was fine
            #as it was just pre prossessing
            line_temp = line.strip().lower().split()
            
            temp_char_array = []
            for x in line_temp:
                for char in x:
                    if char not in string.punctuation and char.isalpha():
                        temp_char_array.append(char)
                string_pool.addToPool(temp_char_array)
                temp_char_array = []

    MakeHeap(string_pool)

    i = 1
    print("The first 10 words sorted alphabetically within frequency:")
    while i < 11:
        print("The word: " + "".join(string_pool.access_tuple(-i)[1]) + " occurs " + str(string_pool.access_tuple(-i)[0]) + " times.")
        i += 1


    i = 10
    print("\nThe last 10 words sorted alphabetically within frequency:")
    while i != 0:
        print("The word: " + "".join(string_pool.access_tuple(i-1)[1]) + " occurs " + str(string_pool.access_tuple(i-1)[0]) + " times.")
        i -= 1

    i = 1
    print('\nThe unique words sorted alphabetically:')
    while i < len(string_pool) + 1:
        if (string_pool.access_tuple(-i)[0] == 1):
            print("The word: " + "".join(string_pool.access_tuple(-i)[1]) + " occurs " + str(string_pool.access_tuple(-i)[0]) + " times.")

        i += 1

    file.close()
        
except:
    print("Invalid file name.\n")
