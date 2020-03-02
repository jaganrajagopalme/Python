#list of Array operation :Start
Number_Array=[
              [1,2,3],[3,4,5],[5,6,7],
              [7,8,9],[11,22,33]
]
print(Number_Array[0][1])
for row in Number_Array:
    print(row)
    for col in row:
        print(col)