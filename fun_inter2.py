# # Avoid using class keywords like int, str, list, and dict as variable/parameter names.
# # Update Values in Dictionaries and Lists
# x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]



# # Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].

x[1][0] = 15
print(x)


# # Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'
print(students)

# # In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] ='Andres'
print(sports_directory)

# # Change the value 20 in z to 30
z[0]['y'] = 30
print(z)


# # Iterate Through a List of Dictionaries
# # Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:

#ORIGINAL VERSION 
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iprint(iterateDictionary(students)) 

def iterateDictionary(some_list):
    for my_dict in some_list:
      my_str = ''
      for my_key in my_dict.keys():
        my_str += f"{my_key}' - '{my_dict[my_key]},"
    # print(my_str)

print(iterateDictionary(students))

# #MY VERSION
    #for i in my_list: / print[i] (prints an entire dictionary)
    #for i in range (len(my_list)): # i in range(len(my_list)):
        #print[i] #index positions in the dictionary 
        #print(some_list)[i] #individual indexes withing the dictionary
        #print(my_list[i]['first_name']) #to access all first names-only

def iterate_dictionary(my_list):
    for i in range(len(my_list)):
        for key in my_list[i]:   
            print("{} - {},".format(key, my_list[i][key].split(',')))

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
print(iterate_dictionary(students))
            # print(f"this is {key}'-'{my_list[i][key]}") 
  # f"My name is {first_name} {last_name} and I am {age} years old."

# 1
for student in students:
    temp=''
    for key, value in student.items(): 
        if(key is 'first_name'):
            temp+=f'{key} - {value}' 
        else:
            temp+=f'{key} - {value}'
    print(temp)

# 2
def iterateDictionary(some_list):
    for x in range(0,len(some_list)):
        for y in some_list[x]:
            if(y == 'first_name'):
                print(y + " - " + some_list[x][y], end=",")
            else:
                print(y + " - " + some_list[x][y])

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
       
iterateDictionary(students)

# # # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # # bonus to get them to appear exactly as below!)
# # first_name - Michael, last_name - Jordan
# # first_name - John, last_name - Rosales
# # first_name - Mark, last_name - Guillen
# # first_name - KB, last_name - Tonel



# # Get Values From a List of Dictionaries
# # Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:

# # Michael
# # John
# # Mark
# # KB

def iterate_dictionary(key_name,some_list):
    for i in range(len(some_list)):
        print(some_list[i][key_name]) #to access all first names-only

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
iterate_dictionary('first_name', students)

# # And iterateDictionary2('last_name', students) should output:

# # Jordan
# # Rosales
# # Guillen
# # Tonel

def iterate_dictionary2(last_name,some_list):
    for i in range(len(some_list)):
        print(some_list[i][last_name]) #to access all first names-only

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
iterate_dictionary2('last_name', students)





# Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

def printInfo(some_dict):
    for key in some_dict:
        print(key.upper()), (len(some_dict[key]))
        for val in some_dict[key]:
            print(val)


dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)

# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon




