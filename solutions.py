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

        set_results = {
            'set_name': self.set_name,
            'max_weight': self.max_weight,
            'set_size': len(results),
            'values': results,
            'score': sum(results)
        }
        print(f"Results: Total score {sum(results)} with set of {len(results)} values.")
        return set_results

    def fast_solution(self):
        """ Fast solution. Formulated to solve the problem outlined
            in docs/practice_problem.pdf. """

        print(f"Solving for set {self.set_name} using \"Fast\" solution...")

        # Init our local variables.
        return_values = []
        weight = self.max_weight
        values = self.values

        # Make a safe copy of these values so we can manipulate them.
        key = copy.copy(weight)
        remaining = copy.deepcopy(values)

        # For each value (x) in our set, starting with the largest values first.
        for x in values[::-1]:

            # Subtract (x) from the max value (key) if the result is not-negative.
            if (key - x) >= 0:
                key -= x

                # Then add it to return_value list, and remove it from remaining list.
                return_values.append(x)
                remaining.remove(x)

        # If we do not end up with a perfect score, brute-force search the remainder.
        if weight != sum(return_values):
            return_values = self.brute_search(weight, return_values, remaining)

        # Some safety assertions to make sure things are running smoothly.
        assert weight == self.max_weight and weight != key
        assert len(values) != len(remaining)
        assert sum(return_values) <= weight

        return self.format_results(return_values)

    def knapsack_solution(self):
        """ The "Knapsack" solution. Formulated to solve the problem
            outlined in docs/practice_problem.pdf. """

        print(f"Solving for set {self.set_name} using \"Knapsack\" solution...")

        # Init our local variables.
        return_values = []
        mw = self.max_weight
        n = self.size
        wt = self.values
        val = self.values

        # Init our knapsack array.
        k = [[0 for x in range(mw + 1)] for x in range(n + 1)]

        # Build our knapsack bottom-up. We are counting from 0-n.
        for i in range(n + 1):
            # For each lower-bound limit of weight in max weight:
            for w in range(mw + 1):

                # If zero, set to zero.
                if i == 0 or w == 0:
                    k[i][w] = 0

                # If value is less than current limit, do complex math:
                elif wt[i - 1] <= w:
                    # The secret sauce.
                    k[i][w] = max(val[i-1] + k[i-1][w-wt[i-1]], k[i-1][w])

                # Else value is greater than current limit, use value.
                else:
                    k[i][w] = k[i-1][w]

        # The end of our table equals the total weight of the knapsack.
        result = k[n][mw]

        # Make a safe copy of these values so we can manipulate them.
        w = copy.copy(mw)
        res = copy.copy(result)

        # Now let's unpack the items in our knapsack.
        for i in range(n, 0, -1):
            # Upon zero, we have emptied our knapsack.
            if res <= 0:
                break
            # Ignore top results in the table, they are not relevant.
            if res == k[i-1][w]:
                continue
            else:
                # All other items must be inside our knapsack.
                if wt[i-1]:
                    return_values.append(wt[i-1])

                # Update our pointers as we retrieve each item,
                # so we can next find the item below it.
                res = res - val[i-1]
                w = w - wt[i-1]

        return self.format_results(return_values[::-1])

    @staticmethod
    def brute_search(weight, results, values):
        """ Check each value in our results and see if we can replace it
            with a better pair of values using brute-force search.

            The "fast" method should get us very close to the answer, so
            we want to start at the lowest values and work our way up. """

        # Init our local variables.
        score = sum(results)

        print(f"Current score {score}:{weight}, difference of {weight - score}. Searching for better values...")

        # For each value (x) in our current results, compare it against pairs of values from the
        # remaining set (of values that we didn't use) and see if they add up to a better score.
        for x in results:
            key = score - x
            for i in range(0, len(values)):
                for j in range(i + 1, len(values)):

                    # Ideally we should handle more match cases, but this works perfectly (for now).
                    match = values[i] + values[j]
                    if key + match == weight:

                        print(f"Found new values ({values[i]} + {values[j]}) to replace {x}.")

                        # So long (x), there's a new dynamic duo in town.
                        results.remove(x)
                        results.append(values[i])
                        results.append(values[j])

                        # Make sure everything checks out, and return results.
                        assert sum(results) == weight

                        return results
