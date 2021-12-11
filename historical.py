import matplotlib.pyplot as plt
import numpy as np

Years = [1700, 1710, 1715, 1720, 1725, 1730, 1733, 1735, 1750, 1755, 1760, 1765, 1777, 1780] 
Imports = [33, 60, 77, 75, 71 , 65, 61, 62, 77, 85, 120, 150, 180, 185]
Exports = [70, 81, 88, 97, 100, 97, 95, 92, 90, 79, 78, 80, 90,90]


plt.plot(Years, Exports)
plt.plot(Years, Imports)
Years = np.array(Years)
Imports = np.array(Imports)
Exports = np.array(Exports)
plt.fill_between(Years, Imports, Exports, where=(Imports > Exports), color = 'C0', alpha = 0.3, interpolate = True) 
plt.fill_between(Years, Imports, Exports, where=(Imports < Exports), color = 'C1', alpha = 0.3, interpolate = True) 
plt.title('(Ex/Im)ports between Denmark and Norway in 18th century')
plt.xlabel('year')
plt.ylabel('10k')


plt.show()
