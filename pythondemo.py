import statistics
import matplotlib.pyplot as plt
subjects = ['Math', 'Science', 'English', 'History', 'Art']
numbers = [1, 2, 3, 4, 5]
mean = statistics.mean(numbers)
print("Mean:", mean)
plt.bar(subjects, numbers)
plt.show()