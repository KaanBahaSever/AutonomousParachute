#Latitude and Longitude
import random, math
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import pandas as pd
import io

class Coordinate:
    def __init__(self,Latitude,Longtitude):
        self.Latitude = round(Latitude,6)
        self.Longtitude = round(Longtitude,6)

    def __add__(self,A):
        return Coordinate(self.Latitude+A.Latitude, self.Longtitude+A.Longtitude)

    def __sub__(self,A):
        return Coordinate(self.Latitude-A.Latitude, self.Longtitude-A.Longtitude)

    def __str__(self):
        return str(round(self.Latitude,6))+','+str(round(self.Longtitude,6))


def Distance(coordinate1, coordinate2):
    r = 6371*1000 #metre
    
    dLat = (coordinate2.Latitude - coordinate1.Latitude) * math.pi / 180
    dLon = (coordinate2.Longtitude - coordinate1.Longtitude) * math.pi / 180

    rLat1 = (coordinate1.Latitude) * math.pi / 180
    rLat2 = (coordinate2.Latitude) * math.pi / 180
    
    delt = (pow(math.sin(dLat / 2),2) + pow(math.sin(dLon / 2),2) * math.cos(rLat1) * math.cos(rLat2))
 
    return 2 * r * math.asin(math.sqrt(delt))

class Rocket:

    def __init__(self,Altitude,Location):
        self.Altitude=Altitude
        self.Location=Location

    def setAltitude(self, newAltitude):
        self.Altitude=newAltitude

    def getAltitude(self):
        return self.Altitude

    def setLocation(self, newCoordinate):
        self.Location=newCoordinate

    def getLocation(self):
        return self.Location

Target = Coordinate(40.909491, 29.145550)

Initial_Coordinate = Coordinate(40.917469, 29.130507)

coor1 = Coordinate(40.909232, 29.146338)
coor2 = Coordinate(40.932968, 29.147540) #coor1 ve coor2 yukarıda gittim
coor3 = Coordinate(40.932709, 29.181208) #coor2 ve coor3 sağa gittim
coor4 = Coordinate(40.933098, 29.102013)  #coor3 ve coor4 sola gittim

Independency=Rocket(5000,Initial_Coordinate)

if random.choice([True,False]):
    if random.choice([True,False]):
        latitudeDiff=random.uniform(10,30)
        longtitudeDiff=random.uniform(10,30)
    else:
        latitudeDiff=random.uniform(-30,-10)
        longtitudeDiff=random.uniform(-30,-10)

else:
    if random.choice([True,False]):
        latitudeDiff=random.uniform(-30,-10)
        longtitudeDiff=random.uniform(10,30)
    else:
        latitudeDiff=random.uniform(10,30)
        longtitudeDiff=random.uniform(-30,-10)

latitudeDiff/=1000000
longtitudeDiff/=1000000

one=True

while Independency.getAltitude()>0:
    velocityVertical = random.uniform(6,10)
    a = Distance(Independency.getLocation(),Target)
    newLocation=Coordinate(Independency.getLocation().Latitude-latitudeDiff,Independency.getLocation().Longtitude-longtitudeDiff)
    b=Distance(Independency.getLocation(),newLocation)
    Independency.setLocation(newLocation)
    c = Distance(newLocation,Target)

    slope = (newLocation.Latitude - Initial_Coordinate.Latitude) / (newLocation.Longtitude - Initial_Coordinate.Longtitude)
    t=Initial_Coordinate.Latitude-(slope*Initial_Coordinate.Longtitude)
    Angle = math.degrees(math.acos((a**2+b**2-c**2)/(2*a*b)))
    
    if  one:
        if slope>0:
            if Initial_Coordinate.Latitude>newLocation.Latitude:
                if Target.Latitude < (slope * Target.Longtitude + t):
                    s='left'
                else:
                    s='right'
            else:
                if Target.Latitude < (slope * Target.Longtitude + t):
                    s='right'
                else:
                    s='left'
        else:
            if Initial_Coordinate.Latitude>newLocation.Latitude:
                if Target.Latitude < (slope * Target.Longtitude + t):
                    s='right'
                else:
                    s='left'
            else:
                if Target.Latitude < (slope * Target.Longtitude + t):
                    s='left'
                else:
                    s='right'
        print(s)
        y='{0} , {1} , {2} , {3} , ({4}) , ({5}) , ({6})'.format(s,round(Angle),slope,t,Target,newLocation,Initial_Coordinate)
        one=False

    Independency.setAltitude(Independency.getAltitude() - velocityVertical)

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

lons, lats = m(Initial_Coordinate.Longtitude,Initial_Coordinate.Latitude) #Roket
m.scatter(lons, lats, marker = 'o', color='r', zorder=3)
plt.text(lons, lats,'Roket')

lons, lats = m(Target.Longtitude, Target.Latitude) #Target
m.scatter(lons, lats, marker = 'o', color='r', zorder=3)
plt.text(lons, lats,'Target')

lons, lats = m(Independency.Location.Longtitude, Independency.Location.Latitude) #End
m.scatter(lons, lats, marker = 'o', color='r', zorder=3)
plt.text(lons, lats,'End')
plt.show()

u=input('Çıktı Doğru mu? = ')
k='{0} , {1}'.format(y,u)
with open('log.txt','a') as f:
     f.write(k)
     f.close()
