a=int(input("enter  the  number you want : ")) 
b=int(input("enter  the  number you want : "))   
print(a//b) 
print(a%b) 
x=[a//b,a%b] 
print(tuple(x))
# secand  method  
# Read input values
a = int(input())
b = int(input())

# Print the required outputs
print(a // b)       # Integer division
print(a % b)        # Modulo operation
print(divmod(a, b)) # Tuple (integer division, modulo)
 