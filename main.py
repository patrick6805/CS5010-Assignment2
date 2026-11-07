def print_num_pattern(a, b):
    print(a, end=" ")
    if a >= 0:
        print_num_pattern(a - b, b)
        print(a, end=" ")


if __name__ == "__main__":
    num1 = int(input())
    num2 = int(input())
    print_num_pattern(num1, num2)