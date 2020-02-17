from utils import load_data_dir, export_results
import solutions

""" Google Hashcode 2020 """

data_set = []

# Load our data sets and format them using the keymap below.
for data in load_data_dir('data/practice', extension='.in', delimiter=' '):
    data_dict = {
        'set_name': data[0],
        'max_val': int(data[1][0]),
        'set_size': int(data[1][1]),
        'values': data[2]
    }

    data_set.append(data_dict)

# Run our solution code.
solution = solutions.practice_problem(data_set, max_set_size=0, verbose=False)

# Write our results to file.
export_results('results', solution)
