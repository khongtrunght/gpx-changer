from sys import argv
import gpxpy
import gpxpy.gpx
from datetime import datetime, timedelta
import pytz

def cut_gpx(gpx, before, after):
    for track in gpx.tracks:
        for segment in track.segments:
            length = len(segment.points)
            truoc = int(length * before)
            sau = int((1 - after) * length)
            segment.points = segment.points[truoc:sau]

def main():
    try :
        filename = argv[1]
        outfile = argv[2]
    except:
        # filename = 'data/test.gpx'
        # outfile = 'data/test2.gpx'
        filename = input('enter filename:')
        outfile = input('enter outfile:')

    gpx_file = open(f'{filename}', 'r')
    gpx = gpxpy.parse(gpx_file)    
    before = float(input('Cut truoc: ') )           
    after = float(input('Cut sau: '))
    cut_gpx(gpx, before, after)
    with open(outfile, "w") as f:
        f.write(gpx.to_xml())

if __name__ == '__main__':
    main()