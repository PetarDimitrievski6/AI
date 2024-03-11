import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"


def process_data(matrix, n):
    result = list()
    for i in range(n):
        tmp_result = list()
        for j in range(n):
            if matrix[i][j] != '#':
                c = 0
                if i > 0:
                    if matrix[i - 1][j] == '#':
                        c += 1
                    if j > 0 and matrix[i - 1][j - 1] == '#':
                        c += 1
                    if j < n - 1 and matrix[i - 1][j + 1] == '#':
                        c += 1

                if i < n - 1:
                    if matrix[i + 1][j] == '#':
                        c += 1
                    if j > 0 and matrix[i + 1][j - 1] == '#':
                        c += 1
                    if j < n - 1 and matrix[i + 1][j + 1] == '#':
                        c += 1

                if j > 0 and matrix[i][j - 1] == '#':
                    c += 1

                if j < n - 1 and matrix[i][j + 1] == '#':
                    c += 1

                tmp_result.append(str(c))
            else:
                tmp_result.append('#')

        result.append(tmp_result)
    return result


if __name__ == "__main__":
    n = int(input())
    input_matrix = list()
    for i in range(n):
        tmp_list = input().split("   ")
        input_matrix.append(tmp_list)

    result_matrix = process_data(input_matrix, n)

    for i in range(n):
        line = "   ".join(result_matrix[i])
        print(line)
