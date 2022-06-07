from typing import List


def median(b: List):
    _inp = len(b)
    # median: the list needs to be sorted
    _sort = sorted(b)

    print(f"sorted data: {_sort}")

    if _inp % 2 == 0:
        return (_sort[_inp // 2] + _sort[_inp // 2 - 1]) / 2
    else:
        return _sort[_inp // 2]

def main():
    data = [1, 5, 2, 9, 3, 4]
    print(f"median: {median(data)}")

if __name__ == '__main__':
    main()
