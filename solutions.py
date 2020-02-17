""" Solutions to problems presented in the docs section """


def practice_problem(data_set, max_set_size=0, verbose=False):
    """ Solution to problem outlined in practice_problem.pdf. """

    set_results = []
    print(f"Attempting solution of {len(data_set)} data set(s)...")

    for data in data_set:

        # Allows us to set a max "set_size" if we want to focus on solving smaller sets first.
        if (not max_set_size) or (max_set_size and int(data['set_size']) < max_set_size):

            # Import our values from the data set.
            val_list = []
            set_name = data['set_name']
            key = data['max_val']
            values = [int(x) for x in data['values'][::-1]]

            if verbose:
                print(f"New problem set. Working with set {set_name}, key {key} and set size of {len(values)}")

            # Our main logic loop.
            for x in values:
                if (key - x) >= 0:
                    key -= x
                    val_list.append(x)

            # Parse our results.
            results = {
                'set_name': set_name,
                'max_val': data['max_val'],
                'set_size': len(val_list),
                'values': val_list,
                'score': sum(val_list)
            }

            if verbose:
                print(f"Results: Total score {results['score']} with set of {results['set_size']} values.")

            # Append our results to the set.
            set_results.append(results)

    # Return our set of results.
    print(f"Computation finished. Returning {len(set_results)} result(s).")
    return set_results
