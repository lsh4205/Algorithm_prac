# You are given an n x n 2D matrix representing an image, 
# rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, 
# which means you have to modify the input 2D matrix directly.
#  DO NOT allocate another 2D matrix and do the rotation.

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# [[7,4,1],[8,5,2],[9,6,3]]


def rotateImage(matrix) :
    # Reference issue
    # new_list = my_list
    # just assigns the name new_list to the object my)list refers to
    # https://stackoverflow.com/questions/240178/list-of-lists-changes-reflected-across-sublists-unexpectedly
    
    temp = [[0 for i in range(len(matrix))] for j in range(len(matrix))]
    # 1. Rotate Diagonal
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            temp[j][i] = matrix[i][j]
    temp1 = [[0 for i in range(len(matrix))] for j in range(len(matrix))]
    print(temp)
    # 2. Mirrored
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            temp1[j][i] = temp[j][len(matrix)-i-1]
    
    return temp1

def rotateOriginal(matrix):
    # 1. Diagonal Rotation
    for i in range(len(matrix)):
        for j in range(i,len(matrix)):
            temp = matrix[i][j]
            print(f'temp={temp}, [{i}][{j}]={matrix[i][j]}, [{j}][{i}]={matrix[j][i]}')
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
            
    print(matrix)
    # 2. Mirrored
    for j in range(int(len(matrix)/2)):
        for i in range(len(matrix)):
            temp = matrix[i][j]
            print(f'temp={temp}, [{i}][{j}]={matrix[i][j]}, [{j}][{i}]={matrix[j][i]}')
            matrix[i][j] = matrix[i][len(matrix)-j-1]
            matrix[i][len(matrix)-j-1] = temp
    print(matrix)

# Save Memory by reducing temp val
def rotateOriginal2(matrix):
    # 1. Diagonal Rotation
    for i in range(len(matrix)):
        for j in range(i,len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            print(f'[{i}][{j}]={matrix[i][j]}, [{j}][{i}]={matrix[j][i]}')
    # 2. Mirrored
    for j in range(int(len(matrix)/2)):
        for i in range(len(matrix)):
            matrix[i][j], matrix[i][~j] = matrix[i][~j], matrix[i][j]

matrix = [[1,2,3],[4,5,6],[7,8,9]] 
#print(rotateImage(matrix))
#rotateOriginal(matrix)
rotateOriginal2(matrix)