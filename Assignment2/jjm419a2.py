import sys
#import numpy
import time

#I only use os to get the path of the input file to make sure its correct
import os

class Tellar:
    def __init__(self):
        self.isBusy = False
        self.item = ""
        self.startTime = 0.0
        self.duration = 0.0
        self.count = 0

    def __str__(self):
        print("Busy: " + str(self.isBusy))
        print(self.item)
        print(str(self.count))

    def makeBusy(self, customer, currentTime):
        if len(customer) > 0:
            self.item = customer
            self.isBusy = True
            self.count += 1
            numbers = [float(num) for num in self.item.split()]

            if len(numbers) > 0:
                self.startTime = currentTime
                self.duration = numbers[1]

    def finishService(self):
        self.isBusy = False
        self.item = ""
        self.startTime = 0.0
        self.duration = 0.0

    def checkBusy(self):
        #If tellar is not busy returns true
        return (not self.isBusy)


class Queue:
    def __init__(self):
        #The basis of the queue will be a list
        #Each list will have a associated count to find max length
        self.p1 = []
        self.p2 = []
        self.p3 = []
        self.maxLength = 0

    def __str__(self):
        return "P1 Queue: " + ' '.join(self.p1) + "\n" + "P2 Queue: " + ' '.join(self.p2) + "\n" + "P3 Queue: " + ' '.join(self.p3) + "\n"

    def enqueue(self, item):
        item.strip()
        print(item.strip())
        #Enqueue is adding two lists together using list comprehesion in python
        if item[-1] == 1:
            self.p1 = self.p1 + [item]
            compareLength = (len(self.p1) + len(self.p2) + len(self.p3))
            if (self.maxLength < compareLength):
                self.maxLength = compareLength
        elif item[-1] == 2:
            self.p2 = self.p2 + [item]
            compareLength = (len(self.p1) + len(self.p2) + len(self.p3))
            if (self.maxLength < compareLength):
                self.maxLength = compareLength
        elif item[-1] == 3:
            self.p3 = self.p3 + [item]
            compareLength = (len(self.p1) + len(self.p2) + len(self.p3))
            if (self.maxLength < compareLength):
                self.maxLength = compareLength
        else:
            print("Out of bounds priority " + item[-1])

    def dequeue(self):
        #print(item)
        if len(self.p1) != 0:
            output = self.p1[0]
            self.p1 = self.p1[1:]
            return output
        elif len(self.p2) != 0:
            output = self.p2[0]
            self.p2 = self.p2[1:]
            return output
        elif len(self.p3) != 0:
            output = self.p3[0]
            self.p3 = self.p3[1:]
            return output
        else:
            print("Dequeue error")

    def maxQueueLength(self):
        max_length = 0

        if self.p1MaxLength > max_length:
            max_length = self.p1MaxLength
        if self.p2MaxLength > max_length:
            max_length = self.p2MaxLength
        if self.p3MaxLength > max_length:
            max_length = self.p3MaxLength

        return max_length

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
        allocated = False
        line = line.strip()

        if line.strip() != "0 0":
            #Allocate customer to a teller (if teller is idle)
            for tellar in tellars:

                #Check the tellar has completed the task
                if tellar.duration <= start_time + tellar.startTime:
                    tellar.finishService()

                #Tellar is not busy and queue is empty
                if (tellar.checkBusy() == True) and (queue.is_empty()):
                    tellar.makeBusy(line, start_time)
                    #allocated = True
                    #break

                #Tellar is not busy and queue is not empty
                elif (tellar.checkBusy() == True) and (not queue.is_empty()):
                    #Add item from queue to tellar
                    tellar.makeBusy(queue.dequeue(), start_time)

                    #Add line to queue
                    queue.enqueue(line, start_time)

                #Tellar is busy
                elif (tellar.checkBusy() == False):
                    #Add line to queue
                    queue.enqueue(line, start_time)
        
        #If everyone is busy then add to the qyeye

        #if allocated == False:
            #print(queue)
        #    queue.enqueue(line)

        #If a tellar becomes free then pull the first person from the queue

        #End simulation when queue becomes empty and the last customer has left

    end_time = time.time()

    total_time = end_time - start_time

    print("Simulation Statistics")
    print("Customers Served by Each Teller")
    i = 0
    for tellar in tellars:
        print("Tellar[" + str(i) + "]: " + str(tellar.count))
        i =+ 1
    print("Total Time of Simulation: " + str(total_time))


    print("Maximum Length of the Queue: " + str(queue.maxLength))



if __name__ == "__main__":
    tellar_simulation(1)
    #tellar_simulation(2)
    #tellar_simulation(4)