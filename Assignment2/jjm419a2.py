import sys
import numpy

#I only use os to get the path of the input file to make sure its correct
import os

class Tellar:
    def __init__(self):
        self.isBusy = False
        self.item = ""

    def makeBusy(self, customer):
        print(customer)
        self.item = customer
        self.isBusy = True

    def checkBusy(self):
        print("nah")
        self.isBusy = False
        self.item = ""

class Queue:
    def __init__(self):
        #The basis of the queue will be a list
        self.p1 = []
        self.p2 = []
        self.p3 = []

    def enqueue(self, item):
        #Enqueue is adding two lists together using list comprehesion in python
        if item[-1] == 1:
            self.p1 = self.p1 + [item]
        elif item[-1] == 2:
            self.p2 = self.p2 + [item]
        elif item[-1] == 3:
            self.p3 = self.p3 + [item]
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
    tellars = [Tellar] * tellar_count
    queue = Queue
    print(tellars)

    #Read from the text file
    file_path = os.path.join(os.path.dirname(__file__), 'a2-sample.txt')
    file = open(file_path, 'r', encoding="utf-8")

    for line in file:
        #Allocate customer to a teller (if teller is idle)
        for tellar in tellars:
            allocated = False
            if tellar.isBusy() == False:
                print(line)
                allocated = True
        
        if allocated == False:
            queue.enqueue(line)


        #If everyone is busy then add to the qyeye

        #Update queue to move people in priority

        #If a tellar becomes free then pull the first person from the queue

        #End simulation when queue becomes empty and the last customer has left

if __name__ == "__main__":
    tellar_simulation(1)
    tellar_simulation(2)
    tellar_simulation(4)