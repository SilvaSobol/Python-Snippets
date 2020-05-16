class SList:                       
    def __init__(self,val):
        self.head = None

    
    def add_to_front(self,val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self

    def print_values(self):
        runner = self.head
        while(runner != None):
            print(runner.values)
            runner = runner.next
        return self

#     def add_to_back(self,val):
#         if self.head == None:
#             self.add_to_front(val)
#             return self
#         new_node = SLNode(val)
#         runner = self.head
#         while(runner != None):
#             runner = runner. next
#         runner.next = new_node
#         return self

# #remove from front
#     def remove_from_front(self):
#         if self.head != None:
#             self.head = self.head.next
#             return self

#     def remove_from_back(self):
#         if self.head == None:
#             return self
#         elif self.head.next == None:
#             self.head = None
#             return self
#         else:
#             runner = self.head
#             while runner.self.next != None:
#                 runner = runner.next
#             runner.next = None 
#         return self

#     def remove_val(self,val):
#         if self.head == None:
#             return self
#         elif self.head.value == val:
#             self.head = self.head.next
#             return self
#         else:
#             runner = self.head
#             while runner.next != None and runner.next.value != val:
#                 runner = runner.next
#             if runner.next == None:
#                 return self
#             else: 
#                 runner.next = runner.next.next
#                 return self
            

class SLNode:
    def __init__(self, value):
        self.value = value
        self.next = None   

SLl = SList()
SLl.add_to_front("B").add_to_front("A").add_to_back("C").remove_from_front("D").print_values("E")

# SLl2 = SList()
# SLl2.add_to_back("Z").add_to_back("Y").remove_from_back().remove_from_back().remove_from_back().remove_from_back().print_values()

# SLl3 = SList()
# SLl3.add_to_back("A").add_to_back("B").add_to_back("C").add_to_back("D").remove_val("A").print_values()


# Create a new Python file and recreate the Node and SList classes  
# Add the add_to_front method to your SList class  
# Add the print_values method to your SList class  
# Add the add_to_back method to your SList class  
# NINJA BONUS: complete the remove_from_front method   #   NINJA BONUS: complete the remove_from_back method  #   NINJA BONUS: complete the remove_val method  
# SENSEI BONUS: complete the insert_at method  
# SENSEI BONUS: consider and account for edge cases for all previous methods
