#custom function for power number

def raise_to_power(base_num,power_num):
    result=1
    for index in range(power_num):
        result= result * base_num
    return result

myvalue=raise_to_power(2,4)
print(myvalue)
