import matplotlib.pyplot as plt
import numpy as np
vegetables = ["cucumber", "tomato", "lettuce", "asparagus",
"potato", "wheat", "barley"]
farmers = ["Farmer Joe", "Upland Bros.", "Smith Gardening",
"Agrifun", "Organiculture", "BioGoods Ltd.", "Cornylee Corp."]
harvest = np.array([[0.8, 2.4, 2.5, 3.9, 0.0, 4.0, 0.0],
[2.4, 0.0, 4.0, 1.0, 2.7, 0.0, 0.0],
[1.1, 2.4, 0.8, 4.3, 1.9, 4.4, 0.0],
[0.6, 0.0, 0.3, 0.0, 3.1, 0.0, 0.0],
[0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0],
[1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1],
[0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 6.3]])
plt.xticks(np.arange(len(farmers)), labels=farmers,
rotation=45, rotation_mode="anchor", ha="right")
plt.yticks(np.arange(len(vegetables)), labels=vegetables)
plt.title("Harvest of local farmers (in tons/year)")
for i in range(len(vegetables)):
    for j in range(len(farmers)):
        text = plt.text(j, i, harvest[i, j], ha="center", va="center", color="w")
plt.imshow(harvest)
plt.colorbar()
plt.tight_layout()
plt.show()