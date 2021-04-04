def calculate_probability(way, ps):
    res = 1
    for elem_is_working, p in zip(bin(way)[2:], ps):
        if elem_is_working == '1':
            res *= p
        else:
            res *= 1 - p
    return res


def join_paths(a, b):
    if isinstance(b[0], int):
        res = [a] + b
        return res
    res = []
    for i in b:
        part_of_result = join_paths(a, i)
        if isinstance(part_of_result[0], list):
            res += part_of_result
        else:
            res.append(join_paths(a, i))
    return res


def get_paths(matrix, start=0):
    res = []
    for i in matrix[start]:
        if not matrix[i]:
            res.append(i)
        else:
            part_of_result = join_paths(i, get_paths(matrix, i))
            if isinstance(part_of_result[0], list):
                res += part_of_result
            else:
                res.append(part_of_result)
    return res


def verify_working_capacity(path):
    result = ['1'] * 9
    for i in path[:-1]:
        result[i - 1] = '0'
    return int('0b' + ''.join(result), 2)


def is_workable(way, masks):
    for mask in masks:
        if mask | way == 255:
            return True
    return False


PATHS_ARRAY = [[1, 2],  # root node
               [3, 4],  # 1-st node
               [3, 5],  # 2-nd node
               [4, 5],  # 3-rd node
               [7, 8],  # 4-th node
               [6],     # 5-th node
               [7, 9],  # 6-th node
               [8, 9],  # 7-th node
               [10],    # 8-th node
               [10],    # 9-th node
               []]      # final node

P = [0.46, 0.05, 0.98, 0.16, 0.77, 0.51, 0.83, 0.16, 0.28]  # Probability array

paths = get_paths(PATHS_ARRAY)  # Looking for all possible paths

print("All possible paths:")
for path in paths:
    print(path)
print("")
masks = [verify_working_capacity(way) for way in paths]
p_result = 0
for i in range(256):
    if is_workable(i, masks):
        p_result += calculate_probability(i, P)

print("Probability is: " + str(p_result))
