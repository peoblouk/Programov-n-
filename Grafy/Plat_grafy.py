from matplotlib import pyplot as plt

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y = [38496, 42000, 46753, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]


plt.plot(ages_x, dev_y, "k--", label="Průměrný plat vývojáře")

py_dev_y = [45372, 18876, 53850, 57287, 63016, 65998, 70003, 71496, 75370, 83640]

plt.plot(ages_x, py_dev_y, "b", label="Python vývojáři")

plt.title("Roční plat")
plt.xlabel("Věk")
plt.ylabel("Průměrná mzda")

plt.legend()
plt.show()
