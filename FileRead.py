file_read=open("employee.txt","r")
for employee in file_read.readlines():
#print (file_read.read())
    print (employee)
#print (file_read.readlines()[2])
file_read.close()