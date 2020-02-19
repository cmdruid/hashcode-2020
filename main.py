from utils import load_data_dir, export_results
from solutions import PracticeSolution

""" Google Hashcode 2020 - Practice Round! """

data_set = []
solution_set = []

# Load our data set and format it properly using the keymap below.
for data in load_data_dir('data/practice', extension='.in', delimiter=' '):
    data_dict = {
        'set_name': data[0],
        'max_weight': int(data[1][0]),
        'set_size': int(data[1][1]),
        'values': [(i, int(x)) for i, x in enumerate(data[2])]
    }
    data_set.append(data_dict)

# Run our solution code.
for data in data_set:
    if 'also_big' in data['set_name']:
        s = PracticeSolution(data)
        solution_set.append(s.fast_solution())

# Check each file in the solution set and their scores.
for s in solution_set:
    print(f"Name: {s['set_name']}, Score: {s['score'] / s['max_weight']}")

# Write our results to file.
export_results('results', solution_set)
