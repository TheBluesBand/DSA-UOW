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
        # self.isBusy = True
        # self.startTime = currentTime
        # self.duration = duration
        # self.count += 1
        # self.busyUntil = currentTime + duration

        self.isBusy = True
        self.available_at = currentTime + nextServiceTime
        self.customers_served += 1

        # tellers[teller_index].isBusy = True
        #         tellers[teller_index].available_at = current_time + next_customer.service_time
        #         tellers[teller_index].customers_served += 1

    def finishService(self):
        self.isBusy = False
        self.startTime = 0.0
        self.duration = 0.0
        self.busyUntil = 0.0

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
            #print("Dequeue from p3: " + str(len(self.p3)))
            return output
        elif len(self.p2) != 0:
            output = self.p2[0]
            self.p2 = self.p2[1:]
            #print("Dequeue from p2: " + str(len(self.p2)))
            return output
        elif len(self.p1) != 0:
            output = self.p1[0]
            self.p1 = self.p1[1:]
            #print("Dequeue from p1: " + str(len(self.p1)))
            return output
        else:
            return None
            #print("Dequeue error " + str(len(self.p1)) + " " + str(len(self.p2)) + " " + str(len(self.p3)))

    def isEmpty(self):
        #Check if list is empty. Return result
        return ((len(self.p1) == 0) and (len(self.p2) == 0) and (len(self.p3) == 0))

def tellar_simulation(tellar_count):
    #Set the all of the intial variables
    queue = Queue()
    currentTime = 0.0
    totalWaitingTime = 0.0
    totalQueueLength = 0.0 
    maxQueueLength = 0
    totalSimulationTime = 0.0
    timeSteps = 0
    servedCustomers = []
    totalCustomers = 0
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

    customer_queue = Queue()
    tellers = [Teller() for _ in range(tellar_count)]

    current_time = 0
    served_customers = 0
    total_wait_time = 0
    total_service_time = 0
    max_queue_length = 0
    total_queue_length_time = 0
    last_queue_update_time = 0

    customer_index = 0
    next_teller_index = 0

    def all_tellers_idle():
        return all(not teller.isBusy for teller in tellers)

    while customer_index < customer_count or not customer_queue.isEmpty() or not all_tellers_idle():
        if current_time > last_queue_update_time:
            total_queue_length_time += customer_queue.size() * (current_time - last_queue_update_time)
            last_queue_update_time = current_time 

        while customer_index < customer_count and customers[customer_index].arrival_time <= current_time:
            customer_queue.enqueue(customers[customer_index])
            customer_index += 1

        for j in range(tellar_count):
            if tellers[j].isBusy and current_time >= tellers[j].available_at:
                tellers[j].isBusy = False
                tellers[j].idle_start = current_time 

        if customer_queue.size() > max_queue_length:
            max_queue_length = customer_queue.size()

        for t in range(tellar_count):
            teller_index = (next_teller_index + t) % tellar_count  
            if not tellers[teller_index].isBusy and not customer_queue.isEmpty():
                next_customer = customer_queue.dequeue()

                if not tellers[teller_index].isBusy and tellers[teller_index].idle_start < current_time:
                    tellers[teller_index].idle_time += current_time - tellers[teller_index].idle_start

                tellers[teller_index].makeBusy(current_time, next_customer.service_time)

                wait_time = current_time - next_customer.arrival_time
                if wait_time < 0:
                    wait_time = 0

                total_wait_time += wait_time
                total_service_time += next_customer.service_time
                served_customers += 1

                next_teller_index = (teller_index + 1) % tellar_count 
                break

        next_event_time = current_time
        event_found = False

        if customer_index < customer_count:
            next_event_time = customers[customer_index].arrival_time
            event_found = True

        for j in range(tellar_count):
            if tellers[j].isBusy:
                if not event_found or tellers[j].available_at < next_event_time:
                    next_event_time = tellers[j].available_at
                    event_found = True

        if next_event_time > current_time:
            current_time = next_event_time
        elif event_found:
            current_time = next_event_time
        else:
            break

    if current_time > last_queue_update_time:
        total_queue_length_time += customer_queue.size() * (current_time - last_queue_update_time)

    print("\nSimulation Statistics")
    print("Customers Served by Each Teller")
    for j in range(tellar_count):
        print(f"Teller [{j}]: {tellers[j].customers_served}")
    print(f"Total Time of Simulation: {current_time:.2f}")
    print(f"Average Service Time per Customer: {total_service_time / served_customers if served_customers else 0:.4f}")
    print(f"Average Waiting Time per Customer: {total_wait_time / served_customers if served_customers else 0:.3f}")
    print(f"Maximum Length of the Queue: {max_queue_length}")
    print(f"Average Length of the Queue: {total_queue_length_time / current_time if current_time > 0 else 0:.4f}")

    print("Average Idle Rate of Each Teller")
    for j in range(tellar_count):
        print(f"Teller [{j}]: {tellers[j].idle_time / current_time if current_time > 0 else 0:.7f}")
    

if __name__ == "__main__":
    tellar_simulation(1)
    #tellar_simulation(2)
    #tellar_simulation(4)