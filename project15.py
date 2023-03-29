# First soluce

def count_path_rec_v1(n, i, j):
	if (i == n or j == n):
		return 1

	return count_path_rec_v1(n, i + 1, j) + count_path_rec_v1(n, i , j + 1)

def count_path_v1(n):
	return count_path_rec_v1(n, 0, 0)


# Second soluce

def count_path_rec_v2(n, i, j, mat):
	if (mat[i][j] != -1):
		return mat[i][j]

	mat[i][j] = count_path_rec_v2(n, i + 1, j, mat) + count_path_rec_v2(n, i , j + 1, mat)
	return mat[i][j]

def count_path_v2(n):
	mat = [[ -1 for _ in range(n + 1) ] for _ in range(n + 1)]
	for i in range(n + 1):
		mat[n][i] = 1
		mat[i][n] = 1
	return count_path_rec_v2(n, 0, 0, mat)

res = count_path_v2(20)
print(res)