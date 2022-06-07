def res_vector(r, c):
    return [[x + y for y in range(c)] for x in range(r)]

def main():
    r = int(input("enter the rows: "))
    c = int(input("enter the columns: "))
    print(res_vector(r, c))

if __name__ == '__main__':
    main()