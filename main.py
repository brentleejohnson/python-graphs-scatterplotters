import matplotlib.pyplot as plt

x = [14.2, 16.5, 11.8, 15.3, 18.8, 22.5, 19.5]
y = [220.00, 330.00, 190.00, 340.00, 410.00, 445.00, 415.00]
plt.title("Soup sales in relation to temperature")
plt.xlabel("Temperature (%)")
plt.ylabel("Price in (R)")
plt.scatter(x, y)

"""a = [1.3, 3.4, 2.3, 9.8]
b = [3.5, 4.9, 1.3, 2.2]
c = [9.7, 1.5, 4.3, 0.9, 11.2]
data1 = [a, b, c]
plt.subplot(121)
plt.boxplot(data1)
plt.xlabel("Colleges")
plt.ylabel("Scores")
plt.title("Boxplot for colleges")
plt.subplot(122)
plt.hist(data1, bins=5)"""

plt.show()
