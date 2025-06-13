#first approach
ar=[5,4,3,2]
a1=sorted(ar)
a2=sorted(ar, reverse=True) 
 
if ar==a1:
    print("sorted in ascending order")
elif ar==a2:
    print("sorted in descending")
else:
    print("not sorted")
   
#second approach
a = [4, 3, 2, 7]
asc = False
desc = False

for i in range(len(a) - 1):
    if a[i] < a[i + 1]:
        asc = True
    elif a[i] > a[i + 1]:
        desc = True

if asc and not desc:
    print("Array is in ascending order")
elif desc and not asc:
    print("Array is in descending order")
else:
    print("Array is not sorted")
