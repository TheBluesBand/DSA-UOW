## Assessment 1 - CSCI203 - README
### Jake McCoy - 7161955

### Purpose
This Python script reads a text file, processes its contents, creates a heap and sorts the max heap based on the amount of times the word appeard and then the alphabetical nature of the word. This is for Assessment 1 of the UOW course CSCI203. The requirements include (but are not limited too):

* **Word Frequency:** Calculates the frequency of each word in the file using a custom String Pool Class.
* **Word Sorting:** Sorts words by their frequency in ascending (If the frequency is the same then it goes to alphabetical comparisons).
* **Unique Words:** Identifies and lists unique words (words that appear only appear once in the given file).

### How It Works
1. **Import Necessary Modules:** Imports the `os`, `string`, and `functions` modules. The `functions` module containing implementations of the `StringPoolWithCount` and `MakeHeap` classes which were made for this assessment.
   * `os` was used to find the location of the inputed file after the user has inputted it.
   * `string` was used as it contains a library of all punctuation accessible using `string.punctuation` so I did not have to create my own list of punctuation.
   * `functions` is a file containing all of the functions I had to implement myself for this assessment.
2. **Create String Pool:** Initialises a `StringPoolWithCount` object to store words and their frequencies. This was to help speed up the sorting process for the sorting required by the assessment. This is used in the `SiftDown` functions within the `functions` module.
3. **Get File Input:** Prompts the user to enter the name of the text file to be processed.
4. **Open File:** Opens the specified file in read mode with UTF-8 encoding. If the file name/path is invalid the script stops.
5. **Process File Content:**
   * Iterates through each line in the file.
   * Cleans the line by removing leading/trailing whitespace, converting to lowercase letters (if they are upper case letters present), and splitting the line into individual words (resulting in an array of words).
   * For each word:
     * Removes punctuation and non-alphabetic characters.
     * Adds the cleaned word to the string pool. Using a linear search we see if the word is already in the pool (we then increase the count by 1) otherwise we add the new word to the bottom of the pool.
6. **Create & Sort Heap:** Constructs a heap data structure using the `MakeHeap` function which I implemented. The script then using a Heap Sort to then sort the Heap to find the words that occur the most to the words that occur the least (and alphabetically are last)
7. **Print Results:**
   * Prints the top 10 most frequent words from the given file.
   * Prints the bottom 10 least frequent words from the given file. 
   * Prints the unique words in the file (any word with a frequency of 1).

### Dependencies
* **functions.py:** This module contains the definitions/implementations for the `StringPoolWithCount` and `MakeHeap` classes. These were made specifically for this assessment as we needed to show our understanding of these concepts
   - `StringPoolWithCount` is a class which is an array of tuples to store the Word Frequency & then the word iteslf.
   - `MakeHeap` is function that takes in the StringPoolWithCount class and creates a max heap using a sift down function (Which I implemented). This then calls the `HeapSort` function to sort the function from most frequent words to least frequent (also taking into account the alphabetical ordering of the word if they have the same frequency)

### Complexity in Big O-Notation
If we ignore the 'preprocessing' of data (Removing numbers, punctuation and turning upper case to lower case) I have two major algorithms. Linear Search for inputting the words into the string pool and then making/sorting the heap

#### Linear Search for String Pool - O(n)
A linear search at worst is O(n) as we would have to check every value in the current string pool to make sure the new word is not there. This is because we check every value until we find the value in the array. This is only as bad as the length of the array

#### Max Heap + Heap Sort - O(nlogn)
The creation of the max heap and then using Heap Sort to sort the heap. Each extraction and recreating of the heap (using siftdown) takes O(logn) times and its need O(n) times. This step takes O(nlogn) complexity using this logic.

#### Total Complexity O(n) + O(nlogn)
Since I use a Linear Search and then the Heap Sort algorithms I end up with the complexity of O(n) + O(nlogn)

### How to Run
1. Ensure that the `functions.py` module is in the same directory as this script.
2. Run the script. 
   - I am using the Python extension in VSCode to run this script. This allows for a button in the top right which will run the file open in the editor.
   - The extension information is below if you want to follow how I did it: 
<table style="padding: 20px">
    <tr>
        <td>
           Python <br />
            Id: ms-python.python <br />
            Description: Python language support with extension access points for IntelliSense (Pylance), Debugging (Python Debugger), linting, formatting, refactoring, unit tests, and more. <br />
            Version: 2024.12.3 <br />
            Publisher: Microsoft <br />
            VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=ms-python.python <br />
        </td>
    </tr>
</table>

3. Enter the name of the text file you want to analyse with the file extension.
   - WARNING: Only tested with files with .txt extensions 
4. The script will process the file and display the results in the terminal.

[comment]: <> (This README was created to provide the reasoning of this code and also how to run it. This will also be here to show people in the future my coding abilities if they are curious how I would solve a given problem)