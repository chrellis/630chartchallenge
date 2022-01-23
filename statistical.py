import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'White non-Hispanic', 'Black', 'Native American', 'Asian',  'Multiracial'
sizes = [76.3, 13.4 , 1.3, 5.9, 2.8  ]
explode = (0, 0, 0.1, 0.0,   0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%'
    , startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title("Racial Statistics in America")

plt.show()