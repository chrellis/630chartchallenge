import matplotlib.pyplot as plt 
from pywaffle import Waffle

fig = plt.figure( 
    FigureClass = Waffle, 
    rows = 3, 
    values = [6,9], 
    colors = ["#232066","#DCB732"], 
    icons = ["arrow-circle-up", "angle-up"], 
    font_size = 20,
    icon_style = "solid", 
    icon_legend = True, 
    legend = {
        "labels": ["feet", "inches"], 
        "loc": "upper left", 
        "bbox_to_anchor": (1,1)
    }
)
plt.title("Magic Johnson's Height in Feet and Inches")

plt.show()




