def get_position(instructions: list) -> [int, int]:
    depth: int = 0
    horizontal_position: int = 0
    for i in range(0, len(instructions), 2):
        if instructions[i] == 'forward':
            horizontal_position += int(instructions[i + 1])
        elif instructions[i] == 'down':
            depth += int(instructions[i + 1])
        elif instructions[i] == 'up':
            if depth - int(instructions[i + 1]) > 0:
                depth -= int(instructions[i + 1])
            else:
                depth = 0
    return [horizontal_position, depth]


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.read().split()
    coordinates = get_position(data)
    print("Coordinates: ", coordinates)
    print("Answer: ", coordinates[0] * coordinates[1])

