from random import randint as ri
from collections import Counter as cr
from matplotlib import pyplot as plt

data = [ri(1, 100) for _ in range(100)]
hdata = cr([x // 10 * 10 for x in data])

# plotting
plt.bar([x+5 for x in hdata.keys()], hdata.values(), width=10, color="orange" ,edgecolor='lime')

plt.xticks(range(0, 111, 10))
plt.title("100 random integers generator: ")
plt.xlabel("x-axis")
plt.ylabel('count')
plt.show()