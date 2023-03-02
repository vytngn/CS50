#outside of file import the function 
from functions import square

#call the function with para from 1 to 9
for i in range (10):
    print(f"The square of {i} is {square(i)}")

