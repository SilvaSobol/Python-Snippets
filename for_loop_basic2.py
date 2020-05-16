
# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def big_to_big(lst):
    for i in range(len(lst)):
        if lst[i] > 0:
            lst[i] = "big"
    return lst        
print(big_to_big([-4,3,6,-1]))
    


# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def pos_sum(lst):
    last = 0
    for val in lst:
      if val > 0:
        last += 1
    lst[len(lst)-1] = last
    return lst

# print(pos_sum([-1,3,3,3,9]))


# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

def the_sum(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum
print(the_sum([9,1,10]))


# Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5

def my_avg(lst):
    sum = 0
    for i in lst:
        sum += i
    return float(sum) / float(len(lst))

# print(my_avg([1,2,3,4]))

# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

def my_length(lst):
    unit = 0
    for i in lst:
        unit += 1
    return unit
print(my_length([0,1,2,3,4,5,6,7,8]))


# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

def my_min(lst):
    if len(lst) == 0:
        return False
    min = lst[0]
    for i in lst:
        if i < min:
            min = i
    return min

print(my_min([3,0,-80,1]))

# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

def my_max(lst):
    if len(lst) == 0:
        return False
    max = lst[0]
    for i in lst:
        if i > max:
            max = i
    return max

print(my_max([3,999,0,-80,1]))


# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ult_analysis(lst):
    big = {       
        "sum": None,
        "min": None,
        "max": None,
        "avg": None,
        "length": 0
    }
    if len(lst) == 0:
        return big 
    else:
        big["sum"] = 0
        big["max"] = lst[0]
        big["min"] = lst[0]

    for i in lst:
        if i > big["max"]:
            big["max"] = i
        elif i < big["min"]:
            big["min"] = i

        big["sum"] += i
        big["length"] += 1
    big["avg"] = float(big["sum"]) / float(len(lst))
    
    return big

print(ult_analysis([0,2,55,4,33]))

# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverse_list(lst):
    swap = int(len(lst) / 2)
    for i in range(swap):
        lst[i], lst[len(lst) - 1 - i] = lst[len(lst) - 1 - i], lst[i] # this is amazing how it works with both odd and even count of indexes
    return lst

print(reverse_list([37, 2, 1, -9]))
#print(reverse_list([37, 2, 1, -9, 5]))
#print(reverse_list([]))
#print(reverse_list([1]))
#print(reverse_list([1, 2]))