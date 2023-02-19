# https://adventofcode.com/2022/day/10

SCREEN_HEIGHT = 6
SCREEN_WIDTH = 40
FILE_NAME = "input.txt"


def get_data(file_name: str) -> list:
    cycle = 1
    commands = []
    with open(file_name, "r") as f:
        for line in f:
            commands.append((cycle, 0))
            match line.strip().split():
                case "addx", value:
                    cycle += 1
                    commands.append((cycle, int(value)))
            cycle += 1
    return commands


def process_commands(commands: list):
    register = 1
    screen = [' '] * SCREEN_WIDTH * SCREEN_HEIGHT
    sprite = (0, 1, 2)
    for cycle, value in commands:
        head = cycle - 1
        tmp = head % SCREEN_WIDTH
        if tmp in sprite:
            screen[head] = '█'
        if value != 0:
            register += value
            sprite = (register - 1, register, register + 1)
    return screen


if __name__ == '__main__':
    data = get_data(FILE_NAME)
    screen = process_commands(data)
    for i in range(SCREEN_HEIGHT):
        print("".join(screen[SCREEN_WIDTH * i:SCREEN_WIDTH * (i + 1)]), sep="")
