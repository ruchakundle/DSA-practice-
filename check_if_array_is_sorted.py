arr = [9, 7, 5, 4, 2]  # You can change this array to test others

is_asc = True
is_desc = True

for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        is_asc = False
    if arr[i] < arr[i+1]:
        is_desc = False

if is_asc:
    print("Array is sorted in ascending order")
elif is_desc:
    print("Array is sorted in descending order")
else:
    print("Array is not sorted")
