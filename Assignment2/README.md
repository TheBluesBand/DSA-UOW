## Assessment 2 - CSCI203 - README

### Jake McCoy - 7161955

### Purpose

This Python script reads a text file, processes its contents, creates a priority queue (Using 3 Python Lists) and processes customers via tellers. This simulation finds a variety of statistics for us such as:

- **Customers served by each teller:** Shows how many customers were served by each given teller.
- **Total Time of Each Simuation:** How long did it take to run the similuation (Based of the first float in the input file)
- **Average Service Time per Customer:** The average time it took each customer to get processed
- **Average Waiting Time per Customer:** The average time it took a customer wait before they were processed.
- **Maximum Length of the Queue:** The maximum length of the queue during the simulation
- **Average Length of the Queue:** The average length of the queue during the simulation.
- **Average Idle Rate of Each Teller:** The average idle time for each of the Tellers during the simulation

### How It Works

1. **Import Necessary Modules:** Imports the `os` module. The file called `jjm419a2.py` contains all of the neccessary classes (`Teller`, `Customer`, `Queue`) and the functions (`allTellarsIdle`, `tellar_simulation`).

   - `os` was used to find the location of the inputed file after the user has inputted it.
   - `Teller` Represents a teller in the simulation environment.
   - `Customer` Represents a customer in the simulation environment.
   - `Queue` Represents a queue with three priority levels and records the maximum length of the queue.
   - `allTellarsIdle` Checks if all tellers in the given list are idle.
   - `tellar_simulation` Simulates a bank teller system based on customer arrivals, service times, and priorities. Once complete, the simulation statistics are printed to the terminal.

2. **Main Initalises:** Main runs and gets the users input for the number of tellers and the name of the input file. It then passes these values into `tellar_simulation(numberOfTellers, fileName)`
3. **Open File:** Opens the specified file in read mode with UTF-8 encoding. If the file name/path is invalid the script stops.
4. **Process File Content:**
   - Iterates through each line in the file.
   - Cleans the line by removing leading/trailing whitespace and splitting it into 3 values needed for the Customer Class (arrival, service, priority)
   - If the arrival & service values do not equal 0 then the customer is added to the customer array (Which we will use to iterate through when simulating the teller system)
5. **Intialise all the variables:** Creates and sets all the variables that are needed for the simulation to run and for all the statistics to be saved.
6. **Run simulation**: Run the simulation while their is still customers to serve or the tellers are not all idle.
   - Update the queue total time if needed
   - Enqueue customers that have arrived
   - Process tellars that have finished their service
   - Assign idle tellers to customers in the queue in round-robin fashion
     - Assign the teller to the next customer in the queue if they are not busy.
     - Calculate the wait time for the customer and update the statistics
     - Breaks the loop if a customer has been assigned
   - Update the simulation time to the next event time.
7. **Print Results:**
   - Prints number of customers served by each teller.
   - Prints the total time of the simulation
   - Prints the average service time per customer
   - Prints the average waiting time per customer
   - Prints the maximum length of the queue during the simulation
   - Prints the average length of the queue
   - Prints the average idle length of the queue

### Dependencies

- **os:** The only dependency required is you have the os library installed for python3 (Which should come preinstalled but if not run `pip3 install os`)
- **Python3 Version:** Make sure you are running the latest version of `Python3`. This code was tested on version `Python3 3.12.5`

### Complexity in Big O-Notation

This solution is O(1) as no matter the size of the queue it takes the same amount of time to Enqueue and Dequeue. However, some of the functions I have written are bigger.

- Enqueue O(1): Since appending to the end of a list is a constant-time operation no matter the length of the array my Enqueue is O(1)
- Dequeue O(1): Removing an element from the begining of a python list is a constant (As it is in python I do not require a double linked list unlike other languages such as C++) so this is O(1)
- Size O(1): The size operation utilises pythons `len()` function which stores the length of the dynamic array as part of pythons implementation. This means its a constant to get the length. So O(1)
- isEmpty O(1): For the same reasons as Size this complexity is 0(1)
- checkMaxLength O(1) or O(n): Updating the `maxLength` attribute after each enqueue operation might introduce a linear time complexity in the worst case, if the queue grows linearly. This is very unlikely to occur in implementation but is the worst possible outcome

#### Best Case O(1) and Absolute worst case O(n)

Overall all computations require O(1). There is potential for a linear complexity for how I have implemented `Enqueue` as everytime I call the function I also call `checkMaxLength` to appropriately record the largest length of the `Queue` Class.

### Data Structures Used: Priority Queue implemented with a List

In short I have created a priority queue to solve the queueing process for the tellers and customers. I also included priority as each customer had different levels of priority. This requires a priority queue then which I implemented using python `Lists`. Python lists are that languages inbuilt arrays which I used for underlying the data structure which is 3 lists one for each priority level so I can enqueue people and store based on priority. This removes the need for a sorting alrogithm as people are sorted once enqueued and that does not change when more people are added or removed (from dequeue)

### How to Run

1. Ensure that the input file is in the same directory as `jjm419a2`. For Assignment 2 of CSCI203 the input file is called `a2-sample.txt`
2. Run the script.

   **Option A**

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

   **Option B**

   - Open a terminal in the same directory as the `jjm419a2.py` and `a2-sample.txt` are in.
   - Type in the command `python3 jjm419a2.py`

3. Enter the number of tellers you want to run for the simulation and then name of the text file you want to analyse with the file extension.
   - WARNING: Only tested with files with .txt extensions
4. The script will process the file and display the simulation statistics in the terminal.

[comment]: <> (This README was created to provide the reasoning of this code and also how to run it. This will also be here to show people in the future my coding abilities if they are curious how I would solve a given problem)
