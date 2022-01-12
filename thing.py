import matplotlib.pyplot as plt

data_set = { "california":39.6, "texas":29.7 ,"florida":21.9 ,"new york":19.3, "pennsylvania": 12.8 }
states = data_set.keys()
pop = data_set.values()

fig = plt.figure(figsize = (10, 5)) 

plt.bar(states, pop, color = 'yellow', width = 0.6)

plt.xlabel("5 most populous states")
plt.ylabel("population in millions")

plt.title("How many people live in the most populous American states" )

plt.show()