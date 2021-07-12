import matplotlib.pyplot as plt

plt.style.use("seaborn")
fig, ax = plt.subplots()

ax.scatter(2, 4, s=200)

ax.set_title("squares", fontsize=24)
ax.set_xlabel("values", fontsize=14)
ax.set_ylabel("squares", fontsize=14)
# set tick params size
ax.tick_params(axis="both", which="major", labelsize=14)

plt.show()
