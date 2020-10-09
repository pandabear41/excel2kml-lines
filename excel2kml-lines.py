import pandas
import simplekml


kml = simplekml.Kml()
dfIn = pandas.read_excel("Test.xlsx")
total = len(dfIn.index)
count = 0

for index, row in dfIn.iterrows():
    count += 1
    print("Completed {} of {} Line Conversions.".format(count, total))
    if row['OBJECTID']:
        ls = kml.newlinestring(name=str(row['OBJECTID']))
        ls.coords = [(float(row['LONGITUDE_BEGIN']),float(row['LATITUDE_BEGIN']),10.0),(float(row['LONGITUDE_END']),float(row['LATITUDE_END']),10.0)]
        ls.extrude = 1
        ls.altitudemode = simplekml.AltitudeMode.relativetoground
        ls.style.linestyle.width = 4
        ls.style.linestyle.color = simplekml.Color.red

kml.save("AllBridges.kml")