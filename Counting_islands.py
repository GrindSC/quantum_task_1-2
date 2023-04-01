def count_islands(M,N,matrix):
    count = 0
    
    def explore_island(i, j):
        if i >= 0 and j >= 0 and i < M and j < N and matrix[i][j] != 0:
            matrix[i][j] = 0
            explore_island(i+1, j)
            explore_island(i-1, j)
            explore_island(i, j+1)
            explore_island(i, j-1)
    
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 1:
                count += 1
                explore_island(i, j)
                
    return count

inputs= [
    [3,3,[[0, 1, 0],[0, 0, 0],[0, 1, 1]]],
    [3, 4, [[0, 0, 0, 1],[0, 0, 1, 0],[0, 1, 0, 0]]],
    [3, 4, [[0, 0, 0, 1],[0, 0, 1, 1],[0, 1, 0, 1]]]
]
assert count_islands(*inputs[0])==2
assert count_islands(*inputs[1])==3
assert count_islands(*inputs[2])==2