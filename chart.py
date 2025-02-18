
import matplotlib.pyplot as plt

# Data for the probability distribution of rolling two dice
sums = list(range(2, 13))
# probabilities = [1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36]


pp =  list(range(6))
pp.extend(list(range(6, 0, -1)))
probabilities = pp

# Convert probabilities to percentages
probabilities_percent = [p * 100 /36 for p in probabilities]

# Create the bar chart
plt.figure(figsize=(10, 5))
plt.bar(sums, probabilities_percent, color='skyblue', edgecolor='black')

plt.savefig('chart.png')

