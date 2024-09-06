import sys
import numpy
import os

class Tellar:
    def __init__(self):
        self.isBusy = False

    def makeBusy(self, customer):
        print(customer)
        self.isBusy = True

    def checkBusy(self):
        print("nah")

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue = self.queue + [item]

    def dequeue(self):
        self.queue = self.queue[1:]

    def is_empty(self):
        return len(self.queue) == 0

def tellar_simulation(tellar_count):
    #Set total number of tellars
    tellars = tellar_count

    #Read from the text file
    file_path = os.path.join(os.path.dirname(__file__), 'a2-sample.txt')
    file = open(file_path, 'r', encoding="utf-8")

    for line in file:
        #Allocate customer to a teller (if teller is idle)
        print(line)

        #If everyone is busy then add to the qyeye

        #Update queue to move people in priority

        #If a tellar becomes free then pull the first person from the queue

        #End simulation when queue becomes empty and the last customer has left

if __name__ == "__main__":
    tellar_simulation(1)