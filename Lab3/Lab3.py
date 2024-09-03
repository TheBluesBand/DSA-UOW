import sys
import numpy
import os

#Get file input from user
input_file_name = input("Please input file name: ")

try:
    #Try and open it
    file_path = os.path.join(os.path.dirname(__file__), input_file_name)
    file = open(file_path, 'r', encoding="utf-8")
except FileNotFoundError:
    print("File not found")

    
