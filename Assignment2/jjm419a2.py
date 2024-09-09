import sys
#import numpy
import time

#I only use os to get the path of the input file to make sure its correct
import os

class Tellar:
    def __init__(self):
        self.isBusy = False
        self.item = ""
        self.count = 0

    def makeBusy(self, customer):
        print(customer)
        self.item = customer
        self.isBusy = True
        self.count += 1

    def checkBusy(self):
        print("nah")
        self.isBusy = False
        self.item = ""

    def checkBusy(self):
        return self.isBusy == True


class Queue:
    def __init__(self):
        #The basis of the queue will be a list
        #Each list will have a associated count to find max length
        self.p1 = []
        self.p1MaxLength = 0

        self.p2 = []
        self.p2MaxLength = 0

        self.p3 = []
        self.p3MaxLength = 0

    def enqueue(self, item):
        item.strip()
        #Enqueue is adding two lists together using list comprehesion in python
        if item[-1] == 1:
            self.p1 = self.p1 + [item]
            if len(self.p1 > self.p1MaxLength):
                self.p1MaxLength = len(self.p1)
        elif item[-1] == 2:
            self.p2 = self.p2 + [item]
            if len(self.p2 > self.p2MaxLength):
                self.p2MaxLength = len(self.p2)
        elif item[-1] == 3:
            self.p3 = self.p3 + [item]
            if len(self.p3 > self.p3MaxLength):
                self.p3MaxLength = len(self.p3)
        else:
            print("Out of bounds priority " + item[-1])

    def dequeue(self, item):
        #Dequeue uses the list comprehension to remove the first element and save the list
        if item[-1] == 1:
            self.p1 = self.p1[1:]
        elif item[-1] == 2:
            self.p2 = self.p2[1:]
        elif item[-1] == 3:
            self.p3 = self.p3[1:]
        else:
            print("Out of bounds priority " + item[-1])

    def is_empty(self):
        #Check if list is empty. Return result
        return len(self.p1) == 0 and len(self.p2) == 0 and len(self.p3) == 0

def tellar_simulation(tellar_count):
    #Set total number of tellars
    tellars = [Tellar() for _ in range(tellar_count)]

    queue = Queue()

    #Read from the text file
    file_path = os.path.join(os.path.dirname(__file__), 'a2-sample.txt')
    file = open(file_path, 'r', encoding="utf-8")

    start_time = time.time()
    

    for line in file:
        #Allocate customer to a teller (if teller is idle)
        for tellar in tellars:
            allocated = False
            if tellar.isBusy == False:
                print(line)
                tellar.makeBusy(line)
                allocated = True
                break
        
        #If everyone is busy then add to the qyeye

        if allocated == False:
            queue.enqueue(line)

        #If a tellar becomes free then pull the first person from the queue

        #End simulation when queue becomes empty and the last customer has left

    end_time = time.time()

if __name__ == "__main__":
    tellar_simulation(1)
    tellar_simulation(2)
    tellar_simulation(4)