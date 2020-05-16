# Selection sort works by iterating through the list, finding the minimum value, and moving it to the beginning of the list. Then, ignoring the first position, which is now sorted, iterate through the list again to find the next minimum value and move it to index 1. This continues until all values are sorted.

x = [3,6,4,7,5,2,1,0,8,9]
print(sorted(x))


#or
x = [3,6,4,7,5,2,1,0,8,9]

def selected_sort(my_list):
    for x in range (len(my_list)):
        min = x
        for y in range(x+1, len(my_list)):
            if my_list[min] > my_list[y]:
                min = y
        temp = my_list[x]
        my_list[x] = my_list[min]
        my_list[min] = temp 
    return my_list

print(selected_sort(x))


#from Max to Min

my_arr = [9,3,78,12,76,0,-2]

for idx in range(1, len(my_arr)): 
    temp = my_arr[idx] 
    prev_idx = idx-1
    while prev_idx >= 0 and temp < my_arr[prev_idx]: 
        my_arr[prev_idx + 1] = my_arr[prev_idx] 
        prev_idx -= 1
    my_arr[prev_idx + 1] = temp 

print(my_arr)