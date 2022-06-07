# component wise mean

def component_wise_mean(vec):
    # v: vector [list]
    assert all([len(vec[0]) == len(v) for v in vec])

    r, c = len(vec), len(vec[0])

    return [sum([vec[i][j] for i in range(r)]) / r for j in range(c)]

def main():
    matrix = [[7, 3, 4], [2, 3, 6], [7, 1, 2]]
    mean = component_wise_mean(matrix)
    print(f"Component wise mean of the vector: {mean}")

if __name__ == '__main__':
    main()