# https://adventofcode.com/2022/day/2

FILE_NAME = "input.txt"

elementMapping = {
    "X": "A",
    "Y": "B",
    "Z": "C"
}

elemetScore = {
    "A": 1,
    "B": 2,
    "C": 3,
}

elemetsWin = {
    "A": "B",
    "B": "C",
    "C": "A",
}

elementLose = {
    "A": "C",
    "B": "A",
    "C": "B"
}

wins = ["AB", "BC", "CA"]


def process_file(file_name):
    result = 0
    with open(file_name) as f:
        for line in f:
            oponent, encoded_me = line.split()
            me = elementMapping[encoded_me]
            play = oponent + me
            roundValue = 0
            if oponent == me:
                roundValue += 3
            elif play in wins:
                roundValue += 6
            roundValue += elemetScore[me]
            result += roundValue
    return result


def process_file2(file_name):
    result = 0
    with open(file_name) as f:
        for line in f:
            oponent, final = line.split()
            roundValue = 0
            if final == "Y":
                me = oponent
                roundValue += 3
            elif final == "X":
                me = elementLose[oponent]
            else:
                me = elemetsWin[oponent]
                roundValue += 6
            roundValue += elemetScore[me]
            result += roundValue

    return result


if __name__ == '__main__':
    res = process_file(FILE_NAME)
    print(res)

    res2 = process_file2(FILE_NAME)
    print(res2)
