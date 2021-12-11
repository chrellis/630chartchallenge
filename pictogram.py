import matplotlib.pyplot as plt 
#import matplotlib as plt 
from pywaffle import Waffle

fig = plt.figure( 
    FigureClass = Waffle, 
    rows = 4, 
    values = [3, 11, 3, 7], 
    colors = ["#232066","#DCB732", "#999999", "#983D3D" ], 
    icons = ["frown", "meh", "smile","bed"], 
    font_size = 20,
    icon_style = "solid", 
    icon_legend = True, 
    legend = {
        "labels": ["sad", "meh", "happy", "sleeping"], 
        "loc": "upper left", 
        "bbox_to_anchor": (1,1)
    }

)
plt.show()




