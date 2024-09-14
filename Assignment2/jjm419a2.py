#I only use os to get the path of the input file to make sure its correct
import os

class Teller:
    def __init__(self):
        self.isBusy = False
        self.available_at = 0.0
        self.idle_start = 0.0 
        self.idle_time = 0.0
        self.customers_served = 0

    def __str__(self):
        return "Busy: " + str(self.isBusy) + " " + str(self.count)

    def makeBusy(self, currentTime, nextServiceTime):
        self.isBusy = True
        self.available_at = currentTime + nextServiceTime
        self.customers_served += 1

    def checkBusy(self, currentTime):
        time_taken = float(self.startTime) + float(self.duration)
        if (float(time_taken) <= currentTime):
            self.finishService()
            return True
        else:
            return False

    def finishService(self, currentTime):
        self.isBusy = False
        self.idle_start = currentTime
        
    def serviceEnd(self):
        return self.startTime + self.duration
    
    def updateIdleTime(self, currentTime):
        if not self.isBusy and self.idle_start < currentTime:
            self.idle_time += currentTime - self.idle_start
    
class Customer:
    def __init__(self, arrival_time, service_time, priority):
        self.arrival_time = arrival_time
        self.service_time = service_time
        self.priority = priority

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
    
    def size(self):
        return len(self.p1) + len(self.p2) + len(self.p3)

    def enqueue(self, customer):
        #Enqueue is adding two lists together using list comprehesion in python
        if customer.priority == 3.0:
            self.p3 = self.p3 + [customer]
            compareLength = (len(self.p1) + len(self.p2) + len(self.p3))
            if (self.maxLength < compareLength):
                self.maxLength = compareLength
        elif customer.priority == 2.0:
            self.p2 = self.p2 + [customer]
            compareLength = (len(self.p1) + len(self.p2) + len(self.p3))
            if (self.maxLength < compareLength):
                self.maxLength = compareLength
        elif customer.priority == 1.0:
            self.p1 = self.p1 + [customer]
            compareLength = (len(self.p1) + len(self.p2) + len(self.p3))
            if (self.maxLength < compareLength):
                self.maxLength = compareLength
        else:
            print("Out of bounds priority " + str(customer.priority))

    def dequeue(self):
        if len(self.p3) != 0:
            output = self.p3[0]
            self.p3 = self.p3[1:]
            return output
        elif len(self.p2) != 0:
            output = self.p2[0]
            self.p2 = self.p2[1:]
            return output
        elif len(self.p1) != 0:
            output = self.p1[0]
            self.p1 = self.p1[1:]
            return output
        else:
            return None

    def isEmpty(self):
        #Check if list is empty. Return result
        return ((len(self.p1) == 0) and (len(self.p2) == 0) and (len(self.p3) == 0))
    
def allTellarsIdle(tellers):
    for teller in tellers:
        if teller.isBusy:
            return False
    return True

def tellar_simulation(tellar_count):
    #Set the all of the intial variables
    customers = []
    customer_count = 0

    #Input all the data from the file
    filename = "a2-sample.txt"
    file_path = os.path.join(os.path.dirname(__file__), filename)
    file = open(file_path, 'r', encoding="utf-8")


    for line in file:
        parts = line.split()
        if len(parts) != 3:
            continue 
        arrival, service, priority = map(float, parts)
        if arrival == 0 and service == 0:
            break
        customers.append(Customer(arrival, service, int(priority)))
        customer_count += 1

    customQueue = Queue()
    tellers = [Teller() for _ in range(tellar_count)]

    current_time = 0
    served_customers = 0
    total_wait_time = 0
    total_service_time = 0
    queueTimeTotal = 0
    last_queue_update_time = 0
    currentCustomer = 0
    nextTeller = 0

    while currentCustomer < customer_count or not customQueue.isEmpty() or not allTellarsIdle(tellers):
        if current_time > last_queue_update_time:
            queueTimeTotal += customQueue.size() * (current_time - last_queue_update_time)
            last_queue_update_time = current_time 

        while currentCustomer < customer_count and customers[currentCustomer].arrival_time <= current_time:
            customQueue.enqueue(customers[currentCustomer])
            currentCustomer += 1

        for j in range(tellar_count):
            if tellers[j].isBusy and current_time >= tellers[j].available_at:
                tellers[j].finishService(current_time)

        for t in range(tellar_count):
            teller_index = (nextTeller + t) % tellar_count  
            if not tellers[teller_index].isBusy and not customQueue.isEmpty():
                next_customer = customQueue.dequeue()

                tellers[teller_index].updateIdleTime(current_time)

                tellers[teller_index].makeBusy(current_time, next_customer.service_time)

                wait_time = current_time - next_customer.arrival_time
                if wait_time < 0:
                    wait_time = 0

                total_wait_time += wait_time
                total_service_time += next_customer.service_time
                served_customers += 1

                nextTeller = (teller_index + 1) % tellar_count 
                break

        next_event_time = current_time
        event_found = False

        if currentCustomer < customer_count:
            next_event_time = customers[currentCustomer].arrival_time
            event_found = True

        for j in range(tellar_count):
            if tellers[j].isBusy:
                if not event_found or tellers[j].available_at < next_event_time:
                    next_event_time = tellers[j].available_at
                    event_found = True

        if next_event_time > current_time or event_found:
            current_time = next_event_time
        else:
            break

    if current_time > last_queue_update_time:
        queueTimeTotal += customQueue.size() * (current_time - last_queue_update_time)

    print("\nSimulation Statistics")
    print("Customers Served by Each Teller")
    for j in range(tellar_count):
        print(f"Teller [{j}]: {tellers[j].customers_served}")
    print(f"Total Time of Simulation: {current_time:.2f}")
    print(f"Average Service Time per Customer: {total_service_time / served_customers if served_customers else 0:.4f}")
    print(f"Average Waiting Time per Customer: {total_wait_time / served_customers if served_customers else 0:.3f}")
    print(f"Maximum Length of the Queue: {customQueue.maxLength}")
    print(f"Average Length of the Queue: {queueTimeTotal / current_time if current_time > 0 else 0:.4f}")

    print("Average Idle Rate of Each Teller")
    for j in range(tellar_count):
        print(f"Teller [{j}]: {tellers[j].idle_time / current_time if current_time > 0 else 0:.7f}")
    

if __name__ == "__main__":
    tellar_simulation(4)
    #tellar_simulation(2)
    #tellar_simulation(4)