def vadd(v1, v2):
    assert len(v1) == len(v2)
    return [v1[i] + v2[i] for i in range(len(v1))]


def vsubtract(v1, v2):
    assert len(v1) == len(v2)
    return [v1[i] - v2[i] for i in range(len(v1))]


def vpro(v1, v2):
    assert len(v1) == len(v2)
    return [v1[i] * v2[i] for i in range(len(v1))]


def sca_pro(v1, a: int):
    return [a * v1[i] for i in range(len(v1))]


def dot_product(v1, v2: list):
    assert len(v1) == len(v2)
    return sum(vpro(v1, v2))


def length_vector(v):
    return len(v)

# menu driven programs
def menu(x, y):

    print("Calculator: 1.Vector Addition 2.Vector Subtraction 3.Vector Produt 4.Scalar Product 5.Dot Product 6.Length")

    choice = int(input("enter your choice of operation: "))

    if choice == 1:
        print("vector addition: ")
        print(f"{x} + {y}: {vadd(x, y)}")

    elif choice == 2:
        print("vector subtraction: ")
        print(f"{x} - {y}: {vsubtract(x, y)}")

    elif choice == 3:
        print("vector product: ")
        print(f"{x} * {y}: {vpro(x, y)}")

    elif choice == 4:
        _sca = int(input("input the value of scalar: "))
        print(f"Scalar product on vector (01): {sca_pro(x, _sca)}")
        print(f"Scalar product on vector (02): {sca_pro(y, _sca)}")

    elif choice == 5:
        print("dot product: ")
        print(f"{x} dot_pro {y}: {dot_product(x, y)}")

    elif choice == 6:
        print("length of vector: ")
        print(f"Length of vector 1: {length_vector(x)}")
        print(f"Length of vector 2: {length_vector(y)}")


def main():
    n = int(input("enter the size of the vector: "))  # x-a
    x = [int(input("enter the elements: ")) for i in range(n)]

    ny = int(input("enter the size of the vector: "))  # y-a
    y = [int(input("enter the elements: ")) for i in range(ny)]

    menu(x, y)


if __name__ == "__main__":
    main()
