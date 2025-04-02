
## How to run the code:
```teminal
python3 problem02.py


```

## description
- create a patient abstract interface
- implement this interface to four types of patients objects: Elder, Child, Youth, and Adult
    - each object contains name and urgency attributes and a priority attribute as the comparator calculated according to the type and the urgency
    - For example, an Elder with an urgency of 3 will have a priority of 6, as the Elder’s priority adds an additional 3 to the initial urgency of 3.
- implement a priority queue, as an array with methods: add, delete, pop, print_queue
- when adding an object, compare the object's priority to all present objects in the queue,
    - if the adding object's priority is bigger than the compared one, insert the adding object before the compared one.
    - otherwise, append the object to the tail of the queue.
- when delete an object, search for it in the queue. If founded, remove it.
- when pop an object, remove the first object in the queue.