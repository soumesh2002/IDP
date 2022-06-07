from random import random
from matplotlib import pyplot as plt
from collections import Counter
from math import erf, sqrt


def normal_cdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    return (1 + erf((x - mu) / sqrt(2) / sigma)) / 2


def bernoulli_trial(p):
    return 1 if random() < p else 0


def binomial(n, p):
    return sum([bernoulli_trial(p) for _ in range(n)])


data = [binomial(100, 0.75) for _ in range(100)]
x = Counter(data)
plt.xticks([i for i in range(min(x.keys()) - 1, max(x.keys()) + 1)])
plt.bar([x - 0.5 for x in x.keys()], [v / 100 for v in x.values()],
        width=1, color='orange', edgecolor='black')

mean = 100 * 0.75  # np
deviation = (100 * 0.75 * (1 - 0.75)) ** 0.5
x = range(min(data), max(data) + 1)
y = [normal_cdf(i + 0.5, mean, deviation) -
     normal_cdf(i - 0.5, mean, deviation) for i in x]

plt.plot(x, y)
plt.title("Binomial distribution and Normal Approximation")
plt.show()
