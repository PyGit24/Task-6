# To check whether Integer or string using Lambda Function
test_list = ["10","501","22","37","100","999","87","351"]

res = list(filter(lambda x: x.isdigit(), test_list))
 
# checking all elements to be numeric using isdigit()
if(len(res) == len(test_list)):
    res = "The given list are integers"
    
else:
    res = "The given list is not integers"
# printing result
print("\tProgram to Check given list is Integer or string")
print("The original list is : ",  str(test_list))
print(str(res))