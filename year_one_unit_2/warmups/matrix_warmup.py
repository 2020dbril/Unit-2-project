#matrix = [[66, 2, 82, 65, 71], [27, 70, 96, 64, 53], [33, 27, 90, 35, 34], [96, 60, 17, 71, 32], [5, 58, 36, 45, 76]]
#for row in range(len(matrix)):
#    for col in range(len(matrix)):
#        print(matrix[row][col])
array=[[3,2,1],[4,6,5], [9,7,8]]
flattened_array=[]

for m in range (0,len(array[0])):
    for n in range(0,len(array)):
        flattened_array.append(array[m][n])
flattened_sorted_array = sorted (flattened_array)

print(flattened_sorted_array)
