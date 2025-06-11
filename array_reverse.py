arr=[10,20,30,40,50]
start=0
end=len(arr)-1

print(f"array before reversing={arr}")

while start<end:
   arr[start],arr[end]=arr[end],arr[start]
   start=start+1
   end=end-1
   
   
print(f"reversed array={arr}")