import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# use built in style
plt.style.use("seaborn")
fig, ax = plt.subplots()

ax.plot(input_values, squares, linewidth=3)

ax.set_title("squares", fontsize=24)
ax.set_xlabel("values", fontsize=14)
ax.set_ylabel("squares", fontsize=14)
# set tick params size
ax.tick_params(axis="both", labelsize=14)

plt.show()
