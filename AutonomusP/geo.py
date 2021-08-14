import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import pandas as pd
import io

u = u"""latitude,longitude
40.917469,29.130507
"""

# read in data to use for plotted points
buildingdf = pd.read_csv(io.StringIO(u), delimiter=",")
lat = buildingdf['latitude'].values
lon = buildingdf['longitude'].values

# determine range to print based on min, max lat and lon of the data
margin = 2 # buffer to add to the range
lat_min = min(lat) - margin
lat_max = max(lat) + margin
lon_min = min(lon) - margin
lon_max = max(lon) + margin

# create map using BASEMAP
m = Basemap(
            projection='merc',
            resolution = 'h',
            area_thresh=10000.,
            llcrnrlon=26, llcrnrlat=36,
            urcrnrlon=45, urcrnrlat=42
            )
m.drawcoastlines()
m.drawcountries()
m.drawstates()
m.drawmapboundary(fill_color='#46bcec')
m.fillcontinents(color = 'white',lake_color='#46bcec')

lons, lats = m(29.13050740,40.917469) #Roket
m.scatter(lons, lats, marker = 'o', color='r', zorder=3)
plt.text(lons, lats,'Roket')

lons, lats = m(29.145550, 40.909491) #Target
m.scatter(lons, lats, marker = 'o', color='r', zorder=3)
plt.text(lons, lats,'Target')

lons, lats = m(29.130967, 40.916989) #End
m.scatter(lons, lats, marker = 'o', color='r', zorder=3)
plt.text(lons, lats,'End')
plt.show()
