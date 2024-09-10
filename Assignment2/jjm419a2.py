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

    def checkBusy(self, currentTime):
        #If tellar is not busy returns true
        #print("Start Time: " + str(self.startTime))
        #print("Duration: " + str(self.duration))
        #print("Start + Duration: " + str(self.startTime + self.duration))
        #print("Current time: " + str(currentTime))
        #print()
        if ((self.startTime + self.duration) <= currentTime):
            self.finishService()
            return True
        else:
            return False


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
        item = item.strip()
        if len(item) > 0:
            print("Added " + item + " to queue")
            #Enqueue is adding two lists together using list comprehesion in python
            if item[-1] == "1":
                self.p1 = self.p1 + [item]
                compareLength = (len(self.p1) + len(self.p2) + len(self.p3))
                if (self.maxLength < compareLength):
                    self.maxLength = compareLength
            elif item[-1] == "2":
                self.p2 = self.p2 + [item]
                compareLength = (len(self.p1) + len(self.p2) + len(self.p3))
                if (self.maxLength < compareLength):
                    self.maxLength = compareLength
            elif item[-1] == "3":
                self.p3 = self.p3 + [item]
                compareLength = (len(self.p1) + len(self.p2) + len(self.p3))
                if (self.maxLength < compareLength):
                    self.maxLength = compareLength
            else:
                print("Out of bounds priority " + item[-1])

    def dequeue(self):
        print("Dequeued item")
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

    def is_empty(self):
        #Check if list is empty. Return result
        return ((len(self.p1) == 0) and (len(self.p2) == 0) and (len(self.p3) == 0))

def tellar_simulation(tellar_count):
    #Set total number of tellars
    tellars = [Tellar() for _ in range(tellar_count)]

    queue = Queue()
    queue_empty = False

    #Read from the text file
    file_path = os.path.join(os.path.dirname(__file__), 'a2-sample.txt')
    file = open(file_path, 'r', encoding="utf-8")

    start_time = time.time()
    for line in file:
        line = line.strip()
        fileEmpty = False
        allocated = False

        if line.strip() == "0 0":
            fileEmpty = True

        #while(queue_empty != True):
        #Allocate customer to a teller (if teller is idle)
        if(fileEmpty == False):
            allocated = False
            currentTime = time.time()
            if (allocated == False):
                for tellar in tellars: 
                    #Check the tellar has completed the task
                    tellar.checkBusy(currentTime)

                    #Tellar is not busy and queue is empty
                    if (tellar.checkBusy(currentTime) == True):
                        if (queue.is_empty()):
                            tellar.makeBusy(line, currentTime)
                            allocated = True
                            break
                        else:
                            tellar.makeBusy(queue.dequeue(), currentTime)
            
            if (allocated == False):
                queue.enqueue(line)


                #Tellar is not busy and queue is not empty
                #elif (tellar.checkBusy(currentTime) == True) and (not queue.is_empty()):
                    #Add item from queue to tellar
                #    tellar.makeBusy(queue.dequeue(), currentTime)

                    #Add line to queue
                #    queue.enqueue(line)

                #Tellar is busy
                #elif (tellar.checkBusy(currentTime) == False):
                    #Add line to queue
                #    queue.enqueue(line)
                #else:
                #    queueEmpty = True     



            
        #If everyone is busy then add to the qyeye

        #if allocated == False:
            #print(queue)
        #    queue.enqueue(line)

        #If a tellar becomes free then pull the first person from the queue

        #End simulation when queue becomes empty and the last customer has left

    end_time = time.time()

    total_time = end_time - start_time

    print(queue)

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