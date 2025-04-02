'''
Implement a priority queue ADT with the following functions:
• Add(object)
• Delete(object)
• Pop(object)
• PrintQueue()
Design an algorithm that takes as input a type of object and a value of that object.
For each type of object design a comparator
Given an input of some set of objects, enqueue them into a set of priorities and print your queues
Demonstrate you code by randomly generating an input set of size 5 to 50 for your objects (you must have at least 3 different
types of objects)
You must print out your input set, your priority queue and then exercise your methods add, delete and pop printing your tree
after every method invocation.
You should submit a readme.txt file with an explanation of your code and algorithms. You must provide exact instructions on how
to run your code and you must submit screen shots of your running code.
'''

#  Servicing patients at an Emergency Room

import random
from abc import ABC, abstractmethod

# the interface of patients
class PatientObj(ABC):
    type = ''
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency

    @abstractmethod
    def priority(self):
        pass

# four types of objects of patients
class Elder(PatientObj):
    type = 'Elder'
    def priority(self):
        return self.urgency + 3
class Child(PatientObj):
    type = 'Child'
    def priority(self):
        return self.urgency + 2
class Youth(PatientObj):
    type = 'Youth'
    def priority(self):
        return self.urgency
class Adult(PatientObj):
    type = 'Adult'
    def priority(self):
        return self.urgency + 1

# priority queue implementation
class PriorityQueue:
    def __init__(self):
        self.queue = []

    def add(self, patient_obj):
        if not self.queue:
            self.queue.append(patient_obj)
        else:
            insert = False
            for i in range(len(self.queue)):
                if patient_obj.priority() > self.queue[i].priority():
                    self.queue.insert(i, patient_obj)
                    insert = True
                    break
            if not insert:
                self.queue.append(patient_obj)

    def delete(self, patient_obj):
       if patient_obj in self.queue:
           self.queue.remove(patient_obj)
           print(f"deleted: {patient_obj.name}")
       else:
            print(f"Patient {patient_obj.name} not found in the queue")
    def pop(self):
        if self.queue:
            patient = self.queue.pop(0)
            print(f"Patient {patient.name} removed")
            return patient
        else:
            print("queue is empty")
            return None
    def print_queue(self):
        for patient in self.queue:
            print(f"patient's type is {patient.type} | name is {patient.name} | priority is {patient.priority()}")


# display the priorityqueue
def display_priority_queue():
    pq = PriorityQueue()
    patient_types = [Elder, Child, Youth, Adult]
    input_set = []

    # Generate random input of size between 5 and 50
    size = random.randint(5, 50)
    for _ in range(size):
        patient_type = random.choice(patient_types)
        name = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=5))
        urgency = random.randint(1,10)
        patient = patient_type(name, urgency)
        input_set.append(patient)
        pq.add(patient)

    # Display input set
    print("-------","\ninput set:")
    for patient in input_set:
        print(f"patient's type is {patient.type} | name is {patient.name} | priority is {patient.priority()}")

    # Display initial queue
    print("-------","\nInitial Priority Queue:")
    pq.print_queue()

    # demonstrate operations
    print("-------","\nDemonstrate operations")

    print("-------","\nAdd an object to the queue")
    new_patient = Elder("new_patient", 8)
    print(f"Add patient:  {new_patient.type} | name is {new_patient.name} | priority is {new_patient.priority()}")
    pq.add(new_patient)
    pq.print_queue()

    print("-------","\nDelete an object to the queue")
    print(f"Delete patient: {new_patient.type} | name is {new_patient.name} | priority is {new_patient.priority()}")
    pq.delete(new_patient)
    pq.print_queue()

    print("-------","\nPop an object to the queue")
    pq.pop()
    pq.print_queue()
if __name__ == "__main__":
    display_priority_queue()