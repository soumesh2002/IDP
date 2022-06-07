from matplotlib import pyplot as plt
from math import exp, sqrt, pi

def normal_pdf(x, mu=0, sigma=1):
    return exp(-(x - mu) ** 2 / 2 / sigma ** 2) / (sqrt(2 * pi) * sigma)

xs = [x / 10 for x in range(-50, 50)]
plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], '-', label='mu = 0, sigma = 1')
plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], '--', label='mu = 0, sigma = 2')
plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], ':', label='mu = 0, sigma = 0.5')
plt.plot(xs, [normal_pdf(x, mu=-1) for x in xs], '-.', label='mu = -1, sigma = 1')

plt.legend(loc=1)
plt.title("various normal pdf: ")
plt.show()