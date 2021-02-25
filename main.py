# This is a sample Python script.

import csv
from math import floor


def quarter1(list, week):
    LEN = len(list)
    if LEN % 2 == 0:
        med = quarter2(list[0: int(LEN / 2)], week)
    else:
        med = quarter2(list[0: int(floor(LEN / 2))], week)
    return med


# This is equivalent to median
def quarter2(list, week):
    LEN = len(list)
    if LEN % 2 == 0:
        med = .5 * (list[int(LEN / 2) - 1][f'Week {week}'] + list[int(LEN / 2)][f'Week {week}'])
    else:
        med = list[int(floor(LEN / 2))][f'Week {week}']
    return med


def quarter3(list, week):
    LEN = len(list)
    if LEN % 2 == 0:
        med = quarter2(list[int(LEN / 2): LEN], week)
    else:
        med = quarter2(list[int((LEN / 2)): LEN], week)
    return med


def tukey_range(Q1, Q3):
    return [Q1 - 1.5 * (Q3 - Q1), Q3 + 1.5 * (Q3 - Q1)]


def print_participants_in_order(out_of_order, in_order, week):
    for p1 in in_order:
        for p2 in out_of_order:
            if p1.get('Name') == p2.get('Name'):
                print("\t{} {}".format(p1.get('Name'), p1.get(f'Week {str(week)}')))


if __name__ == '__main__':
    participants = []
    with open('participants.csv', 'r', newline='') as participants_file:
        reader = csv.DictReader(participants_file)
        for row in reader:
            participants.append({'Name': row['Name'], 'Week 1': float(row['Week 1']), 'Week 2': float(row['Week 2']),
                                 'Week 3': float(row['Week 3'])})

    original_participant_list = participants
    for week in range(1, 4):
        sorted_list = sorted(participants, key=lambda k: k[f'Week {week}'])
        print(f'Week: {week}')
        print(f'Q1: {quarter1(sorted_list, week)}')
        print(f'Q2: {quarter2(sorted_list, week)}')
        print(f'Q3: {quarter3(sorted_list, week)}')
        print(f'Tukey\'s Range: {tukey_range(quarter1(sorted_list, week), quarter3(sorted_list, week))}')
        print(f'Outliers:')
        outliers = []
        for participant in sorted_list:
            if participant[f'Week {week}'] < tukey_range(quarter1(sorted_list, week), quarter3(sorted_list, week))[0]:
                outliers.append(participant)
        print_participants_in_order(outliers, original_participant_list, week)

        print()
