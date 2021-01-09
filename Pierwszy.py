import os
from glob import glob
import csv
import numpy as np
from matplotlib import pyplot as plt

file_list = os.listdir('./covidpl')
file_list = [os.path.join('./covidpl', file_name) for file_name in file_list if '.csv' in file_name]
# file_list = glob('./covidpl/*.csv')
# print(len(file_list) == len(file_list_glob))

# voivodeship_dict = {Voivodeship: {date: (Confirmed, Deaths)}}
# voivodeship_dict = {Voivodeship: number}
list_of_voivodeship = []
data_array = np.zeros(shape=(16, len(file_list), 2))
date_list = []
for file_name in sorted(file_list):
    date_list.append(file_name.rstrip('.csv').lstrip('./covidpl'))
    with open(file_name, encoding='utf-8') as csv_file:
        print(file_name)
        d_reader = csv.DictReader(csv_file)
        for row in d_reader:
            voivodeship = row.get('Voivodeship')
            if voivodeship and 'https' not in voivodeship and voivodeship is not None:
                list_of_voivodeship.append(voivodeship.lower())
voivodeship_dict = {v: i for i, v in enumerate(sorted(set(list_of_voivodeship)))}

parse = lambda x: int(x.replace(' ', ''))

for i, file_name in enumerate(sorted(file_list)):
    with open(file_name, encoding='utf-8') as csv_file:
        d_reader = csv.DictReader(csv_file)
        for row in d_reader:
            voivodeship = row.get('Voivodeship')
            if voivodeship and 'https' not in voivodeship and voivodeship is not None:
                voivodeship_no = voivodeship_dict[voivodeship.lower()]
                data_array[voivodeship_no, i, 0] = parse(row.get('Confirmed'))
                data_array[voivodeship_no, i, 1] = parse(row.get('Deaths'))

# print(data_array)
data_array_2 = np.diff(data_array, axis=1)
fig, (death_ax, conf_ax) = plt.subplots(2, 1, sharex='col')
for voivodeship in voivodeship_dict.keys():
    death_ax.plot(date_list[1:], data_array_2[voivodeship_dict[voivodeship], :, 1], label=voivodeship)
    conf_ax.plot(date_list[1:], data_array_2[voivodeship_dict[voivodeship], :, 0], label=voivodeship)
death_ax.set_xlabel('date')
death_ax.set_ylabel('Deaths')
death_ax.grid(True)
conf_ax.set_xlabel('date')
conf_ax.set_ylabel('Confirmed')
conf_ax.grid(True)
conf_ax.minorticks_off()

plt.show()

# if __name__ == '__main__':
