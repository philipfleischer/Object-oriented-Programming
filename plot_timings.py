import matplotlib.pyplot as plt
import numpy as np

array_list_get = np.loadtxt("array_list_get.txt")
array_list_insert = np.loadtxt("array_list_insert.txt")
linked_list_get = np.loadtxt("linked_list_get.txt")
linked_list_insert = np.loadtxt("linked_list_insert.txt")

fig, ax = plt.subplots(2, 2, sharex=True, sharey=True)

# ArrayList - get - O(1)
ax[0, 0].set_title("ArrayList (get)")
ax[0, 0].loglog(array_list_get.T[0], array_list_get.T[1], label="Time")
ax[0, 0].loglog(
    array_list_get.T[0],
    0.005 * np.ones_like(array_list_get.T[0]),
    label="O(1)",
    linestyle="--",
)

# ArrayList - insert - O(n)
ax[0, 1].set_title("ArrayList (insert)")
ax[0, 1].loglog(array_list_insert.T[0], array_list_insert.T[1], label="Time")
ax[0, 1].loglog(
    array_list_insert.T[0],
    0.001 * array_list_insert.T[0],
    label="O(n)",
    linestyle="--",
)

# LinkedList - get - O(n)
ax[1, 0].set_title("LinkedList (get)")
ax[1, 0].loglog(linked_list_get.T[0], linked_list_get.T[1], label="Time")
ax[1, 0].loglog(
    linked_list_insert.T[0],
    0.001 * linked_list_insert.T[0],
    label="O(n)",
    linestyle="--",
)

# LinkedList - insert - O(1)
ax[1, 1].set_title("LinkedList (insert)")
ax[1, 1].loglog(linked_list_insert.T[0], linked_list_insert.T[1], label="Time")
ax[1, 1].loglog(
    array_list_get.T[0],
    0.05 * np.ones_like(linked_list_insert.T[0]),
    label="O(1)",
    linestyle="--",
)

for axi in ax.flatten():
    axi.legend()
    axi.grid()

fig.savefig("arraylist_vs_linkedlist.png")
