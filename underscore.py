# class Underscore:
#     def map(self, iterable, callback):
#         # your code here
#     def find(self, iterable, callback):
#         # your code here
#     def filter(self, iterable, callback):
#         # your code
#     def reject(self, iterable, callback):
#         # your code

# class Underscore:
#     def map(self, iterable, callback):
        
#         for i in range(len(iterable)):
#             iterable[i]= callback(iterable[i])
       

# # implement the 4 methods above using callbacks. You will have to modify the 4 methods to take in a list and a callback.

class Underscore:
    def map(self, iterable, callback):
        for x in range(len(iterable)):
            iterable[x] = callback(iterable[x])
        return iterable
    
    def find(self, iterable, callback):
        for val in iterable:
            if callback(val):
                return val
    
    
    def filter(self, iterable, callback):
        new_arr = []
        for val in iterable:
            if callback(val):
                new_arr.append(val)
        return new_arr
    
    def reject(self, iterable, callback):
        new_arr = []
        for val in iterable:
            if not callback(val):
                new_arr.append(val)
        return new_arr

_ = Underscore()
my_map = _.map([15,23,31], lambda x: x*9) # should return [2,4,6]
print(my_map)

found = _.find([1,2,3,4,5,6], lambda x: x > 4) # should return the first value that is greater than 4
print(found)

my_evens = _.filter([1,2,3,4,5,6], lambda x: x%2==0) # should return [2,4,6]
print(my_evens)

reject = _.reject([1,2,3,4,5,6], lambda x: x%2==0) # should return [1,3,5]
print(reject)