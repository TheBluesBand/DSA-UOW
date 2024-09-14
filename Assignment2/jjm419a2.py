#I only use os to get the path of the input file to make sure its correct
import os

#Yes I wrote these comments myself
class Teller:
    """Represents a teller in a simulation environment.

    Attributes:
        isBusy (bool): Indicates whether the teller is currently busy serving a customer.
        availableAt (float): The time at which the teller will become available.
        idleStart (float): The time at which the teller became idle.
        idleTime (float): The total idle time accumulated by the teller.
        customersServed (int): The number of customers the teller has served.
    """

    def __init__(self) -> None:
        """Initializes a new Teller object with default values for its attributes."""
        self.isBusy = False
        self.availableAt = 0.0
        self.idleStart = 0.0
        self.idleTime = 0.0
        self.customersServed = 0

    def __str__(self) -> str:
        """Returns a string representation of the teller's status.

        Returns:
            str: A string describing whether the teller is busy and the number of customers served.
        """
        return "Busy: " + str(self.isBusy) + " " + str(self.count)

    def makeBusy(self, currentTime, nextServiceTime) -> None:
        """Sets the teller as busy and calculates the next available time.

        Args:
            currentTime (float): The current simulation time.
            nextServiceTime (float): The estimated time for the next service.
        """
        self.isBusy = True
        self.availableAt = currentTime + nextServiceTime
        self.customersServed += 1

    def finishService(self, currentTime) -> None:
        """Sets the teller as not busy and updates the idle start time.

        Args:
            currentTime (float): The current simulation time.
        """
        self.isBusy = False
        self.idleStart = currentTime

    def updateIdleTime(self, currentTime) -> None:
        """Updates the teller's idle time if they are not busy.

        Args:
            currentTime (float): The current simulation time.
        """
        if not self.isBusy and self.idleStart < currentTime:
            self.idleTime += currentTime - self.idleStart
    
class Customer:
    """Represents a customer in a simulation environment.

    Attributes:
        arrivalTime (float): The time at which the customer arrived.
        serviceTime (float): The service time that the customer requires.
        priority (int): The customer's priority level, tgehigher priority is served first (from 3 to 1).
    """

    def __init__(self, arrivalTime, serviceTime, priority) -> None:
        """Initializes a new Customer object with the specified attributes.

        Args:
            arrivalTime (float): The time at which the customer arrived.
            serviceTime (float): The service time that the customer requires.
            priority (int): The customer's priority level, tgehigher priority is served first (from 3 to 1).
        """
        self.arrivalTime = arrivalTime
        self.serviceTime = serviceTime
        self.priority = priority

    def __str__(self) -> str:
        """Returns a string representation of the customer.

        Returns:
            str: A string containing the customer's arrival time, service time, and priority.
        """
        return "Arrival Time: " + str(self.arrivalTime) + " Service Time: " + str(self.serviceTime) + " Priority: " + str(self.priority)

class Queue:
    """Represents a queue with three priority levels and records the maximum length of the queue.

    Attributes:
        p1 (list): A list of customers with priority 1.
        p2 (list): A list of customers with priority 2.
        p3 (list): A list of customers with priority 3.
        maxLength (int): The maximum length the queue has reached.
    """

    def __init__(self) -> None:
        """Initializes a new Queue object with empty lists for each priority level and a max length of 0."""
        self.p1 = []
        self.p2 = []
        self.p3 = []
        self.maxLength = 0

    def __str__(self) -> str:
        """Returns a string representation of the queue.

        Returns:
            str: A string containing the contents of each priority level.
        """
        return "P1 Queue: " + str(self.p1) + "\n\n" + "P2 Queue: " + str(self.p2) + "\n\n" + "P3 Queue: " + str(self.p3) + "\n\n"

    def size(self) -> int:
        """Calculates the total size of the queue.

        Returns:
            int: The total number of customers in the queue.
        """
        return len(self.p1) + len(self.p2) + len(self.p3)

    def enqueue(self, customer) -> None:
        """Enqueues a customer into the appropriate priority level list.

        Args:
            customer (Customer): The customer to be enqueued.
        """
        compareLength = (len(self.p1) + len(self.p2) + len(self.p3))

        if customer.priority == 3.0:
            self.p3 = self.p3 + [customer]
            if (self.maxLength < compareLength):
                self.maxLength = compareLength
        elif customer.priority == 2.0:
            self.p2 = self.p2 + [customer]
            if (self.maxLength < compareLength):
                self.maxLength = compareLength
        elif customer.priority == 1.0:
            self.p1 = self.p1 + [customer]
            if (self.maxLength < compareLength):
                self.maxLength = compareLength
        else:
            print("Out of bounds priority " + str(customer.priority))

    def dequeue(self) -> Customer:
        """Dequeues the highest priority customer from the queue.

        Returns:
            Customer: The dequeued customer, or None if the queue is empty.
        """
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
        """Checks if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self.p1) == 0 and len(self.p2) == 0 and len(self.p3) == 0
    
def allTellarsIdle(tellers):
    """Checks if all tellers in the given list are idle.

    Args:
        tellers (list): A list of Teller objects.

    Returns:
        bool: True if all tellers are idle, False otherwise.
    """
    for teller in tellers:
        if teller.isBusy:
            return False
    return True

def tellar_simulation(tellar_count, file_name) -> None:
    """Simulates a bank teller system based on customer arrivals, service times, and priorities. Once complete, the simulation statistics are printed to the terminal.

    Args:
        teller_count (int): The number of tellers in the system.
        file_name (str): The name of the input file containing customer data.

    Returns:
        None
    """
    #Array of customers
    customers = []
    #Total number of customers
    totalCustomers = 0
    #Queue for the customers to be added to
    customQueue = Queue()
    #Array of tellers
    tellers = [Teller() for _ in range(tellar_count)]
    #Current simulation time
    currentSimTime = 0
    #Total number of customers served
    servedCustomersCount = 0
    #Total wait time
    totalWaitTime = 0
    #Total service time
    totalServiceTime = 0
    #Total queue time
    queueTimeTotal = 0
    #Last time the queue was updated
    queueLastUpdate = 0
    #Current customer index
    currentCustomer = 0
    #Next teller index
    nextTellerIndex = 0

    #Input all the data from the file
    filePath = os.path.join(os.path.dirname(__file__), file_name)
    file = open(filePath, 'r', encoding="utf-8")

    #Read the file and add the customers to the array of type Customer
    for line in file:
        line = line.split()
        if len(line) != 3:
            continue 
        arrival, service, priority = float(line[0]), float(line[1]), int(line[2])
        if arrival == 0 and service == 0:
            break
        customers.append(Customer(arrival, service, priority))
        totalCustomers += 1

    file.close()

    while currentCustomer < totalCustomers or not customQueue.isEmpty() or not allTellarsIdle(tellers):
        """Main simulation loop. Continues as long as there are customers to serve or idle tellers."""

        #Update the queue time if needed
        if currentSimTime > queueLastUpdate:
            queueTimeTotal += customQueue.size() * (currentSimTime - queueLastUpdate)
            queueLastUpdate = currentSimTime 

        #Enqueue customers that have arrived
        while currentCustomer < totalCustomers and customers[currentCustomer].arrivalTime <= currentSimTime:
            customQueue.enqueue(customers[currentCustomer])
            currentCustomer += 1

        #Process tellars that have finished their service
        for x in range(tellar_count):
            if tellers[x].isBusy and currentSimTime >= tellers[x].availableAt:
                tellers[x].finishService(currentSimTime)

        #Assign idle tellers to customers in the queue
        for t in range(tellar_count):
            index = (nextTellerIndex + t) % tellar_count  
            if not tellers[index].isBusy and not customQueue.isEmpty():
                """Assigns the teller to the next customer in the queue if they are not busy."""
                next_customer = customQueue.dequeue()
                tellers[index].updateIdleTime(currentSimTime)
                tellers[index].makeBusy(currentSimTime, next_customer.serviceTime)

                #Calculate the wait time for the customer and update the statistics
                wait_time = currentSimTime - next_customer.arrivalTime
                if wait_time < 0:
                    wait_time = 0
                totalWaitTime += wait_time

                totalServiceTime += next_customer.serviceTime
                servedCustomersCount += 1

                nextTellerIndex = (index + 1) % tellar_count 
                break #Breaks the loop if a customer has been assigned

        #Find the next event time
        next_event_time = currentSimTime
        event_found = False

        if currentCustomer < totalCustomers:
            next_event_time = customers[currentCustomer].arrivalTime
            event_found = True

        for x in range(tellar_count):
            if tellers[x].isBusy:
                if not event_found or tellers[x].availableAt < next_event_time:
                    next_event_time = tellers[x].availableAt
                    event_found = True

        #Update the simulation time to the next event time
        if next_event_time > currentSimTime or event_found:
            currentSimTime = next_event_time

    #Final update of the queue time
    if currentSimTime > queueLastUpdate:
        queueTimeTotal += customQueue.size() * (currentSimTime - queueLastUpdate)



    """Prints the simulation statistics to the terminal."""
    print("\n\nSimulation Statistics")
    print("Customers Served by Each Teller")
    for x in range(tellar_count):
        print(f"Teller [{x}]: {tellers[x].customersServed}")
    print(f"Total Time of Simulation: {currentSimTime:.3f}")
    print(f"Average Service Time per Customer: {totalServiceTime / servedCustomersCount if servedCustomersCount else 0:.4f}")
    print(f"Average Waiting Time per Customer: {totalWaitTime / servedCustomersCount if servedCustomersCount else 0:.5f}")
    print(f"Maximum Length of the Queue: {customQueue.maxLength}")
    print(f"Average Length of the Queue: {queueTimeTotal / currentSimTime if currentSimTime > 0 else 0:.7f}")

    print("Average Idle Rate of Each Teller")
    for x in range(tellar_count):
        print(f"Teller [{x}]: {tellers[x].idleTime / currentSimTime if currentSimTime > 0 else 0:.7f}")
    

if __name__ == "__main__":
    numberOfTellers = input("Please enter the number of tellers: ")
    fileName = input("Please enter the name of the input file: ")

    print(f"\nSimulation Inputs")
    print(f"Number of tellers: {numberOfTellers}")
    print(f"Name of input file: {fileName}")

    tellar_simulation(int(numberOfTellers), fileName.strip())