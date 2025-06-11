arr=[10,20,30,40,50]
max_val=arr[0]
min_val=arr[0]

for i in range(len(arr)):
    if max_val<arr[i]:
       max_val=arr[i]
       
    if min_val>arr[i]: 
     min_val=arr[i]
     
print("maximum value is:",max_val)
print("minimum value is:",min_val)