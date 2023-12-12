import math


def findAverage(num_values, values):
    total = sum(values)
    average = total / num_values
    return math.floor(average)


def main():
    num_values = int(input())
    values_input = input()
    values = list(map(int, values_input.split()))
    print(findAverage(num_values, values))


if __name__ == "__main__":
    main()
