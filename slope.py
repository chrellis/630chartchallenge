import matplotlib.pyplot as plt 
import numpy as np

#for one adult, one day, from 1/6 - 1/7


data_set = { "vail":208, "breckenridge":199 ,"palisades tahoe":209 ,"deer valley":239 }
resorts = data_set.keys()
prices = data_set.values()

fig = plt.figure(figsize = (10, 5)) 

plt.bar(resorts, prices, color = 'black', width = 0.6)

plt.xlabel("prominent ski resorts")
plt.ylabel("prices (USD)")

plt.title("how much does it cost to hit the slopes? price comparison for a single adult's one day of skiing" )

plt.show()