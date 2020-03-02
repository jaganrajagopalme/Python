#Try and catch handling
try:
    number= int(input("Enter the number:"))
    print(number)
# except:
   # print("Please enter the number only") 
   
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")


