import matplotlib.pyplot as plt

a = [1.3, 3.4, 2.3, 9.8]
b = [3.5, 4.9, 1.3, 2.2]
c = [9.7, 1.5, 4.3, 0.9, 11.2]
data1 = [a, b, c]
plt.subplot(121)
plt.boxplot(data1)
plt.xlabel("Colleges")
plt.ylabel("Scores")
plt.title("Boxplot for colleges")
plt.subplot(122)
plt.hist(data1, bins=5)

"""x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

plt.scatter(x, y)"""

plt.show()
