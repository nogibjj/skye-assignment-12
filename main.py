import sys
from src.dotp import dot_product
def parse_input(arg):
    return list(map(int, arg.strip("[]").split(',')))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 dotp.py [vector_x] [vector_y]")
        sys.exit(1)

    vector_x = parse_input(sys.argv[1])
    vector_y = parse_input(sys.argv[2])

    dot_product(vector_x, vector_y)
