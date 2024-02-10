from shapely.geometry import Point, LineString

def start_end_points(line: LineString):
    
    start_point = Point(line.coords[0])
    end_point = Point(line.coords[-1])

    return start_point, end_point