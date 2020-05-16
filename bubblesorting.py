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

# arr = [64, 34, 25, 12, 22, 11, 90]*100
# print(bubblesort(arr))