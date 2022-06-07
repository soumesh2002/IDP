def getRow(m, r):
    return m[r - 1] # where r: row

def getCol(m, c):
    # m: matrix
    # c: col
    return [m[i][c - 1] for i in range(len(m))]

def main():
    vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
    
    r = int(input("enter row: "))
    c = int(input("enter col: "))

    print(getRow(vector, r))
    print(getCol(vector, c))

if __name__ == "__main__":
    main()