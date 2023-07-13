import pandas as pd
import os
import time
dirname = "data\\new"
stationa = '8841.03' #Mosholu
stationb = '2733.03' #Erik Pl
#stationa = '5659.05' #Test Ave A and E10th
#stationb = '5788.13' #Test Lafayette and E 8th
files = os.listdir(dirname) #code for gathering all data
#files = ['202102-citibike-tripdata.csv'] #smallest file, use for testing
print(files)
for x in files:
    start_time = time.time()
    print(x)
    filename = dirname +"\\"+ x
    singlefile = pd.read_csv(filename,parse_dates=["started_at","ended_at"],
        dtype={
            'start_station_id': 'category',
            'end_station_id': 'category',
            'start_station_name': 'category',
            'end_station_name': 'category',
            'rideable_type': 'category',
            'member_casual': 'category'
        })
    print("full month: ")
    print(singlefile.shape)
    print("--- %s seconds to read file ---" % (time.time() - start_time))
    if x == files[0]:
        ridesfroma = singlefile[singlefile.start_station_id==stationa]
        ridesfromb = singlefile[singlefile.start_station_id==stationb]
        print("from a: ")
        print(ridesfroma.shape)
        print("from b: ")
        print(ridesfromb.shape)
    else:
        ridesfroma = pd.concat([ridesfroma,singlefile[singlefile.start_station_id==stationa]])
        ridesfromb = pd.concat([ridesfromb,singlefile[singlefile.start_station_id==stationb]])
        print("from a: ")
        print(ridesfroma.shape)
        print("from b: ")
        print(ridesfromb.shape)
ridesfroma.to_csv('output\\ridesfroma.csv')
ridesfromb.to_csv('output\\ridesfromb.csv')
ridesatob = ridesfroma[ridesfroma.end_station_id==stationb]
ridesbtoa = ridesfromb[ridesfromb.end_station_id==stationa]
ridesbothways = pd.concat([ridesatob,ridesbtoa])
print(ridesbothways.shape)
ridesbothways.to_csv('output\\ridesbothways.csv')
