#list of function 

def myfunction():
    print(" calling my function")
print("top")
myfunction()
print("bottom")

def sum(num1,num2):
    result=num1+num2
    return result
print("Calling sum")
myvalue=sum(2,3)
print(myvalue)

def compare_max(num1,num2,num3):
    if (num1>num2 or num2 > num3):
        print ("number1 is greater",num1, "or Number 2 is greater" , num2)
    elif (num3>num2 or num2 <num3):
        print ("number2 is greater ", num2)
    else:
        print("None of the above")
print("calling compare max")
print(compare_max(2,6,4))      
print("end compare max")      
