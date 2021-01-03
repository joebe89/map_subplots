'''
Outputs a n*n subplot using matplotlib with basemap
Labels for each data point, shifted to avoid overlap using adjustText
'''

import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
from adjustText import adjust_text

gdf = gpd.read_file('data.shp')

# transforms to EPSG 3857 to align with ctx basemaps
gdf = gdf.to_crs(epsg=3857)

# creates groupby object
site = gdf.groupby()


plt.figure(figsize =(20,20))

# Iterate through sites

for i, (j, k) in enumerate(site):
    # create subplot axes in a n*n grid
    ax = plt.subplot(n_rows, n_cols, i + 1) # nrows, ncols, axes position
    # plot the site on these axes
    k.plot(ax=ax)
    # set the title
    ax.set_title(k, fontsize = 18)
    # set the aspect
    # adjustable datalim ensure that the plots have the same axes size
    ax.set_aspect('equal', adjustable='datalim')
    # configure labels, adjust_text iterates till no overlap
    annotations = []
    for j, k, label in zip(k.geometry.x, k.geometry.y, k.ref):
        annotations.append(plt.text(x,y, label,color='white',fontsize=15))
    adjust_text(annotations, arrowprops=dict(arrowstyle='-', color='white'))
    ctx.add_basemap(ax, source=ctx.providers.Esri.WorldImagery)
    

# use tight_layout to prevent labels plotting over each other
plt.tight_layout()
# always put plt.savefig before plt.show(), else returns blank output
plt.savefig()
plt.show()
