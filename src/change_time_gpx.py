from sys import argv
import gpxpy
import gpxpy.gpx
from datetime import datetime, timedelta
import pytz

def change_time(gpx, new_time):
    delta = new_time - gpx.time
    gpx.time = gpx.time + delta 
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                point.time = point.time + delta
 
def main():
    try :
        filename = argv[1]
        outfile = argv[2]
    except:
        # filename = 'data/Afternoon_Walk.gpx'
        # outfile = 'data/test.gpx'
        filename = input('enter filename:')
        outfile = input('enter outfile:')
    gpx_file = open(f'{filename}', 'r')
    gpx = gpxpy.parse(gpx_file)
    print("time now: ", gpx.time)
    datetime_str = input("Time to shift to ('%Y-%m-%d %H:%M:%S') :")
    datetime_obj = datetime.strptime(datetime_str + '+0700', '%Y-%m-%d %H:%M:%S%z' )
    print(datetime_obj)
    # datetime_obj = datetime_obj.replace(tzinfo=pytz.timezone('Etc/GMT+7'))
    # hours_shift = int(input("Number of hours to shift ( add '-' if when to shift backward) : "))
    change_time(gpx, datetime_obj) 
    with open(outfile, "w") as f:
        f.write(gpx.to_xml())

if __name__ == '__main__':
    main()
