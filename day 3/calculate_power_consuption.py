def invert_binary_number(binary_number: str) -> str:
    """Invert a binary number."""
    inverted_binary = ""
    for i in range(len(binary_number)):
        inverted_binary += str(1 - int(binary_number[i]))
    return inverted_binary


def binary_to_decimal(binary):
    """Convert a binary number to decimal."""
    decimal = 0
    for i in range(len(binary)):
        decimal += int(binary[i]) * 2**(len(binary) - i - 1)
    return decimal


def get_binary_rates(metric_values: list) -> (str, str):
    """Get the binary representation of the power consumption rates from data."""
    count_dict = dict(zip([x for x in range(len(metric_values[0]))], [0 for x in range(len(metric_values[0]))]))
    metric_values_len = len(metric_values)
    epsilon_rate_binary = ""
    for item in metric_values:
        for i in range(len(item)):
            if item[i] == "1":
                count_dict[i] += 1
    for key, value in count_dict.items():
        if count_dict[key] >= metric_values_len / 2:
            epsilon_rate_binary += "1"
        else:
            epsilon_rate_binary += "0"
    return epsilon_rate_binary, invert_binary_number(epsilon_rate_binary)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().split()

    gamma_rate_binary, epsilon_rate_binary = get_binary_rates(data)
    print("Gamma rate binary:", gamma_rate_binary)
    print("Epsilon rate binary:", epsilon_rate_binary)
    gamma_rate = binary_to_decimal(gamma_rate_binary)
    epsilon_rate = binary_to_decimal(epsilon_rate_binary)
    print("Power consumption:", gamma_rate * epsilon_rate)
