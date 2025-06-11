arr=[10,20,30,40,50]
first=arr[0]

for i in range(1,len(arr)):
    arr[i-1]=arr[i]
    
arr[-1]=first   #arr[-1] represents the last element  
print("Left Rotated:",arr)    
    