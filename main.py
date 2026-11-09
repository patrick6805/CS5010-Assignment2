def print_num_pattern(a, b):
    if a < 0:
        print(a, end="")
        return
    print(a, end=" ")
    print_num_pattern(a - b, b)
    print(f" {a}", end="")


if __name__ == "__main__":
    num1 = int(input())
    num2 = int(input())
    print_num_pattern(num1, num2)