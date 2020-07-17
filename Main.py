import numpy as np

number_of_dice = 5


def roll_dice(number_of_dice):
    roll = np.random.randint(6, size=number_of_dice) + 1
    return roll


def group_duplicates(array):
    array.sort()
    new_list = []
    temp_list = []
    for i in array:
        if len(temp_list) > 0 and temp_list[0] != i:
            new_list.append(temp_list)
            temp_list = []
        temp_list.append(i)
    new_list.append(temp_list)
    return new_list


def score_roll(roll):
    new_list = []
    for i in roll:
        new_list.append(6 ** (5 - len(i)))
    return new_list


if __name__ == "__main__":
    roll = roll_dice(number_of_dice)
    grouped_roll = group_duplicates(roll)
    roll_score = score_roll(grouped_roll)

    keep = roll[0]
    for i in range(1, len(roll_score)):
        print(i - 1, i)
        if roll_score[i - 1] > roll_score[i]:
            keep = roll[i]


    print(grouped_roll)
    print(score_roll(grouped_roll))
    print(keep)
