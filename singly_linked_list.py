# 1. Just as we would pass in a value to a Python list's append method, our add_to_front method should accept a value to be added to the list:

    class SList:
        def __init__(self):
            self.head = None
        def add_to_front(self, val):	# added this line, takes a value

# 2. The first thing our method should do is create a node:

	def add_to_front(self, val):
            new_node = SLNode(val)	# create a new instance of our Node class using the given value

# This implies we have already created the Node class. We did this in the previous tab, but as a reminder, in a separate class (same file is okay):

class SLNode:
        def __init__(self, val):
            self.value = val
            self.next = None

# 3. We want this new node to be the front of our list, but let's not be too hasty. Since the only node we have a reference to in our list is the head, if we replace it right away, we'll lose our reference to the current head, so let's save it before moving forward:

	def add_to_front(self, val):
            new_node = SLNode(val)
            current_head = self.head	# save the current head in a variable

# 4. Currently our new node doesn't have a neighbor. Because we're trying to add this new node to the front, we now know its neighbor should be the current head that we just saved:

	def add_to_front(self, val):
            new_node = SLNode(val)
            current_head = self.head
            new_node.next = current_head	# SET the new node's next TO the list's current head

# 5. Finally, we need this new node to be the head of our list:

	def add_to_front(self, val):
            new_node = SLNode(val)
            current_head = self.head
            new_node.next = current_head
            self.head = new_node	# SET the list's head TO the node we created in the last step
            return self	                # return self to allow for chaining


TRAVERSING through a LIST

	def print_values(self):

#We need to start at the front of our list, so let's create a pointer to our first node:

	def print_values(self):
            runner = self.head	# a pointer to the list's first node


#As long as the runner variable is pointing to a node:

	def print_values(self):
            runner = self.head
            while (runner != None):	# iterating while runner is a node and not None

#Let's print its value:

	def print_values(self):
            runner = self.head
            while (runner != None):
                print(runner.value)	# print the current node's value
                
#Then, we need to "increment" our runner to the next node, or update the runner so it is pointing to its neighbor:

def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
        runner = runner.next 	# set the runner to its neighbor
        return self	     # once the loop is done, return self to allow for chaining

print(print_values())


# THROUGH THE LIST AND ADDING A VALUE TO THE END 
# This method will require a value to be added:

def add_to_back(self, val):	# accepts a value

#Then we'll want to create a new node with the given value:

def add_to_back(self, val):
     new_node = SLNode(val)	# create a new instance of our Node class with the given value

# Start an iterator at the beginning of the list:

def add_to_back(self, val):
    new_node = SLNode(val)
            runner = self.head	    # set an iterator to start at the front of the list

# Because we want to make it to the last node, we'll want to stop on the node who doesn't have a neighbor:

	def add_to_back(self, val):
            new_node = SLNode(val)
            runner = self.head
            while (runner.next != None):	# iterator until the iterator doesn't have a neighbor

# Increment the runner to its neighbor (since we just checked to ensure there is, in fact, a neighbor):

	def add_to_back(self, val):
            new_node = SLNode(val)
            runner = self.head
            while (runner.next != None):
                runner = runner.next # increment the runner to the next node in the list

# When the loop has finished running, runner will be pointing to the last node. Its next is currently set to None, but we want to make the new node we created at the beginning of this method to be its neighbor:

	def add_to_back(self, val):
            new_node = SLNode(val)
            runner = self.head
            while (runner.next != None):
                runner = runner.next
            runner.next = new_node	# increment the runner to the next node in the list

Consider the edge case where our list is empty. In that case, adding to the front would be the same as adding to the back. Since we've already written that method, let's use it!

def add_to_back(self, val):
    if self.head == None:	# if the list is empty
        self.add_to_front(val)	# run the add_to_front method
    return self	# let's make sure the rest of this function doesn't happen if we add to the front
    new_node = SLNode(val)
    runner = self.head
    while (runner.next != None):
        runner = runner.next
    runner.next = new_node	# increment the runner to the next node in the list
    return self                 # return self to allow for chaining

# Let's test our class!

my_list = SList()	# create a new instance of a list
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()    # chaining, yeah!
# output should be:
# Linked lists
# are
# fun!


class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

def add_to_front(self, val):
            new_node = SLNode(val)
            current_head = self.head
            new_node.next = current_head
            self.head = new_node	# SET the list's head TO the node we created in the last step
            return self	                # return self to allow for chaining

def print_values(self):
            runner = self.head
            while (runner != None):
                print(runner.value)
        	runner = runner.next 	# set the runner to its neighbor
            return self	

def add_to_back(self, val):
    if self.head == None:	# if the list is empty
        self.add_to_front(val)	# run the add_to_front method
        return self	# let's make sure the rest of this function doesn't happen if we add to the front
    new_node = SLNode(val)
    runner = self.head
    while (runner.next != None):
        runner = runner.next
    runner.next = new_node	# increment the runner to the next node in the list
    return self                 # return self to allow for chaining

my_list = SList()	# create a new instance of a list
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()    # chaining, yeah!
# output should be:
# Linked lists
# are
# fun!