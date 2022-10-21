def spiralOrder(matrix):
    result = []

    def circling(l, r, up, down):
        print(f'Left: {l}, Right: {r}')
        print(f'UP: {up}, DOWN: {down}')
        # Right
        # Traverse first line of matrix 
        for i in range(l, r):
            result.append(matrix[up][i])
        print(f'Right: {result}')
        # Down 
        # Travese last index through vertically
        for j in range(up+1, down):
            result.append(matrix[j][r-1])
        print(f'Down: {result}')
        # Left
        # Traverse last line of a list in reverse order
        for z in range(r-2, l-1, -1):
            result.append(matrix[down-1][z])
        print(f'Left: {result}')
        # Up
        # Traverse fisrt index of each line in reverse order before first line
        for y in range(down-2, up, -1):
            result.append(matrix[y][l])
        print(f'Up: {result}\n')
    h_f_idx, h_l_idx = 0, len(matrix[0])
    v_f_idx, v_l_idx = 0, len(matrix) 
    while v_f_idx < v_l_idx and h_f_idx < h_l_idx and v_f_idx < len(matrix) and v_l_idx > 1 :
        circling(h_f_idx, h_l_idx, v_f_idx, v_l_idx)
        v_f_idx += 1
        v_l_idx -= 1
        h_f_idx += 1
        h_l_idx -= 1
    return result

print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(spiralOrder([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]))
print(spiralOrder([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]))
print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))

