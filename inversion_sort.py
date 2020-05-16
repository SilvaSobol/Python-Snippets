#Starting at index 1, shifting that value to the left until it is sorted relative to all values to the left, and then moving on to the next index position and performing the same shifts until the end of the list is reached. 

x = [99,-9,88,-8,45,0]

def inversion_sort(my_list):
    for x in range(1,len(my_list)):
        temp = my_list[x]
        one_before = x-1
        while one_before >=0 and temp < my_list[one_before]:
            my_list[one_before +1] = my_list[one_before]
            one_before -= 1
        my_list[one_before + 1] = temp
    return(my_list)

print(inversion_sort(x))

#or

def bubblesort(list_values):
##ex: [5,3,6,1]
#[3,5,6,1]
#[3,5,6,1]
#[3,5,1,6] ONCE
#[3,5,1,6]
#[3,1,5,6]
#[1,3,5,6[
    for j in range(len(list_values)):
        swap = 0
        for i in range(len(list_values)-1-j):
            if list_values[i] > list_values[i+1]:
                list_values[i],list_values[i+1] = list_values[i+1],list_values[i]
#count the number of swaps that occurred!
                swap += 1
#if no swaps occurred, we can confirm that the entire array is in order so return the ordered list
        if swap == 0:
            break
    return list_values
            
arr = [6,5,3,1,8,7,2,4]
print(bubblesort(arr))

arr = [64, 34, 25, 12, 22, 11, 90]*100
print(bubblesort(arr))