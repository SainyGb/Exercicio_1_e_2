import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from check_equal_lists_random import check_equal_lists_random
from check_equal_sequences import equal_sequences

labels = list(range(1, 101))
random_method = []
consecutive_method = []

# Make 100 executions of the program
for i in range(100):
    random_method.append(check_equal_lists_random())
    consecutive_method.append(equal_sequences())

# Analyze the results.
frequencies_random = []
for value in range(1, 101):
    frequency_random = random_method.count(value)
    frequencies_random.append(frequency_random)

frequencies_consecutive = []
for value in range(1, 101):
    frequency_consecutive = consecutive_method.count(value)
    frequencies_consecutive.append(frequency_consecutive)

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars


fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, frequencies_random, width, label='random')
rects2 = ax.bar(x + width/2, frequencies_consecutive, width, label='consec')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
#ax.set_xticks(x, labels)
ax.legend()


ax.bar_label(rects1, padding=10)
ax.bar_label(rects2, padding=10)

# Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)
fig.tight_layout()

plt.show()
