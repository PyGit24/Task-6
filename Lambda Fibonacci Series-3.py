# Fibonacci Series using Lambda Function
# Importing Reduce from FunctionTools
# Method-1
from functools import reduce
 
fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])
print("\tProgram to find the Fibonacci Series using Lambda")
inpt = 50
print("The Given Fibonacci Series Number is:", + inpt)
print("The Fibonacci Series are:",fib(inpt))