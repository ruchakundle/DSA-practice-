n = int(input())
p= input().split()
L = list(p)
result = ""

for a in L:
    if len(a)%2 == 1:
        if len(a) > len(result):
            result = a
            
if result == "":
   print("better luck next time!")
else:            
   print(result)
