import copy


class PracticeSolution:
    """ A class template for presenting our solution code in the
        practice round and future challenges. """

    def __init__(self, data):
        self.set_name = data['set_name']
        self.max_weight = data['max_weight']
        self.values = data['values']
        self.size = len(data['values'])

    def format_results(self, results):
        """ Print that we have got the receipts, and return them
            with proper formatting. """

        score = self.sum_of_tuples(results)

        # Convert our results into their index values.
        indexed_results = []
        for x in results:
            indexed_results.append(x[0])
        indexed_results.sort()

        set_results = {
            'set_name': self.set_name,
            'max_weight': self.max_weight,
            'set_size': len(results),
            'values': indexed_results,
            'score': score
        }
        print(f"Results: Total score {score} with set of {len(results)} values.")
        return set_results

    @staticmethod
    def sum_of_tuples(tuples):
        return sum([x[1] for x in tuples])

    def fast_solution(self):
        """ Fast solution. Formulated to solve the problem outlined
            in docs/practice_problem.pdf. """

        print(f"Solving for set {self.set_name} using \"Fast\" solution...")

        # Init our local variables.
        return_values = []
        total = 0
        weight = self.max_weight
        values = self.values

        # Make a safe copy of our value set so we can manipulate the copy.
        remaining = copy.deepcopy(values)

        # For each value (x) in our set.
        for x in values:

            # Add (x) from the max value (key) if the result is not-negative.
            if (total + x[1]) < weight:
                total += x[1]

                # Then add it to return_value list, and remove it from remaining list.
                return_values.append(x)
                remaining.remove(x)

        # If we do not end up with a perfect score, brute-force search the remainder.
        if weight != self.sum_of_tuples(return_values):
            return_values = self.brute_search(weight, return_values, remaining)

        # Some safety assertions to make sure things are running smoothly.
        assert len(values) != len(remaining)
        assert self.sum_of_tuples(return_values) <= weight

        return self.format_results(return_values)

    # def knapsack_solution(self):
    #     """ The "Knapsack" solution. Formulated to solve the problem
    #         outlined in docs/practice_problem.pdf. """
    #
    #     print(f"Solving for set {self.set_name} using \"Knapsack\" solution...")
    #
    #     # Init our local variables.
    #     return_values = []
    #     mw = self.max_weight
    #     n = self.size
    #     wt = self.values
    #     val = self.values
    #
    #     # Init our knapsack array.
    #     k = [[0 for x in range(mw + 1)] for x in range(n + 1)]
    #
    #     # Build our knapsack bottom-up. We are counting from 0-n.
    #     for i in range(n + 1):
    #         # For each lower-bound limit of weight in max weight:
    #         for w in range(mw + 1):
    #
    #             # If zero, set to zero.
    #             if i == 0 or w == 0:
    #                 k[i][w] = 0
    #
    #             # If value is less than current limit, do complex math:
    #             elif wt[i - 1] <= w:
    #                 # The secret sauce.
    #                 k[i][w] = max(val[i-1] + k[i-1][w-wt[i-1]], k[i-1][w])
    #
    #             # Else value is greater than current limit, use value.
    #             else:
    #                 k[i][w] = k[i-1][w]
    #
    #     # The end of our table equals the total weight of the knapsack.
    #     result = k[n][mw]
    #
    #     # Make a safe copy of these values so we can manipulate them.
    #     w = copy.copy(mw)
    #     res = copy.copy(result)
    #
    #     # Now let's unpack the items in our knapsack.
    #     for i in range(n, 0, -1):
    #         # Upon zero, we have emptied our knapsack.
    #         if res <= 0:
    #             break
    #         # Ignore top results in the table, they are not relevant.
    #         if res == k[i-1][w]:
    #             continue
    #         else:
    #             # All other items must be inside our knapsack.
    #             if wt[i-1]:
    #                 return_values.append(wt[i-1])
    #
    #             # Update our pointers as we retrieve each item,
    #             # so we can next find the item below it.
    #             res = res - val[i-1]
    #             w = w - wt[i-1]
    #
    #     return self.format_results(return_values)

    @classmethod
    def brute_search(cls, weight, results, values):
        """ Loop through each value in our remainder set and check if it can
            replace two lesser values in our results to give us a better score.

            The "fast" method should get us very close to the answer, so
            we want to start at the largest values in our results and work backwards.

            Note: This actually works even faster in reverse, but the google code
                  judges would not allow it! :-( """

        # Init our local variables.
        score = cls.sum_of_tuples(results)

        print(f"Current score {score}:{weight}, difference of {weight - score}. Searching for better values...")

        # For each (z) in our remaining set of un-used values, compare it against the largest pairs of values
        # from our results and work back-ward through the list.
        for z in range(0, len(values)):
            key = score + values[z][1]
            for i in range(len(results)-1, 0, -1):
                for j in range(i-1, 0, -1):

                    # Check if we can replace two smaller numbers with a more fitting number.
                    # Ideally we should handle more match cases, but this works perfectly (for now).
                    match = results[i][1] + results[j][1]
                    if key - match == weight:

                        print(f"Found a new value {values[z][1]} to replace ({results[i][1]}, {results[j][1]}).")

                        # Swap out our smaller values with the more fitting one.
                        results.remove(results[i])
                        results.remove(results[j])
                        results.append(values[z])

                        # Make sure everything checks out, and return results.
                        assert cls.sum_of_tuples(results) == weight

                        return results
