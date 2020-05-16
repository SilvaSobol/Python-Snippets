
# name = "Zara"
# age = 31
# job = "doctor"
# w = "This is Magic"
# print(w.title())
# print("Hello, my name is",name +".")
# print(f"My name is {name}, I am {age} years old and {job} is my occupation.")

# def iterate_dictionary(my_list):
# #     for i in range(len(my_list)):
# #         for key in my_list[i]:
# #             print(key,"-",my_list[i][key]+',')
#     for i in range(len(my_list)):
#         for key in my_list[i]:  
#             print("{} - {}, ".format(key, my_list[i][key]))        

# students = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
# print(iterate_dictionary(students))
# # first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# Michael
# John
# Mark
# KB



# Input: ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"] 
# Output: 1,4,13

# def FindIntersection(strArr):
#   a = strArr[0]
#   b =
#   return strArr

# # keep this function call here 
# print(FindIntersection(input()))

# arr = [55,81,-9,35,0]

# def addArr(arr):
#     sum = 0
#     max = arr[0]
#     min = arr[0]
#     for i in range(len(arr)):
#       if(arr[i] < min):
#         min = arr[i]
#       if(arr[i] > max):
#          max = arr[i]
#       sum = arr[i] + sum
#     return sum, max, min
# print(addArr(arr))

# x = "6"
# print(type(x))

# x = [1,2,3,4]
# def my_append(arr):
#     new_arr = []
#     for i in range(0,len(arr),3):
#         new_arr.append(arr[i])
#     return new_arr

# print(my_append(x))

#python swap
# arr = [1,2,3,4]
# arr[0], arr[1] = arr[1], arr[0]
# print(arr)



# HOW COOL IS THIS! 

# my_arr = [33,45,100,7,6,-7,0,26]
# # # print(sorted(my_arr))


# # # My version of selecion_sort / Hope the logic is correct :)

# def sort(my_arr):
#     for i in range(len(my_arr)):
#         for j in range(i+1,len(my_arr)):
#             if my_arr[i] > my_arr[j]:
#                 my_arr[i],my_arr[j] = my_arr[j],my_arr[i]
#         print(my_arr)
# sort(my_arr)

# print(sorted(my_arr))
# print(my_arr[2:4])
# print(max(my_arr))
# print(sum(my_arr))
# print(map(sort,my_arr))

# def my_lambda(num):
#     x = num **2 
#     return x
# print(my_lambda(5))

# my_list = ["abc", 123, "yxz"]
# for i in range(0,len(my_list)):
#     print(i, my_list[i])

# my_dict = {"name": "Noelle", "language": "Python"}
    # for k in my_dict:
    #     print(k,my_dict[k],end="")

# ninjas = {"rose", "tulip", "sunflower"}
# ninjas.defaultdict("Lorie")
# print(ninjas)

# x = {}
# x['name'] = "Jack"
# x['age'] = "32"
# print(w)
# print(x)


# count = 0
# while count < 5:
#     print("looping - ", count)
#     count += 1
# print

# print("My name is Sam, and I am " + str(43))

# total = "54"
# other_val = 34
# total = int(total) + other_val 
# print(total )

# y = 3
# while y > 0:
#     print(y)
#     y = y - 1
# else:
#     print("Why is not bigger than 0")

# for x in "string":
#     if x == "i":
#         break 
#     print(x,end=" ")

# for x in "disappearing":
#     if x == "p":
#         continue 
#     print(x)

# y = 3
# while y > 0:
#     print(y)
#     y = y - 1
#     if y == 0:
#         break
# else:
#     print("Final else statement")

# def para_game(name=" ", repeat = 100):
#     print(f"goog day{name}\n "*repeat)
# para_game("tim")

# class User:		# here's what we have so far
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.account_balance = 0
#     # adding the deposit method
#     def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
#     	self.account_balance += amount	# the specific user's account increases by the amount of the value received
    
#     def make_withdrawal(self, amount):
#         self.account_balance -= amount
    
#     def display_user_balance(self):
#         print(f"User: {self.name}, Balance: ${self.account_balance}")
    
#     def transfer_money(self, other_user, amount):
#         # BONUS
#         # let's leverage the fact that we have deposit and withdrawal methods that are available to self and other_user
#         # since they're both User objects...You don't have to do it this way though
#         other_user.make_deposit(amount) # could also say other_user.account_balance += amount
#         self.make_withdrawal(amount) # could also say self.account_balance -= amount
