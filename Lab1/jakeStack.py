class JakeStack:
    #Intalises the stack as a python list
    def __init__(self):
        self.stack = []

    #Using list comprehension we cut off the last element of the list
    def Pop(self):
        new_stack = self.stack[:-1]
        self.stack = new_stack

    #Append the new element onto the list
    def Push(self, element):
        self.stack = self.stack + [element]

    #Return the first element on the stack
    def Top(self):
        return self.stack[-1]
    
    #Return if the stack is empty or not
    def isEmpty(self):
        return len(self.stack) != 0
    
    def print_stack(self):
        print(self.stack)

