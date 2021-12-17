def count_increased_values(values: list) -> int:
    """
    Returns the number of values in the list that are greater than the previous value.
    """
    count = 0
    for i in range(1, len(values)):
        if values[i] > values[i - 1]:
            count += 1
    return count


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read().split()
        data = [int(x) for x in data]
    print(count_increased_values(data))
