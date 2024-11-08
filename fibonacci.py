def fibonacci_rabbits(n, k):
    # the list for storing the number of rabbit pairs
    rabbits = [0] * (n + 1)

    rabbits[1] = 1  # After month 1, there's 1 pair of rabbits
    rabbits[2] = 1  # After month 2, there's still 1 pair

    # Compute the number of rabbit pairs for each month
    for month in range(3, n + 1):
        rabbits[month] = rabbits[month - 1] + rabbits[month - 2] * k

    return rabbits[n]


def read_input_from_file(file_name):
    with open(file_name, 'r') as file:
        # Read the first line for the input values of n and k
        n, k = map(int, file.readline().split())
    return n, k


def main():
    file_name = 'rosalind_fib.txt'
    n, k = read_input_from_file(file_name)
    result = fibonacci_rabbits(n, k)
    print(f"The total number of rabbit pairs after {n} months is: {result}")


if __name__ == "__main__":
    main()
