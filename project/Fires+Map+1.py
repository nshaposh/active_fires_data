
# coding: utf-8

# In[8]:

from bokeh.io import output_file, show
from bokeh.models import GMapPlot, GMapOptions, ColumnDataSource, Circle, DataRange1d, PanTool, WheelZoomTool, BoxSelectTool


map_options = GMapOptions(lat=30.29, lng=-97.73, map_type="roadmap", zoom=10)

plot = GMapPlot(
    x_range=DataRange1d(), y_range=DataRange1d(), map_options=map_options, title="Austin")
plot.api_key = "AIzaSyDea2ehkc_IE8vnhkw-C0AKBLeMu2LCBEo"

source = ColumnDataSource(
    data=dict(
        lat=[30.29, 30.20, 30.29],
        lon=[-97.70, -97.74, -97.78],
    )
)

circle = Circle(x="lon", y="lat", size=15, fill_color="blue", fill_alpha=0.8, line_color=None)
plot.add_glyph(source, circle)

plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())
output_file("fires.html")
show(plot)


# In[ ]:




# In[ ]:



