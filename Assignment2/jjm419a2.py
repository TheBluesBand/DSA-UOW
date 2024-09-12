import sys
import time

#I only use os to get the path of the input file to make sure its correct
import os

class Tellar:
    def __init__(self):
        self.isBusy = False
        self.startTime = 0.0
        self.duration = 0.0
        self.count = 0
        self.totalIdleTime = 0.0
        self.busyUntil = 0.0

    def __str__(self):
        return "Busy: " + str(self.isBusy) + " " + str(self.count)

    def makeBusy(self, currentTime, duration):
        self.isBusy = True
        self.startTime = currentTime
        self.duration = duration
        self.count += 1
        self.busyUntil = currentTime + duration

    def finishService(self):
        self.isBusy = False
        self.startTime = 0.0
        self.duration = 0.0

    def checkBusy(self, currentTime):
        time_taken = float(self.startTime) + float(self.duration)
        if (float(time_taken) <= currentTime):
            self.finishService()
            return True
        else:
            return False
        
    def serviceEnd(self):
        return self.startTime + self.duration
    
class Customer:
    def __init__(self, arrival_time, service_time, priority):
        self.arrivalTime = arrival_time
        self.serviceTime = service_time
        self.priority = priority
        self.waitingTime = 0.0

    def __str__(self):
        return "Arrival Time: " + str(self.arrivalTime) + " Service Time: " + str(self.serviceTime) + " Priority: " + str(self.priority)


class Queue:
    def __init__(self):
        #The basis of the queue will be a list
        #Each list will have a associated count to find max length
        self.p1 = []
        self.p2 = []
        self.p3 = []
        self.maxLength = 0

    def __str__(self):
        return "P1 Queue: " + str(self.p1) + "\n\n" + "P2 Queue: " + str(self.p2) + "\n\n" + "P3 Queue: " + str(self.p3) + "\n\n"

    def __len__(self):
        return len(self.p1) + len(self.p2) + len(self.p3)

    def enqueue(self, customer):
        #Enqueue is adding two lists together using list comprehesion in python
        if customer.priority == 1.0:
            self.p1 = self.p1 + [customer]
            compareLength = (len(self.p1) + len(self.p2) + len(self.p3))
            if (self.maxLength < compareLength):
                self.maxLength = compareLength
        elif customer.priority == 2.0:
            self.p2 = self.p2 + [customer]
            compareLength = (len(self.p1) + len(self.p2) + len(self.p3))
            if (self.maxLength < compareLength):
                self.maxLength = compareLength
        elif customer.priority == 3.0:
            self.p3 = self.p3 + [customer]
            compareLength = (len(self.p1) + len(self.p2) + len(self.p3))
            if (self.maxLength < compareLength):
                self.maxLength = compareLength
        else:
            print("Out of bounds priority " + str(customer.priority))

    def dequeue(self):
        if len(self.p1) != 0:
            output = self.p1[0]
            self.p1 = self.p1[1:]
            #print("Dequeue from p1: " + str(len(self.p1)))
            return output
        elif len(self.p2) != 0:
            output = self.p2[0]
            self.p2 = self.p2[1:]
            #print("Dequeue from p2: " + str(len(self.p2)))
            return output
        elif len(self.p3) != 0:
            output = self.p3[0]
            self.p3 = self.p3[1:]
            #print("Dequeue from p3: " + str(len(self.p3)))
            return output
        else:
            return None
            print("Dequeue error " + str(len(self.p1)) + " " + str(len(self.p2)) + " " + str(len(self.p3)))

    def isEmpty(self):
        #Check if list is empty. Return result
        return ((len(self.p1) == 0) and (len(self.p2) == 0) and (len(self.p3) == 0))

def tellar_simulation(tellar_count):
    #Input all the data from the file
    file_path = os.path.join(os.path.dirname(__file__), 'a2-sample.txt')
    file = open(file_path, 'r', encoding="utf-8")
    fileData = [line.split() for line in file if line.strip() != "0 0" and line.strip()]
    input_file = 'a2-sample.txt'

    #Turn the data into a list of customers with their arrival time, service time, and priority
    customers = []
    for record in fileData:
        if len(record) == 3:
            arrival, service, priority = record[0], record[1], record[2]
            customers.append(Customer(float(arrival), float(service), float(priority)))

    #Set total number of tellars
    tellars = [Tellar() for _ in range(tellar_count)]

    #Set the all of the intial variables
    queue = Queue()
    currentTime = 0.0
    totalWaitingTime = 0.0
    totalQueueLength = 0.0 
    maxQueueLength = 0
    totalSimulationTime = 0.0
    timeSteps = 0
    servedCustomers = []

    while (customers or not queue.isEmpty()):
        while(customers and customers[0].arrivalTime <= currentTime):
            queue.enqueue(customers[0])
            customers = customers[1:]

        for tellar in tellars:
            if tellar.busyUntil < currentTime:
                if not queue.isEmpty():
                    customer = queue.dequeue()
                    if customer != None:
                        customer.waitingTime = currentTime - customer.arrivalTime
                        tellar.makeBusy(currentTime, customer.serviceTime)
                        totalWaitingTime += customer.waitingTime
                        servedCustomers.append(customer)
                else:
                    # Track idle time if no customers are in the queue
                    tellar.totalIdleTime += 0.0001  

        if len(tellars) > 1:
            tellars = tellars[1:] + [tellars[0]]

        # Track max queue length and accumulate the queue length over time
        maxQueueLength = max(maxQueueLength, len(queue))
        totalQueueLength += len(queue)
        timeSteps += 1

        currentTime += 0.0001

    totalSimulationTime = currentTime

    # Calculate statistics
    avg_service_time = sum([c.serviceTime for c in servedCustomers]) / len(servedCustomers) if servedCustomers else 0
    avg_waiting_time = totalWaitingTime / len(servedCustomers) if servedCustomers else 0
    avg_queue_length = totalQueueLength / timeSteps if timeSteps > 0 else 0
    
    # Output the statistics in the specified format
    print(f"\nSimulation Inputs")
    print(f"Number of tellers: {tellar_count}")
    print(f"Name of input file: {input_file}\n")
    
    print(f"Simulation Statistics")
    print(f"Customers Served by Each Teller")
    for i, teller in enumerate(tellars):
        print(f"Teller [{i}]: {teller.count}")
    
    # Enforce precision for each output statistic
    print(f"Total Time of Simulation: {totalSimulationTime:.2f}")
    print(f"Average Service Time per Customer: {avg_service_time:.4f}")
    print(f"Average Waiting Time per Customer: {avg_waiting_time:.3f}")
    print(f"Maximum Length of the Queue: {maxQueueLength}")
    print(f"Average Length of the Queue: {avg_queue_length:.7f}")
    
    print(f"Average Idle Rate of Each Teller")
    for i, teller in enumerate(tellars):
        idle_rate = teller.totalIdleTime / totalSimulationTime if totalSimulationTime > 0 else 0
        print(f"Teller [{i}]: {idle_rate:.7f}")
    

if __name__ == "__main__":
    tellar_simulation(1)
    #tellar_simulation(2)
    #tellar_simulation(4)