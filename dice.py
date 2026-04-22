import random


class RandomDice:
    def __init__(self, probabilities=None):
        if probabilities is None:
            self.probabilities = ([1/6] * 6)
            # self.unfair_prob = [3/4] + [1/20] * 5
        else:
            if len(probabilities) != 6 or not all(p >= 0 for p in probabilities) or not abs(sum(probabilities) - 1.0) < 1e-10:
                raise ValueError(
                    "Probabilities must be non-negative numbers summing to 1")
            self.probabilities = probabilities

        self.faces = [1, 2, 3, 4, 5, 6]

    def Roll(self, num_rolls=1):
        results = []

        for i in range(num_rolls):
            rnd = random.random()
            cummulative = 0

            for j, prob in zip(self.faces, self.probabilities):

                cummulative += prob

                if rnd <= cummulative:

                    results.append(j)

                    break
        return results
